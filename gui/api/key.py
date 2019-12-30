

class KeyHandler:

    def __init__(self):
        self.key_actions = {}

    def add_action(self, key, action):
        if not self.key_actions.has_key(key):
            self.key_actions[key] = []
        if action is not None:
            self.key_actions[key].append(action)

    def handle(self, key):
        if self.key_actions.has_key(key):
            for action in self.key_actions[key]:
                callable = action['callable']
                arguments = action['arguments']
                callable(**arguments)

    def __repr__(self):
        return 'KeyHandler()'
