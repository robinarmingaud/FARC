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
                    checkout([  $class: 'GitSCM', 
                          branches: [[name: 'refs/heads/'+"${main}"]],
                          extensions: [[$class: 'GitLFSPull']]
                                      +[[$class: 'CloneOption', timeout: 30]],
                          userRemoteConfigs: [
                                [credentialsId: "${f09f43a11f2277048a0657d186517e35c963c182}",
                                url: "${http://192.168.160.24:11180/CI/FARC}"]
                          ]
                    ])
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