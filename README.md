# python-bookstore

## Goals

- Get familiar with Python
- Understand REST API: https://www.kite.com/blog/python/flask-restful-api-tutorial/
- Work with Mongo DB driver

## Problem Statement
- Write a simple bookstore application using python
- Add persistance to your bookstore using MongoDB
- https://github.com/mongodb/mongo-go-driver
- A book resource can be represented as JSON below:
```
{
"id": "auto_generated_id",
"name": "Harry Potter and the Prisioner of Azkaban",
"author": "J K Rowling",
"ISBN": "134238982734",
"genre": "fantasy"
}
```
- Create the following APIs
```
POST /books : Creates a new book.
PUT /book/{id}: Updates a book.
GET /books: Returns a list of books in the store.
GET /book/{id}: Returns the book with id = {id}
DELETE /book/{id}: Deletes the book with id = {id}
DELETE /books: Deletes all books in the store
```
## Steps
- install Python 3
- Install Visual Source Code
- Install Python extension for VS Code
- Install MongoDB Python driver: https://docs.mongodb.com/drivers/pymongo
- Install Flask: `pip install Flask`
- install Flask-CORS: `pip install -U flask-cors`

## Tips
- Run MongoDB on docker
```
docker run mongo
```
## Bonus
- Write unit tests and generate code coverage reports

- Write a `Dockerfile` to build your application into a docker image
- https://docs.docker.com/develop/develop-images/dockerfile_best-practices/

- Create a k8s deployment for your service
- https://kubernetes.io/docs/tutorials/

- Deploy, upgrade, scale your service in your Kubernetes cluster. For this bootcamp, create a Kubernetes cluster using [`minikube`](https://github.com/kubernetes/minikube)

- Utilize http load test tools locust to load / perf test your APIs.

## Suggested Reading
* https://kubernetes.io/docs/tutorials/
* https://docs.docker.com/develop/develop-images/dockerfile_best-practices/

## To Run the App
```
env FLASK_APP=app.py flash run
```
