pipeline {
    agent {
        kubernetes {
            label 'kaniko-agent'
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