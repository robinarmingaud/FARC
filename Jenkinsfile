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
                    def gitRemoteOriginUrl = scm.getUserRemoteConfigs()[0].getUrl()
                    echo 'The remote URL is ' + gitRemoteOriginUrl
                    scmVars = checkout([$class: 'GitSCM', branches: [[name: 'refs/heads/$BRANCH_NAME']], extensions [$class: 'GitLFSPull'],[$class: 'LocalBranch', localBranch: '**']], gitTool: 'git', userRemoteConfigs: [[credentialsId: "GitLab", url: gitRemoteOriginUrl]])
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