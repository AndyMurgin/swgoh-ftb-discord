class ServiceLocator:
    def __init__(self):
        self.components = {}

    def load(self, key: str, instance):
        self.components[key] = instance

    def get_component(self, key: str):
        return self.components[key]
