class Scheduler:
    def __init__(self, workers=4):
        self.workers = workers
    def run(self, tasks):
        for task in tasks:
            task()
