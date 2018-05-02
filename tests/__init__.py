class IsInstance:
    def __init__(self, type):
        self.type = type

    def __eq__(self, other):
        print('isinstance?', isinstance(other, self.type))
        return isinstance(other, self.type)

    def __ne__(self, other):
        return not isinstance(other, self.type)

    def __repr__(self):
        return str(self.type)
