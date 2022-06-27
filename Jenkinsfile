pipeline {  
  environment {
    registry = "dockerhub.flow-r.fr"
  }  
  agent any
  stages {
    stage('Checkout') {
      steps{
        checkout scm
      }
    }
    stage('Cloning Git') {
      steps {
        git([url: 'http://fl-git-213.flow-r.fr:11180/CI/FARC.git', branch: 'main', credentialsId: "472a59da-9b35-42cb-bf03-6996a91c0551"])
 
      }
    }
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build("dockerhub.flow-r.fr/farc:dev")
        }
      }
    }
    stage('Deploy Image') {
      steps{
        script {
            docker.withRegistry('') {
                    dockerImage.push()
                }
          }
        }
      }
    }
    post {
    always {
      sh"docker system prune -f" 
    }
  }
}

