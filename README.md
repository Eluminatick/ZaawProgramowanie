# App for object recognition
## About project
App created as passing project for one of the classes at UEKat.
This app was created for image recognition from image. It's simple app build using ResNet50 from torchvision package, using currently best, default weights. Uses Fast API as an interface framework.
Runs on Python 3.9.

# Files
This project consists of files below:
- app/main.py - main file consisting whole application code
- app/test.py - file for testing hosted app with requests library
- requirements.txt - requierments file
- Dockerfile - dockerfile for building docker image

# API
API consists of single POST endpoint `/predict` which require image file in binary format.

# Usage 
To host applicatione locally:

 1. Clone repository.
 2. Ensure you have Python 3.9 or newer installed on your system.
 3. Install dependencies using `pip install -r requirements.txt`
 4. Run from command line `uvicorn main:app --reload` to run uvicorn web server.

Now you can check Swagger Documentation on site :`http://127.0.0.1:8000/docs`

If you want to test POST endpoint:
1. In test file:
    1. Change set `url` to `http://127.0.0.1:8000/predict`
    2. Change `'image.jpg'` to `'Path_to_your_image'`
 2. Run test.py. In terminal you should receive response from your application. 
 
# Docker
You can also run this application on docker container. For that:
1. Ensure you have installed docker on you computer.
2. Clone git repository.
3. From terminal run: `docker build -t resnet .`
4. After image will be built: `docker run -d --name resnet -p 80:8000 resnet`
5. Now you can access app on `http://localhost:80`

You can test this app in similar manner like above, just change url to `http://localhost:80`

# Hosted app
This application is currently hosted on AWS EC2 using docker image pushed to ECR. The POST endpoint can be found at adress: `http://18.184.77.184/predict/` (base adress in test.py). You can check this endpoint just by changing `'image.jpg'` in test file. 
