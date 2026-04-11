pipeline {
    agent any
    

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds') // Jenkins credentials ID
        DOCKERHUB_REPO = "kavitakhandelwal/github_gists"
        //KUBECONFIG = credentials('minikube-kubeconfig')
        //HELM_NAMESPACE = "mynamespace"
        //HELM_RELEASE = "myapp"
    }

    stages {
        stage('Verify Cluster Access') {
            steps {
                //sh 'kubectl cluster-info'
                sh 'kubectl get pods'
            }
        }

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
