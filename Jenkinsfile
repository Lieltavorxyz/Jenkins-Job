pipeline {
    agent any
    stages {
        stage ("Fetching.....") {
            steps {
                echo "========Fetching========"
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