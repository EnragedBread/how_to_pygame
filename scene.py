class Scene():
    def __init__(self):
        self.manager = None

    def handle_event(self, event):
        raise NotImplementedError

    def render(self, screen):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError