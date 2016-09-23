class BaseSelect(object):
    def __init__(self, first_level, second_level, third_level):
        self.one = first_level
        self.two = second_level
        self.three = third_level


    def get_one(self):
        for i in  self.one:
            yield i

    def get_two(self):
        for i in  self.two:
            yield i

    def get_three(self):
        for i in  self.three:
            yield i
