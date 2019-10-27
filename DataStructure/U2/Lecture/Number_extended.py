from functools import total_ordering
import numbers

@total_ordering
class Number_extended:
    def __init__(self,value,side=None):
        self.v=value
        self.side=side
    def __eq__(self,other):
        if isinstance(other,numbers.Number):
            return self.v==other and self.side==None
        elif isinstance(other,Number_extended):
            return self.v==other.v and self.side==other.side
    def __lt__(self,other):
        if isinstance(other,numbers.Number):
            return (self.v<other or
                   (self.v==other and self.side==-1))
        elif isinstance(other,Number_extended):
            return (self.v<other.v or
              (self.v==other.v and
                (self.side,other.side) in ((-1,None),(-1,+1),(None,+1))))

a = Number_extended(5,+1)
print("a<5 ", a<5)
print("a>5 ", a>5)
print("a==5", a==5)
print("5>a ", 5>a)
print("5<a ", 5<a)
print("5==a", 5==a)
print("a==a", a==a)
print("a<a ", a<a)
print("a<=a", a<=a)
print("a+1 ", a+1)
