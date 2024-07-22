from pydantic import BaseModel


class PplConfig(BaseModel):
    def __str__(self):
        return str(self.model_dump_json(indent=4))