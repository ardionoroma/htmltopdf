pipeline {
    agent any

    parameters {
        string(name: 'projectKey', defaultValue: '')
        string(name: 'projectToken', defaultValue: '')
    }
   
    stages{
        stage('Static Analysis with SonarQube') {
   	        steps {
                script {
                    sh """/var/lib/jenkins/sonar-scanner/bin/sonar-scanner \
                    -Dsonar.projectKey=${params.projectKey} \
                    -Dsonar.sources=. \
                    -Dsonar.css.node=. \
                    -Dsonar.host.url=http://10.8.60.81:9090\
                    -Dsonar.login=${params.projectToken}"""
                }
       		}
	    }
	}
}