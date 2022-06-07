pipeline {  
  environment {
    registry = "fl-git-213.flow-r.fr:5000"
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
          dockerImage = docker.build("fl-git-213.flow-r.me:5000/farc:latest")
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
 }
