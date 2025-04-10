pipeline {
    agent any

    stages {
        stage('Clonar repo') {
            steps {
                git 'https://github.com/J-Sebastian22/Pagos.git'
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                sh 'python3 -m unittest discover -s . -p "test_*.py"'
            }
        }
    }
}
