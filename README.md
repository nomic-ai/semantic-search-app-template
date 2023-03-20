# Building a Semantic Search Powered App with Atlas
Tutorial and template for a semantic search app powered by the Atlas Embedding Database and FastAPI. 
Optional integrations include the OpenAI Embedding API and Langchain.


### Getting started
To build a semantic search powered app, you normally need to:
1. Gather your dataset of text, images or other content you want your app to search through.
2. Generate [embeddings](https://vaclavkosar.com/ml/Embeddings-in-Machine-Learning-Explained) of your data. This is usually done using an Embedding API such as Cohere or OpenAI.
3. Write code that performs vector similarity search over your embeddings and returns back your content.
4. Integrate all of this into a back-end which you can hit over a REST API.

This app template simplifies this process by providing a ready to deploy FastAPI and React app that interfaces with the [Atlas Embedding Database](https://docs.nomic.ai/how_does_atlas_work.html).
Atlas allow you to load your content (text documents, embeddings) and instantly access semantic search over your data. Additionally, it comes built with a visual debugger
that allows you to see the types of results your semantic search app will generate for any query.



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