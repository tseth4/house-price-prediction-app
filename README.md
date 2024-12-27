```
docker build -t frontend-react .
docker run -d -p 5717:5717 frontend-react

docker build -t backend-flask .
docker run -d -p 5000:5000 backend-flask

```
