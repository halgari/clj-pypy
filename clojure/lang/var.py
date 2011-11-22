from primitives import Obj, StrObj

_named = {}

def lookup(sym):
	print _named, sym
	return _named[sym]
	


class Var(Obj):
	def __init__(self, name, value):
		self._name = name
		self._value = value
		_named[name] = self
		print _named
	def evaluate(self):
		return self._value.evaluate()
		
		

