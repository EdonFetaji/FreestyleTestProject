node {
    def frontend, backend
    def imageTag = "${env.BRANCH_NAME}-${env.BUILD_NUMBER}"
    def latestTag = "${env.BRANCH_NAME}-latest"

    stage('Clone Repository') {
        checkout scm
    }

    stage('Build Images') {
        frontend = docker.build("edon505/freestyle-project-frontend", "./frontend")
        backend  = docker.build("edon505/freestyle-project-backend", "./backend")
    }

    stage('Push Images') {
        docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
            frontend.push(imageTag)
            frontend.push(latestTag)
            backend.push(imageTag)
            backend.push(latestTag)
        }
    }
}
