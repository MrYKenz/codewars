import operator


class Calculator(object):
    operations = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    def __init__(self):
        self.result = []

    def evaluate(self, string):
        self.result = string.split(' ')
        self.calc('*/')
        self.calc('+-')
        return float(self.result[0])

    def calc(self, operators):
        i = 1
        while i < len(self.result) - 1:
            if self.result[i] in operators:
                self.result[i - 1] = str(self.operations[self.result[i]](float(self.result[i - 1]), float(self.result[i + 1])))
                self.result.pop(i + 1)
                self.result.pop(i)
                continue
            i += 1
