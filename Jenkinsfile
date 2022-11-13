pipeline {
    agent any
    stages {
        stage ("Cloning.....") {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']]
                , extensions: [],
                 userRemoteConfigs: [[url: 'https://github.com/Lieltavorxyz/Jenkins-Job']]])
            }
        }
    
        stage ("Building.....") {
            steps {
                echo "=======Building========"            
            }
                    
        }
        stage ("Testing.....") {
            steps {
                echo "=======Testing========"
            }
        }
        stage ("Deploying.....") {
            steps {
                echo "=======Deploying========"
            }
        }
    }
    post {
        always {
            echo "=====+++++always+++++====="
        }
        success {
            echo "====++++only when successful++++===="
        }
        failure {
            echo "====++++only when failure++++===="
        }
    }
}