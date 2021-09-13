pipeline {
    agent any
   
    stages{
        stage('Checkout'){
            steps {
		        checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: $gitUrl]]])
            }
        }
        
        stage('Static Analysis with SonarQube') {
   	        steps {
                script {
                    sh '''/var/lib/jenkins/sonar-scanner/bin/sonar-scanner \
                    -Dsonar.projectKey=$projectKey \
                    -Dsonar.sources=. \
                    -Dsonar.css.node=. \
                    -Dsonar.host.url=http://192.168.1.112:9000\
                    -Dsonar.login=$projectToken'''
                }
       		}
	    }
	}
}