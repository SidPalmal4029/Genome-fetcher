import json


class ConfigManager:

    def __init__(self, config_file):

        with open(config_file) as f:
            cfg = json.load(f)

        self.host = cfg["host"]
        self.user = cfg["user"]
        self.key = cfg.get("key_file")
        self.target = cfg["target"]
