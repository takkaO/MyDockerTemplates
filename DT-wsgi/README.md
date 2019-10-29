# Docker template [Apache + php + WSGI(python)]

## Make image
```
cd DT-wsgi
docker build -t wsgi-docker .
```

## Make container
1. Edit share volume path in ```docker-compose.yml```
2. Execute ```docker-compose up -d```
3. Access ```http://localhost:8080/test_wsgi/test.py```
