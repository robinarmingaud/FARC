pipeline {  
  environment {
    registry = "ingenicaflowr/FARC"
    registryCredential = 'Dockerhub'
  }  
  agent any  
  stages {
    stage('Checkout') {
            steps {
                script {
                    checkout scm
                }
            }
        }
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build("ingenicaflowr/farc:latest")
        }
      }
    }
    stage('Deploy Image') {
      steps{
         script {
            docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
          }
        }
      }
    }
  }
}