--up/pre:
	docker run --name container \
		--hostname=quickstart.cloudera \
		--privileged=true \
		-i -t -d \
		--cpus=4 \
		-v $(shell pwd)/data:/data/ \
		-v $(shell pwd)/src:/src/ \
		--publish-all=true \
		-p 7180 \
		--rm \
		cloudera/quickstart bash

up: --up/pre
	docker exec container bash /usr/bin/docker-quickstart && \
	echo 'Up and ready!'

reduce_tasks = 1
run:
	docker exec -i container bash -c "./src/run_exercise.sh $(exercise) $(reduce_tasks)"

attach:
	docker attach container

down:
	docker stop container
