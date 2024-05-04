docker-build:
	docker build -t hand-image .

run-inference:
	docker run --rm hand-image python src/main.py