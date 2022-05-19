pipeline {  
  environment {
    registry = "fl-git-213.flow-r.me:5000"
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
                    dockerImage = docker.build("fl-git-213.flow-r.me:5000/farc:latest")
                    docker.withRegistry( '') {
                    dockerImage.push()
                }
            }
        }
      }
    }
}