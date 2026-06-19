pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                echo 'Cloning repository...'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t keeperg/flask-app:jenkins .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker rm -f flask-app-jenkins || true'
                sh 'docker run -d --name flask-app-jenkins -p 5001:5000 keeperg/flask-app:jenkins'
            }
        }
    }
}
