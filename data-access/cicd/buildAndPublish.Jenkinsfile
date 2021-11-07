pipeline {
    agent {
        label SLAVE
    }
    stages {
        stage("Get Version from File") {
            steps {
                env.VERSION = readFile 'VERSION'
            }
        }
        stage("Build") {
            steps {
                sh "docker build -t jackwhelan/data-access data-access -f data-access/Dockerfile"
            }
        }
        stage("Tag Image") {
            steps {
                sh "docker image tag data-access data-access:latest"
                sh "docker image tag data-access data-access:${env.VERSION}"
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