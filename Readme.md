## GetBuildsSortedTasks Microservice  <!-- omit in toc -->

## Summary

This microservice provides one endpoint `/get_tasks/`.
The endpoint expects the JSON body request containing the name of the build:
> {
>     "name": "reach_wind"
> }
>
The endpoint response is the JSON with the list of tasks related to this build sorted based on their dependencies.
> {
>     "sorted_tasks": [
>         "bring_maroon_golems",
>         "bring_silver_orcs"
>     ]
> }
>
The endpoint returns 404 error if the build name does not exist in the builds.yaml file.

## Setup

The project dependencies can be installed using `pyproject.toml` file with `poetry`.

## Start

The server is powered by `uvicorn`. To start the microservice run this command from te poetry environment:

> uvicorn main:app --reload

## Tests

Unittests can be run from the poetry environment with the command:
 > poetry run python -m pytest
 >

Use Postman of other http client to run API.
