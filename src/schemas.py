from pydantic import BaseModel


class Build(BaseModel):
    name: str
