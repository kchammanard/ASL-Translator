## Description
Real-Time American Sign Language translation project using Mediapipe Hands and Deep Neural Networks. This project delivers an intuitive pipeline for data acquisition, annotation, and training. 

## Running
Use Makefile for building the project and running inference. You can install **make** with chocolatey:
```Shell
choco install make
```
Build docker image (takes around 5 minutes)
```Shell
cd ASL-Translator
make docker-build
```
Run inference 
**Note** - You MUST allow docker to access your camera, otherwise your camera cannot be opened
```Shell
make run-inference
```
