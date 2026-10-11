
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
                bat '"C:\\Users\\atul\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat '"C:\\Users\\atul\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest -v'
            }
        }
    }
}
