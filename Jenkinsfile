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

    stage('Push Images (only on dev)') {
        if (env.BRANCH_NAME == 'dev') {
            docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
                frontend.push(imageTag)
                frontend.push(latestTag)
                backend.push(imageTag)
                backend.push(latestTag)
            }
            echo "Docker images pushed for branch: ${env.BRANCH_NAME}"
        } else {
            echo "Skipping Docker push: branch is ${env.BRANCH_NAME}"
        }
    }
}
