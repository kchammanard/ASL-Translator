docker-build:
	docker build -t hand-image .

run-inference:
	docker run --rm mydocker python src/main.py