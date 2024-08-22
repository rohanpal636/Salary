pipeline {
    agent any

    environment {
        VENV_PATH = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the Git repository
                git 'https://github.com/rohanpal636/Salary.git'
            }
        }
        stage('Setup Environment') {
            steps {
                // Create and activate a Python virtual environment
                sh 'python3 -m venv ${VENV_PATH}'
                sh '. ${VENV_PATH}/bin/activate'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Install dependencies from requirements.txt
                sh '. ${VENV_PATH}/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                // Run your tests (e.g., using pytest)
                sh '. ${VENV_PATH}/bin/activate && pytest'
            }
        }
        stage('Build') {
            steps {
                // Add build steps if necessary
                echo 'Building the project'
            }
        }
    }
    
    post {
        always {
            // Clean up actions like deactivating the virtual environment
            sh 'deactivate || true'
        }
    }
}
