import json


class Config:
    def __init__(self, token: str, prefix: str, owner: int):
        self.token = token
        self.prefix = prefix
        self.owner = owner


with open("config.json", "r") as config_json:
    config: Config = json.load(config_json, object_hook=(lambda dct: Config(**dct)))
