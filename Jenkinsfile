pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build and Install') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m pytest -v'
            }
        }
    }
}
