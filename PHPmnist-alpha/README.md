# PHP MNIST Test

## Build Dockerfile
```
cd Docker  
docker build -t php-tf .
```

## Run docker-compose
```
cd Docker  
docker-compose up -d
```

## Setting
Copy ``` model, index.php, res.php, tf-test.py ``` into set volumes.
(For example: "C:/Users/csel-pc05/Desktop/html")  
See your ```docker-compose.yml```.


## How to use
Access ```http://localhost:8080```.


## 🚧 CAUTION 🚧
YOU CAN ONLY USE 28x28 IMAGES!!! (No resize code included.)
