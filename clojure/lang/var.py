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
    def __repr__(self):
    	return str(self._k) + "->" + str(self._v)    	

def push_frame(frame):
    global _frames
    _frames = _frames.cons(frame)
    
def pop_frame():
	global _frames
	_frames = _frames.rest()
    
def lookup(sym):
    global _frames
    if len(_frames) != 0:
        h = _frames.first()
        while h is not None:
            if (h.first().k() == sym):
                return h.first().v()
            h = h.rest()
    return _named[sym]



class Var(Obj):
	def __init__(self, name, value):
		self._name = name
		self._value = value
		_named[name] = self
	def evaluate(self):
		return self._value.evaluate()
		
		
	

