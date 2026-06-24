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
        stage("build docker image") {
            steps {
                withCredentials([
                        usernamePassword(
                            credentialsId: 'DOCKER_CREDENTIAL',
                            usernameVariable: 'USER',
                            passwordVariable: 'PWD'
                        )
                    ])
                    sh "echo ${PWD} | docker login -u ${USER} --password-stdin"
                    sh "docker build -t  ."
                    sh "docker push \$USER/backend-ms1:${IMAGE_NAME}"
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
}

