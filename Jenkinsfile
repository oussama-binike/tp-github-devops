pipeline {
    agent any
    tools {
        maven 'maven'
        ansible 'ansible'
    }
    environment {
        DOCKER_IMAGE = "TON_USERNAME/shopping-cart"
        DOCKER_TAG = "latest"
    }
    stages {
        stage('test') {
        steps {
        sh 'echo "Running tests..."'
        }
    }
    }
}