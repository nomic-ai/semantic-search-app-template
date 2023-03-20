# Building a Semantic Search Powered App
Tutorial and template for a semantic search app powered by the Atlas Embedding Database and FastAPI. 
Optional integrations include the OpenAI embedding API and Langchain.



### Starting the app

First build the FastAPI docker image. You only have to do this once and when you add new dependencies to the requirements.txt file:
```bash
DOCKER_BUILDKIT=1 docker build -t backend_api --progress plain -f backend/Dockerfile.buildkit .
```

Then, start the app:

```bash
docker compose up --build
```


## API Documentation

Once the app is started you can access its documentation and test its endpoint by going to:
```
localhost:80/docs
```