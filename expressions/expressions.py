class Expression:

    def __init__(self, operands):
        self.operands = operands

    def __add__(self, other):
        return Add(self, other)
    
    def __sub__(self, other):
        return Sub(self, other)
    
    def __mul__(self, other):
        return Mul(self, other)
    
    def __truediv__(self, other):
        return Div(self, other)
    
    def __pow__(self, other):
        return Pow(self, other)
    
class Operator(Expression):
    def __repr__(self):
        return type(self).__name__ + repr(self.operands)
    
    def __str__(self):
        

