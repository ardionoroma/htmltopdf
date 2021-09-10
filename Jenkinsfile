pipeline {
    agent any
   
    stages{
        stage('Checkout'){
            steps {
		        checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/ardionoroma/htmltopdf']]])
            }
        }
        
        stage('Static Analysis with SonarQube') {
   	        steps {
                script {
                    sh '''/var/lib/jenkins/sonar-scanner/bin/sonar-scanner \
                    -Dsonar.projectKey=htmltopdf \
                    -Dsonar.sources=. \
                    -Dsonar.css.node=. \
                    -Dsonar.host.url=http://192.168.1.112:9000\
                    -Dsonar.login=e16d050cc719b1a24fb747ccbfc1a1d631c4e6eb'''
                }
       		}
	    }
	}
}