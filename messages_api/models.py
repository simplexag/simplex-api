
class Message:
    def __init__(self, text=""):
        self.metadata = Metadata()
        self.text = text


class Metadata:
    def __init__(self):
        self.api = "simplex_api"
        self.branch = "basic-role-based-access-control"
