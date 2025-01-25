pipeline {
    agent any
    
    environment {
        SSH_PASSWORD = credentials('SSH_PASSWORD')
    }

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
                sh 'ls'
                sh 'pwd'
                sshCommand remote: [
                    name: 'test',
                    host: 'tronxi.ddns.net',
                    user: 'tronxi',
                    password: SSH_PASSWORD,
                    port: 22,
                    allowAnyHosts: true 
                ], command: '''
                    cd workspace/jenkins_files/ &&
                    sh start.sh &&
                    sh kill.sh
                '''
            }
        }
    }
}
