pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds') // Jenkins credentials ID
        DOCKERHUB_REPO = "kavitakhandelwal/my-repo"
        HELM_NAMESPACE = "mynamespace"
        HELM_RELEASE = "myapp"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                   // sh """
                   // docker build -t ${DOCKERHUB_REPO}:${BUILD_NUMBER} .
                   // """
                     sh 'docker build -t myapp:${BUILD_NUMBER} .'
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    sh """
                    echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin
                    docker push ${DOCKERHUB_REPO}:${BUILD_NUMBER}
                    """
                }
            }
        }

        
    }

    post {
        always {
            sh 'docker logout'
        }
    }
}
