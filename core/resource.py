import os


class Resource:
    def __init__(self, path):
        self.path = path
    def is_directory(self):
        return os.path.isdir(self.path)
    def is_file(self):
        return os.path.isfile(self.path)
