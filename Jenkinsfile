pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'calculator-env-demo'
    }

    stages {
        stage('Load .env Variables') {
            steps {
                script {
                    // Read and prepare environment variables for Docker
                    def envFile = readFile('parameters.env').split('\n')
                    def dockerEnvArgs = ''
                    envFile.each { line ->
                        if (line.trim() && !line.startsWith('#')) {
                            def (key, value) = line.tokenize('=')
                            value = value.trim().replaceAll('"', '')
                            dockerEnvArgs += "-e ${key}=${value} "
                        }
                    }

                    // Save env args to workspace for later use
                    writeFile file: 'docker_env_args.txt', text: dockerEnvArgs
                    echo "✅ Loaded environment variables: ${dockerEnvArgs}"
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    def dockerEnvArgs = readFile('docker_env_args.txt').trim()
                    sh "docker run --rm ${dockerEnvArgs} ${DOCKER_IMAGE}"
                }
            }
        }
    }
}
