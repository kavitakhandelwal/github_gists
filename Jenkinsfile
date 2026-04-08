pipeline {
    image 'python:3.11'

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds') // Jenkins credentials ID
        DOCKERHUB_REPO = "kavitakhandelwal/github_gists"
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
                   sh """
                    docker build -t ${DOCKERHUB_REPO}:${BUILD_NUMBER} .
                   """
                     
                }
            }
        }

        stage('API testing- Run Container and Execute Tests') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'docker run -d -p 8000:8000 --name myapp-test ${DOCKERHUB_REPO}:${BUILD_NUMBER}'
                sh 'pytest tests/ --maxfail=1 --disable-warnings -q'
                sh 'docker stop myapp-test && docker rm myapp-test'
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
            echo "Cleaned up Docker credentials"
        }
    }
}
