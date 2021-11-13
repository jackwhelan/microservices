def MICROSERVICE_VERSION;
def REPO_VERSION;

pipeline {
    agent {
        label SLAVE
    }
    stages {
        stage("Repo Version Bump") {
            steps {
                script {
                    if (REPO_VERSION_TYPE == 'auto') {
                        if (MICROSERVICE_VERSION_TYPE == 'major') {
                            REPO_VERSION_TYPE = 'minor';
                        } else if (MICROSERVICE_VERSION_TYPE == 'minor' || MICROSERVICE_VERSION_TYPE == 'patch') {
                            REPO_VERSION_TYPE = 'patch';
                        }
                    }
                }
                sh "docker run -v ${env.WORKSPACE}/VERSION:/app/microservice/VERSION ${DOCKER_REPO}/version-bump:latest ${REPO_VERSION_TYPE}"
                script {
                    REPO_VERSION = readFile 'VERSION'
                }
            }
        }
        stage("Microservice Version Bump") {
            when {
                expression { MICROSERVICE_VERSION_TYPE != 'none' }
            }
            steps {
                sh "docker run -v ${env.WORKSPACE}/${MICROSERVICE}/VERSION:/app/microservice/VERSION ${DOCKER_REPO}/version-bump:latest ${MICROSERVICE_VERSION_TYPE}"
                script {
                    MICROSERVICE_VERSION = readFile "${MICROSERVICE}/VERSION"
                }
            }
        }
        stage("Build") {
            when {
                expression { MICROSERVICE_VERSION_TYPE != 'none' }
            }
            steps {
                sh "docker build -t ${DOCKER_REPO}/${MICROSERVICE} ${MICROSERVICE} -f ${MICROSERVICE}/Dockerfile"
            }
        }
        stage("Tag Image") {
            when {
                expression { MICROSERVICE_VERSION_TYPE != 'none' }
            }
            steps {
                sh "docker image tag ${DOCKER_REPO}/${MICROSERVICE} ${DOCKER_REPO}/${MICROSERVICE}:latest"
                sh "docker image tag ${DOCKER_REPO}/${MICROSERVICE} ${DOCKER_REPO}/${MICROSERVICE}:${MICROSERVICE_VERSION}"
            }
        }
        stage("Publish") {
            when {
                expression { MICROSERVICE_VERSION_TYPE != 'none' }
            }
            steps {
                sh "docker push ${DOCKER_REPO}/${MICROSERVICE}:latest"
                sh "docker push ${DOCKER_REPO}/${MICROSERVICE}:${MICROSERVICE_VERSION}"
            }
        }
        stage("Pushing Git Tags and Version file Changes (ms update)") {
            when {
                expression { MICROSERVICE_VERSION_TYPE != 'none' }
            }
            steps {
                sh "git tag -a \"v${REPO_VERSION}\" -m \"${MICROSERVICE} bumped to v${MICROSERVICE_VERSION}\""
                sh "git add VERSION"
                sh "git add ${MICROSERVICE}/VERSION"
                sh "git commit -m \"${MICROSERVICE} v${MICROSERVICE_VERSION} built and published to ${DOCKER_REPO}/${MICROSERVICE} on Dockerhub.\""
                sh "git push origin HEAD:master --follow-tags"
            }
        }
        stage("Pushing Git Tags and Version file Changes (repo update)") {
            when {
                expression { MICROSERVICE_VERSION_TYPE == 'none' }
            }
            steps {
                sh "git tag -a \"v${REPO_VERSION}\" -m \"Repo related update\""
                sh "git add VERSION"
                sh "git commit -m \"Updating repo version file.\""
                sh "git push origin HEAD:master --follow-tags"
            }
        }
        stage("Cleanup") {
            steps {
                sh "docker rmi ${DOCKER_REPO}/${MICROSERVICE} | true"
                sh "docker rmi ${DOCKER_REPO}/${MICROSERVICE}:latest | true"
                sh "docker rmi ${DOCKER_REPO}/${MICROSERVICE}:${MICROSERVICE_VERSION} | true"
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}