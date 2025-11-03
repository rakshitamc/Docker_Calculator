def dockerImage
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
                    dockerImage = docker.build("calculator-env-demo")
                }
            }
        }

        stage('Run Calculator') {
            steps {
                script {
                    echo "▶️ Running calculator inside Docker container using plugin..."

                    // Use plugin method to run inside the container
                    dockerImage.inside("-e NUM1=${params.NUM1} -e NUM2=${params.NUM2} -e OPERATION=${params.OPERATION}") {
                        sh "python calculator.py"
                    }
                }
            }
        }
    }
}