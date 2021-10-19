
class Callback:
    def __init__(self, function, **kwargs):
        self.function = function
        self.args = kwargs

    def putArgument(self, name, value):
        self.args[name] = value

    def call(self):
        self.function(**self.args)