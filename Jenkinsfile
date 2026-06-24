pipeline {
    agent any

    tools {
        maven 'maven'
        ansible 'ansible'
    }

    environment {
        DOCKER_IMAGE = "ousssamabinike/shopping-cart-2"
        DOCKER_TAG = "latest"
    }

    stages {

        stage('COMPILE') {
            steps {
                sh 'mvn clean compile -DskipTests=true'
            }
        }

        stage('Build Docker Image') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'DOCKER_CREDENTIAL',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    sh '''
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                        docker build -t $DOCKER_IMAGE:$DOCKER_TAG .
                        docker push $DOCKER_IMAGE:$DOCKER_TAG
                    '''
                }
            }
        }

        stage('Ansible Deploy') {
            steps {
                ansiblePlaybook(
                    playbook: 'tp-ansible/deploy.yml',
                    inventory: 'tp-ansible/inventory.ini',
                    credentialsId: 'ansible-ssh',
                    colorized: true
                )
            }
        }
    }

    post {
        success {
            echo 'Pipeline Jenkins + Ansible terminé avec succès !'
        }

        failure {
            echo 'Pipeline échoué !'
        }

        always {
            echo 'Pipeline terminé !'
        }
    }
}
