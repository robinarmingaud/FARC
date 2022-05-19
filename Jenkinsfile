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
                    sh 'apt-get install git-lfs'
                    sh 'git lfs pull'
                    sh 'docker build -t fl-git-213.flow-r.me:5000/farc:latest .'
                    sh 'docker push fl-git-213.flow-r.me:5000/farc:latest'
                }
            }
        }
      }
  }