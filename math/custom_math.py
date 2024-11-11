import sys
import types
import inflect
import importlib
start=1

# Initialize the inflect engine once
inflect_engine = inflect.engine()
class Math(types.ModuleType):
    def __init__(self,value):
        name=inflect_engine.number_to_words(value).replace(" ", "_").replace(".","Point").replace(",","").replace("-","_")
        super().__init__(name)
        self.val=value
        self.__path__ = []

        # Explicitly import the module into the current namespace
        setattr(sys.modules["__main__"],name,self)

        sys.modules[name]=self
    def __add__(self, other):
        if isinstance(other, Math):
            v = self.val + other.val
            return Math(v)
        return NotImplemented

    def __neg__(self):
        v = -self.val
        return Math(v)

    def __sub__(self, other):
        if isinstance(other, Math):
            v = self.val - other.val
            return Math(v)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Math):
            v = self.val * other.val
            return Math(v)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Math):
            v = self.val / other.val
            return Math(v)
        return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, Math):
            v = self.val // other.val
            return Math(v)
        return NotImplemented

    def __mod__(self, other):
        if isinstance(other, Math):
            v = self.val % other.val
            return Math(v)
        return NotImplemented

    def __pow__(self, other):
        if isinstance(other, Math):
            v = self.val ** other.val
            return Math(v)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Math):
            return self.val == other.val
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Math):
            return self.val != other.val
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Math):
            return self.val < other.val
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Math):
            return self.val <= other.val
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Math):
            return self.val > other.val
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Math):
            return self.val >= other.val
        return NotImplemented

print(Math(1))
sys.modules[__name__]=Math
