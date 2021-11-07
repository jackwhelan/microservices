pipeline {
    agent any
    stages {
        stage("Docker Build") {
            steps {
                sh "docker build -t jackwhelan/data-access-precode:${BUILD_TAG} data-access -f data-access/Dockerfile"
            }
        }
        stage("Pylint") {
            steps {
                sh "docker run --name ${BUILD_TAG}-linting jackwhelan/data-access-precode:${BUILD_TAG} pylint data-access"
            }
        }
        stage("Pytest") {
            steps {
                sh "pushd data-access"
                sh "docker run --name ${BUILD_TAG}-unit-tests jackwhelan/data-access-precode:${BUILD_TAG} pytest"
                sh "popd"
            }
        }
        stage("Cleanup") {
            steps {
                sh "docker stop ${BUILD_TAG}-linting ${BUILD_TAG}-unit-tests | true"
                sh "docker rm ${BUILD_TAG}-linting ${BUILD_TAG}-unit-tests | true"
                sh "docker rmi jackwhelan/data-access-precode:${BUILD_TAG} | true"
            }
        }
    }
}