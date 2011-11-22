from primitives import Obj, StrObj
from clojure.lang.list import List, EmptyList

_named = {}

_frames = EmptyList()

class Binding:
    def __init__(self, k, v):
        self._k = k
        self._v = v
    def k(self):
        return self._k
    def v(self):
        return self._v

def push_frame(frame):
    global _frames
    _frames = _frames.cons(frame)
    
def lookup(sym):
    global _frames
    print _named, sym, _frames
    if len(_frames) != 0:
        h = _frames.first()
        while h.rest() is not None:
            if (h.first().k() == sym):
                return h.first().v()
            h = h.rest()
    return _named[sym]



class Var(Obj):
	def __init__(self, name, value):
		self._name = name
		self._value = value
		_named[name] = self
		print _named
	def evaluate(self):
		return self._value.evaluate()
		
		
	

