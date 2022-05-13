pipeline {  
  environment {
    registry = "ingenicaflowr/FARC"
    registryCredential = 'Dockerhub'
  }  
  agent any  
  stages {
    stage('Building image') {
      steps{
        sleep 3
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