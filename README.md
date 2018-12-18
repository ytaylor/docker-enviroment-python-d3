# DH-Visualization-Development-Enviroment
This repository includes a base environment to deploy a project has a back-end written in Python, version 3.6. The back-end runs a server implemented using the flask library.

In order to process information it is possible to use libraries like pandas, numpy or after as needed.

The javascript front-end depends on jquery and the visualizations are implemented using d3.js.

## Installing dependencies

The python dependencies are listed in the `requirements.txt` file, and can be installed using pip:
```
  pip install -r requirements.txt
```
At this point, there is no need to install any javascript dependencies.
They are all fetched and loaded directly from the web.

## Running the server locally
The server expects a /data folder, containing data files depending on the needs. 

Once the folder has been created, the server can be started with:
```
  python app.py
```
The front-end is accessible with a browser at `http://127.0.0.1:5000/`.

## Docker Image
Alternatively, we provide a docker image with a base environment to deploy a project that contains all dependencies.

# Build Docker Image
In this repository there are the files necesary for to build the image docker. Make sure you are still at the top level of your directory.

  docker build -t templateflaskpythond3 path_to_directory

# Run Docker Image
To run docker image

  docker run -p 5000:80 templateflaskpythond3

In case we need to work with data, we have to make sure that a folder containing. To map a data directory to a docker container directory you need to use the -v flag when using docker run like so.

  docker run -p 5000:80 -v /data/:/path_to_folder_add/ templateflaskpythond3
