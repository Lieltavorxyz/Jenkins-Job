pipeline {
    agent any
    stages {
        stage ("Cloning.....") {
            steps {
                sh " git clone https://github.com/devopsPRO27/requests "
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