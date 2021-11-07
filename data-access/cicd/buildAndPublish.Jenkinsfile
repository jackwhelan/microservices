pipeline {
    agent {
        label SLAVE
    }
    environment {
        VERSION = readFile 'data-access/VERSION'
    }
    stages {
        stage("Version Bump") {
            steps {
                sh "docker run -v ${env.WORKSPACE}:/app/microservice jackwhelan/version-bump:latest ${VERSION_TYPE}"
            }
        }
        stage("Build") {
            steps {
                sh "docker build -t jackwhelan/data-access data-access -f data-access/Dockerfile"
            }
        }
        stage("Tag Image") {
            steps {
                sh "docker image tag jackwhelan/data-access jackwhelan/data-access:latest"
                sh "docker image tag jackwhelan/data-access jackwhelan/data-access:${env.VERSION}"
            }
        }
        stage("Publish") {
            steps {
                sh "docker push jackwhelan/data-access:latest"
                sh "docker push jackwhelan/data-access:${env.VERSION}"
            }
        }
        stage("Cleanup") {
            steps {
                sh "docker rmi jackwhelan/data-access | true"
                sh "docker rmi jackwhelan/data-access:latest | true"
                sh "docker rmi jackwhelan/data-access:${env.VERSION} | true"
            }
        }
    }
}