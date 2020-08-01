// Comentario
pipeline {
    agent any

    stages {
        stage('CheckOut git') {
            steps {
                git poll: true, url:'https://github.com/atacho7/test-jenkins1.git'
            }    
        }
        stage('Create Virtual Env') {
            steps {
               sh '''
                    bash -c "virtualenv entorno_virtual && source entorno_virtual/bin/activate"
               '''
            }
        }
        stage('Install Requirements') {
            steps {
                sh '''
                    bash -c "source entorno_virtual/bin/activate && entorno_virtual/bin/python entorno_virtual/bin/pip install -r requirements.txt"
                '''
            }
        }
        stage('Test App') {
            steps {
                sh '''
                    bash -c "source entorno_virtual/bin/activate && cd src && entorno_virtual/bin/python entorno_virtual/bin/pytest && cd .."
                ''' 
            }
        }
        stage('Run App'){
           steps {
                sh '''
                    bash -c "source entorno_virtual/bin/activate; entorno_virtual/bin/python src/main.py &"
                '''
           }
        }
        stage('Buid Docker'){
           steps {
                sh '''
                    docker build -t apptest:latest .
                '''
           }
        }
        stage('Push Docker Image'){
            steps {
                sh '''
                     docker tag apptest:latest atacho7/apptest:latest
                          docker push atacho7/apptest:latest
                          docker rmi apptest:latest
                '''
            }
        }    
   }
