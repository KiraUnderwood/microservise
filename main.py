import yaml
from fastapi import FastAPI, HTTPException

from src import schemas
from src.get_sorted_tasks import get_sorted_tasks_by_build_name, build_exists


app = FastAPI()

builds = {}
tasks = {}


@app.on_event("startup")
def read_yamls():
    with open(r"builds\builds.yaml", "r") as stream:
        global builds
        builds = yaml.safe_load(stream)
    with open(r"builds\tasks.yaml", "r") as stream:
        global tasks
        tasks = yaml.safe_load(stream)


@app.post("/get_tasks/")
def get_tasks(request: schemas.Build):
    try:
        build_exists(request.name, builds)
    except Exception as e:
        raise HTTPException(status_code=404, detail=repr(e))

    sorted_tasks = get_sorted_tasks_by_build_name(request.name, builds, tasks)
    return {"sorted_tasks": sorted_tasks}
