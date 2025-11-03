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
                    echo "Building Docker image..."
                    def dockerImage = docker.build("calculator-env-demo")
                }
            }
        }

        stage('Run Calculator') {
            steps {
                script {
                    echo "Running calculator in Docker container..."
                    bat """
                    docker run --rm ^
                        -e NUM1=${params.NUM1} ^
                        -e NUM2=${params.NUM2} ^
                        -e OPERATION=${params.OPERATOR} ^
                        calculator-env-demo
                    """
                }
            }
        }
    }
}
