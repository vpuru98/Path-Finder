

class ClickHandler():

    def __init__(self, region, action):
        self.region = region
        self.action = action

        if action is None:
            self.callable = self.nothing
            self.arguments = {}
        else:
            self.callable = action['callable']
            self.arguments = action['arguments']

    def click_in_region(self, click_pos):
        if self.region[0] + self.region[2] >= click_pos[0] >= self.region[0] and self.region[1] + self.region[3] >= click_pos[1] >= self.region[1]:
            return True
        else:
            return False

    def handle(self, click_pos):
        if self.click_in_region(click_pos):
            self.callable(**self.arguments)

    @staticmethod
    def nothing():
        pass

    def __repr__(self):
        return 'ClickHandler({}, {})'.format(repr(self.region), repr(self.action))
