## Description
Real-Time American Sign Language translation project using Mediapipe Hands and Deep Neural Networks. This project delivers an intuitive pipeline for data acquisition, annotation, and training. 

## Running
Use Makefile for building the project and running inference. You can install **make** with chocolatey:
```Shell
choco install make
```
Build docker image
```Shell
docker build -t hand-image .
```
Run inference
```Shell
docker run --rm hand-image python src/main.py
```
