pipeline {
    agent {
        kubernetes {
            yaml """
apiVersion: v1
kind: Pod
spec:
  serviceAccountName: jenkins-sa
  containers:
  - name: jenkins
    image: jenkins_all_dependencies:latest
    command:
    - cat
    tty: true

  - name: kaniko
    image: gcr.io/kaniko-project/executor:latest
    command:
    - cat
    tty: true
    volumeMounts:
    - name: docker-config
      mountPath: /kaniko/.docker

  volumes:
  - name: docker-config
    secret:
      secretName: dockerhub-secret
"""
        }
    }

    environment {
        DOCKERHUB_REPO = "kavitakhandelwal/github_gists"
    }

    stages {

        stage('Verify Cluster Access') {
            steps {
                container('jenkins') {
                    sh 'kubectl get pods -n jenkins'
                }
            }
        }

        stage('Checkout') {
            steps {
                container('jenkins') {
                    checkout scm
                }
            }
        }

        stage('Build & Push Image (Kaniko)') {
            steps {
                container('kaniko') {
                    sh '''
                    /kaniko/executor \
                      --dockerfile=Dockerfile \
                      --context=$PWD \
                      --destination=${DOCKERHUB_REPO}:${BUILD_NUMBER}
                    '''
                }
            }
        }
    }
}