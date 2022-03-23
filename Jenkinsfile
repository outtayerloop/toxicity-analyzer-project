pipeline {
	agent any
    stages {
		stage('Clean Jenkins Workspace before starting'){
            steps{
				sh 'sudo rm -rf /var/lib/jenkins/caches/'
				sh 'sudo rm -rf /var/lib/jenkins/.cache/'
                cleanWs()
            }
        }
        stage('Clone repository') { 			
            steps {              
                git([url:'https://github.com/wiwiii/toxicity-analyzer.git', credentialsId: 'toxicity-analyzer-token'])
				sh  'git checkout ${GIT_BRANCH}'
				sh 'git config --global user.email "${GITHUB_MAIL}"'
				sh 'git config --global user.name "${GITHUB_USERNAME}"'
            }
	    } 
		//RUN UNIT TEST AND PUSH TO DEVELOP
		stage('Run unit tests on Feature branch and push to develop'){
			when {
                branch 'feature/*'
            }
			steps {
				dir('back') {
					sh '/home/ubuntu/.poetry/bin/poetry install'
					sh '/home/ubuntu/.poetry/bin/poetry run python -m pytest ./tests/unit'
				}
				dir('model') {
					sh '/home/ubuntu/.poetry/bin/poetry install'
					sh '/home/ubuntu/.poetry/bin/poetry run python -m pytest ./tests/unit'
				}
				sh 'git checkout develop'
				withCredentials([gitUsernamePassword(credentialsId: 'toxicity-analyzer-token', gitToolName: 'git-tool')]) {
					sh 'git merge ${GIT_BRANCH}'
					sh 'git push -u origin develop'
				}
			}
		}
		//RUN STRESS TEST AND PUSH TO RELEASE
		stage('Run stress tests on Develop branch and push to release'){
			when {
                branch 'develop'
            }
			steps {
				dir('model') {
					sh '/home/ubuntu/.poetry/bin/poetry install'
					sh '/home/ubuntu/.poetry/bin/poetry run locust --config ./tests/stress/locust.conf'
				}
				sh 'git checkout release'
				withCredentials([gitUsernamePassword(credentialsId: 'toxicity-analyzer-token', gitToolName: 'git-tool')]) {
					sh 'git merge develop'
					sh 'git push -u origin release'
				}
			}
		}
		//RUN INTEGRATION/E2E TEST AND PUSH TO MASTER
		stage('Run integration and e2e tests and push to master'){
			when {
                branch 'release'
            }
			steps {
				sh 'rm ./front/vue.config.js'
				sh 'sed -i "s/start_http_server[(]ct[.]get_local_prometheus_server_port[(][)][)]/#prometheus_server/g" ./model/app.py'
				sh 'sed -i "s/start_http_server[(]ct[.]get_local_prometheus_server_port[(][)][)]/#prometheus_server/g" ./back/app.py'
				dir('model') {
					sh '/home/ubuntu/.poetry/bin/poetry install'
					sh '/home/ubuntu/.poetry/bin/poetry run python -m pytest ./tests/integration'
					sh 'sed -i "s/poetry/\\/home\\/ubuntu\\/.poetry\\/bin\\/poetry/g" ./tests/back/BaseBackTestLaunch.py'
					sh '/home/ubuntu/.poetry/bin/poetry run python -m pytest -s ./tests/back/launch_back_integration_tests.py'
					sh 'sed -i "s/\\/home\\/ubuntu\\/[.]poetry\\/bin\\/poetry/poetry/g" ./tests/back/BaseBackTestLaunch.py'
				}
				dir('back') {
					sh '/home/ubuntu/.poetry/bin/poetry install'
				}
                dir('front') {
					sh 'npm install'
					sh 'sed -i "63,65d" ./src/components/Home.vue'
					sh 'sed -i "64d" ./src/components/Home.vue'
					sh 'sed -i "s/poetry/\\/home\\/ubuntu\\/.poetry\\/bin\\/poetry/g" ./package.json'
					sh 'npm run jenkins:run'
					sh 'sed -i "s/\\/home\\/ubuntu\\/[.]poetry\\/bin\\/poetry/poetry/g" ./package.json'
					sh 'sudo rm -rf ./node_modules'
					sh 'sudo rm -rf /var/lib/jenkins/caches/pypoetry'
					sh 'sudo rm -rf /var/lib/jenkins/.cache/pypoetry'
				}
				sh 'git reset --hard'
				sh 'git checkout master'
				withCredentials([gitUsernamePassword(credentialsId: 'toxicity-analyzer-token', gitToolName: 'git-tool')]) {
					sh 'git merge release'
					sh 'git push -u origin master'
				}
			}
		}
		//BUILD DOCKER IMAGES AND PUSH TO DOCKERHUB
		stage('Release Docker images'){
			when {
                branch 'master'
            }
			steps{
				sh 'sudo docker-compose up --remove-orphans --build --no-start'
				sh 'sudo docker tag toxicity-analyzer-front start2015/toxicity-analyzer-front'
				sh 'sudo docker logout'
				sh 'sudo docker login -u "${DOCKER_USERNAME}" -p "${DOCKER_PWD}" docker.io'
				sh 'sudo docker push start2015/toxicity-analyzer-front:latest'				
				sh 'sudo docker tag toxicity-analyzer-back start2015/toxicity-analyzer-back'
				sh 'sudo docker logout'
				sh 'sudo docker login -u "${DOCKER_USERNAME}" -p "${DOCKER_PWD}" docker.io'
				sh 'sudo docker push start2015/toxicity-analyzer-back:latest'
				sh 'sudo docker tag toxicity-analyzer-model start2015/toxicity-analyzer-model'
				sh 'sudo docker logout'
				sh 'sudo docker login -u "${DOCKER_USERNAME}" -p "${DOCKER_PWD}" docker.io'
				sh 'sudo docker push start2015/toxicity-analyzer-model:latest'
				sh 'sudo docker-compose down --rmi "all" -v --remove-orphans'
				sh 'sudo docker system prune -f'
			}
		}
    }
}