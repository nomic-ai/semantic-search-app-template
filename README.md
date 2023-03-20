# Building a Semantic Search Powered App with Atlas
Tutorial and template for a semantic search app powered by the Atlas Embedding Database and FastAPI. 
Optional integrations include the OpenAI Embedding API and Langchain.


### Getting started
The typical process for building a semantic search app includes:
1. Gathering a dataset of text, images or other content you want your app to search through.
2. Generating [embeddings](https://vaclavkosar.com/ml/Embeddings-in-Machine-Learning-Explained) of your data. This is usually done using an Embedding API such as Cohere or OpenAI.
3. Writing code that performs vector similarity search over your embeddings and returns back your content.
4. Integrating all of this into a back-end which you can hit over a REST API.


This app template simplifies the process by providing a ready to deploy FastAPI and React app that interfaces with the [Atlas Embedding Database](https://docs.nomic.ai/how_does_atlas_work.html).

Atlas allow you to upload your content (text documents, embeddings) and instantly access semantic search over your data. Importantly, Atlas comes built with a visual debugger
allowing you to see the types of results your semantic search app will generate for any query.



### Starting the app

First build the FastAPI docker image. You only have to do this on initial build or when you add new dependencies to the requirements.txt file:
```bash
DOCKER_BUILDKIT=1 docker build -t backend_api --progress plain -f backend/Dockerfile.buildkit .
```

Then, start the backend with:

```bash
docker compose up --build
```

You will need to insert your Nomic API Key (giving your app access to your Atlas Embedding Database instance) into the [settings file](backend/app/api_v1/settings.py) or the [docker compose
environment variables](docker-compose.yaml).
You can find this API Key by making an [Atlas](atlas.nomic.ai/cli-login) account.

#### Uploading your content to Atlas

We will use demo news data in this tutorial. To upload the demo data go through the [Content Upload Tutorial](tutorial/semantic_search_data_upload.ipynb).

This tutorial stores your data in an Atlas Embedding DB project called '10k News Articles'.

You should paste this string as an environment variable into the [settings file](backend/app/api_v1/settings.py) for the variable `atlas_project_name`.


## Viewing your Apps API Documentation

Once the app is started you can access its documentation and test its endpoint by going to:
```
localhost:80/docs
```