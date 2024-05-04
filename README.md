## Description
Real-Time American Sign Language translation project using Mediapipe Hands and Deep Neural Networks. This project delivers an intuitive pipeline for data acquisition, annotation, and training. 

## Running
Use Makefile for building the project and running inference. You can install **make** with chocolatey:
```Shell
choco install make
```
Build docker image (takes around 3 minutes)
```Shell
cd ASL-Translator
make docker-build
```
Load the model and data using dvc
```Shell
choco install make
```
Run inference
```Shell
make run-inference
```
