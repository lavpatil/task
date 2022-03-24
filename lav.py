pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Build code'
            }
        }
        stage('Test') {
            steps {
                echo 'test code'
            }
        }
        stage('connect') {
            steps {
                echo 'connecting'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploy code'
            }
        }
    }
}
