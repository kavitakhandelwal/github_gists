pipeline {
    agent {
        kubernetes {
            cloud 'kubernetes'
            yaml '''
apiVersion: v1
kind: Pod
spec:
  serviceAccountName: jenkins-sa
  containers:
  - name: build-tools
    image: alpine/k8s:1.29.2  # Lightweight image with kubectl, helm, and git
    command: ['cat']
    tty: true
  - name: kaniko
    image: gcr.io/kaniko-project/executor:debug
    env:
      - name: DOCKER_CONFIG
        value: /kaniko/.docker/
    command: ['sleep']
    args: ['99d']
    volumeMounts:
      - name: kaniko-secret
        mountPath: /kaniko/.docker
  volumes:
    - name: kaniko-secret
      secret:
        secretName: dockerhub-secret
        items:
          - key: .dockerconfigjson
            path: config.json
'''
        }
    }
    environment {
        DOCKERHUB_REPO = "kavitakhandelwal/github_gists"
    }


    stages {
        stage('Checkout & Verify') {
            steps {
                container('build-tools') {
                    // This container handles the Git checkout and cluster checks
                    checkout scm
                    //sh 'kubectl get pods -n jenkins'
                }
            }
        }

        stage('Build & Push') {
            steps {
                container('kaniko') {
                    withEnv(['DOCKER_CONFIG=/kaniko/.docker/']) {
                   sh 'ls -la /kaniko/.docker/ && cat /kaniko/.docker/config.json'
                    // This container handles ONLY the image building
                    sh '/kaniko/executor --dockerfile=Dockerfile --context=dir://${WORKSPACE} --destination=${DOCKERHUB_REPO}:${BUILD_NUMBER}-NEW'
                }
            }
        }
    }

    stage('Deploy to Minikube') {
    steps {
        container('build-tools') {
            // This replaces the image tag in the YAML dynamically
            sh "sed -i 's|image: kavitakhandelwal/github_gists:latest|image: kavitakhandelwal/github_gists:${BUILD_NUMBER}-NEW|g' deploy/deployment.yaml"
            
            // Apply the deployment
            sh 'kubectl apply -f deploy/deployment.yaml'
            
            sh 'kubectl apply -f deploy/service.yaml'
            // Verify rollout
            sh 'kubectl rollout status deployment/github-gists-api'
        }
    }
    }
}
}