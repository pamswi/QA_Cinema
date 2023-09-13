pipeline {
    agent any
    environment {
        DOCKERHUB_LOGIN = credentials('DOCKERHUB_LOGIN')
        DATABASE_URI = credentials('DATABASE_URI')
        MYSQL_ROOT_PASSWORD = credentials('MYSQL_ROOT_PASSWORD')
    }
    stages {
        stage('Build') {
            steps {
                sh "sudo apt-get update && sudo apt-get install -y python3-pip"
            }
        }
        stage('Dependencies') {
            steps {
                sh "pip install -r requirements.txt"
            }
        }
        stage('Building Containers') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'DOCKERHUB_LOGIN', usernameVariable: 'DOCKERHUB_LOGIN_USR', passwordVariable: 'DOCKERHUB_LOGIN_PSW')]) {
                        sh "docker login -u \$DOCKERHUB_LOGIN_USR -p \$DOCKERHUB_LOGIN_PSW"
                        sh "export DATABASE_URI=${DATABASE_URI}"
                        sh "bash scripts/containers.sh"
                    }
                }
            }
        }
        stage('Deploy to Docker Swarm') {
            steps {
                

                sh "docker stack deploy -c docker-compose.yaml cinema_app_stack"


                sh "docker stack services cinema_app_stack"
            }
        }
    }
}
