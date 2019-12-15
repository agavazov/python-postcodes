from flask import Response


class ActionWrapper:
    def __init__(self, action):
        self.action = action
        self.response = Response(status=201, headers={})

    def __call__(self):
        self.action()
        return self.response
