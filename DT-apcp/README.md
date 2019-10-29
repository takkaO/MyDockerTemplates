# Docker template [Apache + php + CGI(python)]

## Make image
```
cd DT-apcp
docker build -t cgi-docker .
```

## Make container
1. Edit share volume path in ```docker-compose.yml```
2. Execute ```docker-compose up -d```
3. Access ```http://localhost:8080/cgi-bin/test.py```

## 🚧Caution🚧
You should use **LF** as line feed code in cgi file.  
DON'T USE **CRLF** !!!!!


## Memo
```/etc/apache2/conf-available/serve-cgi-bin.conf```  
```a2enmod cgi.load```
```docker restart hogehoge```