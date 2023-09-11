pipeline {
    agent any
    environment {
        DOCKERHUB_LOGIN=credentials('DOCKERHUB_LOGIN')
        DATABASE_URI=credentials('DATABASE_URI')
    }
    stages {
        stage('Build') {
            steps {
                sh 'sudo apt-get update && sudo apt-get install -y python3-pip'
            }
        }
        stage('Dependencies') {
            steps {
                sh "pip install -r requirements.txt"
            }
        }
        // stage('Testing') {
        //     steps {
        //         // add testing steps
        //     }
        // }
        stage('Deploy') {
            steps {
                sh "python3 app.py"
            }
        }
    }
}
// add environment config
// install dependencies
// add docker step to build containers from images...