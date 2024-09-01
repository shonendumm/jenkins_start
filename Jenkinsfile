pipeline {
    agent any
    environment {
        NEW_VERSION = "1.0.0"
        CSRF_CREDENTIALS = credentials('CSRF_SECRET') // store and get credentials from Jenkins
    }
    stages {
        stage("build") {
            steps {
                echo "Building the project.."
                echo "building version: ${NEW_VERSION}" // need double quotes for string interpolation
                echo "CSRF_CREDENTIALS: ${CSRF_CREDENTIALS}"
            }
        }

        stage("test") {
            when {
                expression {
                    BRANCH_NAME == "master" || BRANCH_NAME == "dev" // or env.BRANCH_NAME == "master" , env variable available
                }
            }
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
