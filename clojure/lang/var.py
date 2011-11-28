from primitives import Obj, StrObj
from clojure.lang.list import List, EmptyList

class Globals(Obj):
	_named = dict()
	_frames = EmptyList()
	
	def push_frame(self, frame):
		self._frames = self._frames.cons(frame)
	
	def pop_frame(self):
		self._frames = self._frames.rest()
		
	def get_frames(self):
		return self._frames
		
	def get_named(self):
		return self._named
		
_Globals = Globals()

class Binding(Obj):
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
    _Globals.push_frame(frame)
    
def pop_frame():
	_Globals.pop_frame()
    
def lookup(sym):
    _frames = _Globals.get_frames()
    if _frames.length().int_value() != 0:
        h = _frames.first()
        while h is not None:
            if (h.first().k() == sym):
                return h.first().v()
            h = h.rest()
    return _Globals.get_named()[sym]



class Var(Obj):
	def __init__(self, name, value):
		self._name = name
		self._value = value
		_Globals.get_named()[name] = self
	def evaluate(self):
		return self._value.evaluate()
		
		
	

