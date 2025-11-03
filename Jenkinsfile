pipeline {
    agent any

    parameters {
        string(name: 'NUM1', defaultValue: '10', description: 'Enter first number')
        string(name: 'NUM2', defaultValue: '5', description: 'Enter second number')
        choice(name: 'OPERATION', choices: ['+', '-', '*', '/'], description: 'Select operation')
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build image with Docker plugin
                    def dockerImage = docker.build("calculator-env-demo", 
                        "--build-arg NUM1=${params.NUM1} --build-arg NUM2=${params.NUM2} --build-arg OPERATION=${params.OPERATION} ."
                    )
                }
            }
        }

        stage('Run Docker Container') {
           steps {
                script {
                    // ✅ Use Linux-style working directory & mount
                    docker.image('calculator-env-demo').inside('-v /workspace:/app -w /app') {
                        withEnv([
                            "NUM1=${params.NUM1}",
                            "NUM2=${params.NUM2}",
                            "OPERATOR=${params.OPERATOR}"
                        ]) {
                            sh 'python calculator.py'
                        }
                    }
                }
            }
        }
    }
}