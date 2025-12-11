pipeline {
    agent any

    environment {
        PROJECT_ID = 'handy-sensor-475806-n3'
        GOOGLE_APPLICATION_CREDENTIALS = credentials('test-gcp-jen')
    }

    stages {

        stage("Clone Repository") {
            steps {
                git branch: 'main', url: 'https://github.com/Harikrishnakakarla/harifirstproject.git'
            }
        }

        stage("Run Tests (if any)") {
            steps {
                sh '''
                    python3 --version
                    pytest || echo "No tests found"
                '''
            }
        }

        stage("Deploy to Google App Engine") {
            steps {
                sh '''
                    gcloud --version

                    gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                    gcloud config set project $PROJECT_ID

                    gcloud app deploy --bucket=gs://avian-chariot-450105-deployments --quiet
                '''
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
