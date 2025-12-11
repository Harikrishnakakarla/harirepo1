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

        stage("Setup Python & Install Dependencies") {
            steps {
                sh '''
                    # Install Python tools (safe for Debian)
                    sudo apt update
                    sudo apt install -y python3-full

                    # Create Virtual Environment
                    python3 -m venv venv
                    source venv/bin/activate

                    # Install pip safely
                    pip install --upgrade pip

                    # Install Poetry
                    curl -sSL https://install.python-poetry.org | python3
                    export PATH="$HOME/.local/bin:$PATH"

                    # Install project dependencies
                    pip install -r requirements.txt
                '''
            }
        }

        stage("Run Tests") {
            steps {
                sh '''
                    source venv/bin/activate
                    pytest
                '''
            }
        }

        stage("Deploy to Google App Engine") {
            steps {
                sh '''
                    # Check gcloud installation
                    gcloud --version

                    # Authenticate using service account
                    gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}

                    # Set project
                    gcloud config set project $PROJECT_ID

                    # Deploy to App Engine
                    gcloud app deploy --bucket=gs://avian-chariot-450105-deployments --quiet
                '''
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            cleanWs()
        }

        success {
            echo 'Deployment successful!'
        }

        failure {
            echo 'Deployment failed!'
        }
    }
}
