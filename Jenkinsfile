pipeline {
    agent any
    environment {
        // Define credentials for Docker Hub login, database URI, and MySQL root password
        DOCKERHUB_LOGIN = credentials('DOCKERHUB_LOGIN')
        DATABASE_URI = credentials('DATABASE_URI')
        MYSQL_ROOT_PASSWORD = credentials('MYSQL_ROOT_PASSWORD')
    }
    stages {
        stage('Build') {
            steps {
                // Install Python dependencies
                sh "sudo apt-get update && sudo apt-get install -y python3-pip"
            }
        }
        stage('Dependencies') {
            steps {
                // Install Python project dependencies
                sh "pip install -r requirements.txt"
            }
        }
        // testing steps to run
        stage('Testing') {
            steps {
                sh "bash scripts/testing.sh"
            }
        }
        stage('Building Containers') {
            steps {
                script {
                    // Log in to Docker Hub securely
                    withCredentials([usernamePassword(credentialsId: 'DOCKERHUB_LOGIN', usernameVariable: 'DOCKERHUB_LOGIN_USR', passwordVariable: 'DOCKERHUB_LOGIN_PSW')]) {
                        sh "docker login -u \$DOCKERHUB_LOGIN_USR -p \$DOCKERHUB_LOGIN_PSW"
			sh "export DATABASE_URI=${DATABASE_URI}"

                        // Build containers using a script
                        sh "bash scripts/containers.sh"
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                // Create and run Python scripts for deployment
                // "python3 create.py"
                // sh "python3 app.py"
                sh "docker-compose up -d"
            }
        }
    }
}
