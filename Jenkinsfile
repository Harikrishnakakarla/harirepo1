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

        stage("Setup Python Environment") {
            steps {
                sh '''
                    # Create virtual environment
                    python3 -m venv venv
                    source venv/bin/activate

                    # Upgrade pip
                    pip install --upgrade pip

                    # Install Poetry
                    curl -sSL https://install.python-poetry.org | python3
                    export PATH="$HOME/.local/bin:$PATH"

                    # Install dependencies
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