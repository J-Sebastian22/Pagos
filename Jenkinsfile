pipeline {
    agent any

    stages {
        stage('Clonar repo') {
            steps {
                git branch: 'main', url: 'https://github.com/J-Sebastian22/Pagos.git'
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                sh 'python3 -m unittest test_pago.py'
            }
        }
    }
}
