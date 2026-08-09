pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
               }
        }

        stage('Set Up Environment') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\pip install --upgrade pip'
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\pytest -v --html=reports\\report.html --self-contained-html'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'reports/*.html', allowEmptyArchive: true
        }
    }
}