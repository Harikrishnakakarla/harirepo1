pipeline {
    agent any

    environment {
        PROJECT_ID = 'handy-sensor-475806-n3'
        GOOGLE_APPLICATION_CREDENTIALS = credentials('test-gcp-jen')  // Service account credential
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Harikrishnakakarla/harifirstproject.git'
            }
        }

        stage('Install Dependencies') {
             steps {
                 script {
                     sh '''
                     curl -sS https://install.python-poetry.org | python3
                     export PATH="$HOME/.local/bin:$PATH"
                     pip3 install --upgrade pip
                     pip install -r requirements.txt
                     '''
                }
             }
         }
        stage('Run Tests'){
            steps {
                script{
                    sh 'pytest'
                }
            }       
        }

        stage('Deploy to Google App Engine') {
            steps {
                script {
                    // Check gcloud installation and working directory
                    sh 'gcloud --version'
                    sh 'pwd'
                    sh 'ls -l'  // List files to verify app.yaml presence

                    // Authenticate with Google Cloud
                    sh 'gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}'

                    // Set the GCP project
                    sh 'gcloud config set project $PROJECT_ID'

                    // Deploy the application to App Engine
                    sh 'gcloud app deploy --bucket=gs://avian-chariot-450105-deployments --quiet'
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            cleanWs()  // Cleans workspace
        }

        success {
            echo 'Deployment successful!'
        }

        failure {
            echo 'Deployment failed!'
        }
    }
}
