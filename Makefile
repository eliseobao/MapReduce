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

run:
	docker exec -i container bash < ./scripts/exercise_$(exercise).sh

attach:
	docker attach container

down:
	docker stop container
