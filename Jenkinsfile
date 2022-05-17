pipeline {  
  environment {
    registry = "ingenicaflowr/FARC"
    registryCredential = 'Dockerhub'
  }  
  agent any  
  stages {
    stage('Clean') {
      steps {
        script {
          cleanWs()
        }
      }
    }
    stage('Build and Deploy') {
            steps {
                script {
                    checkout scm
                    dockerImage = docker.build("ingenicaflowr/farc:latest")
                    docker.withRegistry( '', registryCredential ) {
                    dockerImage.push()
                }
            }
        }
      }
    }
}