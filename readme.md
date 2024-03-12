## ML model deployment with FastAPI & Docker

Hello, I would like to share with you this go to template that involves creating an Language detaction App with FastAPI 😁.

Let's dive in by introducing what is this project about and why I have done it.

### 1. What is this project about?

On this project you can checkout how you can build an basic API using FastAPI as backend to be able to use custom models in any project

### 2. Why I did built it?
For the past couple of months I've been studying about Fast API. I wanted to create a basic template with Fast API to server custome made models to serve the frontends.

#### What is Fast API?
FastAPI is a high-performance web framework used to build APIs (Application Programming Interfaces) in Python. It's known for its speed and ease of use, making it a popular choice among developers. Here are some key points about FastAPI:

- Performance:  FastAPI is known for being very fast, comparable to frameworks in languages like Node.js and Go.

- Developer Friendly:  It boasts features that make development faster and with fewer errors. These include automatic data validation, clear error messages, and interactive API documentation.

- Pythonic:  FastAPI leverages standard Python type hints, making the code intuitive and easy to understand.

- Modern:  It's a relatively new framework (first released in 2018) built with contemporary design principles.

What I like from FastAPI is the ability to create API's quickly without too much hassle. 

##### Resources
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)

### Project Structure
```
└── 📁app
    └── main.py
    └── 📁model
        └── 📁data
            └── language_detection.csv
        └── model-0.1.0.pkl
        └── model.ipynb
        └── model.py
        └── transform.pkl
```

### Setup and run it

Clone using the Repo. with web URL.

 `https://github.com/salmansrizon/fas-api-dev-template.git`

Create your environment and activate your environment

```
python -m venv venv 
source venv/bin/activate
pip install -r requirements.txt
```
Startup Fast API
```
uvicorn main:app -- host 0.0.0.0 --port 8885

```