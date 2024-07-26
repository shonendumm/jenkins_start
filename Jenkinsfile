pipeline {
    agent any

    stages {

        stage("build") {
            steps {
                echo "Building the project.."
            }
        }

        stage("test") {
            steps {
                echo "Testing the project.."
            }
        }   

        stage("deploy") {
            steps {
                echo "Deploying the project.."
            }
        }
    }
    post {
        always {
            echo "This will always run"
        }
        success {
            echo "This will run only if successful"
        }
        failure {
            echo "This will run only if failed"
        }
    }

}
