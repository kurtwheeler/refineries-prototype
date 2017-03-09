build:
	docker build -t docker-test .

run:
	docker run --name test-worker -v /home/kurt/Development/prototyping/testDir:/testDir --link some-rabbit:rabbit -d docker-test

stop:
	docker rm test-worker -f

master:
	docker build -t master-test .

test:
	docker run --name master-test --link some-rabbit:rabbit master-test

rabbit:
	docker run -d --hostname my-rabbit --name some-rabbit rabbitmq:3
