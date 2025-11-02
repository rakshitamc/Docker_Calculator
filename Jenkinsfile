pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'calculator-env-demo'
    }

    stages {
        stage('Load .env Variables') {
            steps {
                script {
                    def envFile = readFile('parameter.env').split('\n')
                    envFile.each {
                        if (it.trim() && !it.startsWith('#')) {
                            def pair = it.split('=')
                            env[pair[0]] = pair[1].replaceAll('"', '')
                        }
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t ${DOCKER_IMAGE} .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh '''
                    docker run --rm \
                    -e NUM1=$NUM1 \
                    -e NUM2=$NUM2 \
                    -e OPERATION=$OPERATION \
                    ${DOCKER_IMAGE}
                    '''
                }
            }
        }
    }
}
