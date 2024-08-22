pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                
                git 'https://github.com/rohanpal636/Salary.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                
                sh 'pytest'
            }
        }
    }
    
    post {
        always {
            
            junit 'test-results/*.xml'
        }
    }
}
