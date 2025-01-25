pipeline {
    agent any
    
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
                sh 'ls'
                sh 'pwd'
                withCredentials([usernamePassword(credentialsId: 'SSH_CREDENTIALS', usernameVariable: 'SSH_USER', passwordVariable: 'SSH_PASS')]) {
                    sshCommand remote: [
                        name: 'test',
                        host: 'tronxi.ddns.net',
                        user: SSH_USER,
                        password: SSH_PASS,
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
}
