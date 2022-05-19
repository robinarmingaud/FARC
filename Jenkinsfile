pipeline {  
  environment {
    registry = "fl-git-213.flow-r.me:5000"
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
        git([url: 'http://fl-git-213.flow-r.me:11180/CI/FARC.git', branch: 'main'])
 
      }
    }
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build fl-git-213.flow-r.me:5000/farc:latest
        }
      }
    }
    stage('Deploy Image') {
      steps{
        script {
            dockerImage.push(fl-git-213.flow-r.me:5000/farc:latest)
          }
        }
      }
    }
}
