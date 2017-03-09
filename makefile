build:
	docker build -t docker-test .

run:
	docker run --name test-worker -v /home/kurt/Development/prototyping/testDir:/testDir --link some-rabbit:rabbit -d docker-test

stop:
	docker rm test-worker -f

test:
	python master.py
