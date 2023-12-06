pipeline {
    agent any

    // parameters {
    //     string(name: 'PROJECT_NAME', defaultValue: 'fnd', description: 'Specify your project name')
    // }

    environment {
        DOCKER_USERNAME = 'BhawnaGarg2508'
        DOCKER_PASSWORD = 'BhawnaGarg-2508'
        DOCKER_IMAGE_NAME = 'house-price-pred'
        DOCKER_CONTAINER_NAME = 'house-price-pred-c'
        PATH = "/usr/local/bin:$PATH"
    }

    stages {
        stage('Checkout') {
            steps {
                sh "echo 'Checkout SCM'"
                checkout scm
            }
        }

        stage('Build') {
            steps {
                script {
                    try {
                        sh 'echo "Building the repository"'
                        // Add any build steps specific to your project
                    } catch (Exception buildException) {
                        currentBuild.result = 'FAILURE'
                        throw buildException
                    }
                }
            }
        }

        // stage('Test') {
        //     steps {
        //         script {
        //             try {
        //                 sh 'python3 test_unit.py'
        //             } catch (Exception testException) {
        //                 currentBuild.result = 'FAILURE'
        //                 throw testException
        //             }
        //         }
        //     }
        // }

        stage('Deploy') {
            steps {
                script {
                    try {
                        echo 'Deploying the application'

                        // Log into Docker
                        sh "echo ${DOCKER_PASSWORD} | docker login -u ${DOCKER_USERNAME} --password-stdin"

                        // Build Docker image
                        sh "docker build -t ${DOCKER_IMAGE_NAME} ."

                        // Run Docker container with port exposure
                        sh "docker run -d -p 8000:3000 --name ${DOCKER_CONTAINER_NAME} ${DOCKER_IMAGE_NAME}"

                        // Wait for the web app to start
                        sleep time: 30, unit: 'SECONDS'

                        // Print Docker container logs for debugging
                        sh "docker logs ${DOCKER_CONTAINER_NAME}"
                    } catch (Exception deployException) {
                        currentBuild.result = 'FAILURE'
                        throw deployException
                    }
                }
            }
        }
    }

    post {
        failure {
            script {
                echo 'Before email notification'

                // Stop and remove the Docker container
                sh 'docker stop ${DOCKER_CONTAINER_NAME} || true'
                sh 'docker rm ${DOCKER_CONTAINER_NAME} || true'

                // Send email notification with web app URL and failure details
                emailext subject: "Web App Build and Test Results - ${currentBuild.result}",
                    body: """
                    See Jenkins console output for details.

                    Web App URL: http://your-jenkins-server:8000

                    Failure Details:
                    - Build: ${currentBuild.result == 'FAILURE' ? 'Failed' : 'Successful'}
                    - Unit Test: ${currentBuild.result == 'FAILURE' ? 'Failed' : 'Successful'}
                    - Deployment: ${currentBuild.result == 'FAILURE' ? 'Failed' : 'Successful'}
                    """,
                    recipientProviders: [
                        [$class: 'CulpritsRecipientProvider'],
                        [$class: 'DevelopersRecipientProvider'],
                        [$class: 'RequesterRecipientProvider']
                    ],
                    replyTo: '$DEFAULT_REPLYTO',
                    to: '$DEFAULT_RECIPIENTS'

                echo 'After email notification'
            }
        }
    }
}
