from clojure.lang.var import Var
from clojure.lang.symbol import Symbol
from clojure.lang.primitives import Obj, IntObj
from clojure.lang.afn import AFn


class Add(AFn):
	def __init__(self):
		pass
	def evaluate(self):
		return self
	def invoke2(self, arg0, arg1):
		return IntObj(arg0.int_value() + arg1.int_value())
		
add = Var(Symbol.from_string("+"), Add())

class Sub(AFn):
	def __init__(self):
		pass
	def evaluate(self):
		return self
	def invoke2(self, arg0, arg1):
		return IntObj(arg0.int_value() - arg1.int_value())
		
sub = Var(Symbol.from_string("-"), Sub())

class Equals(AFn):
	def __init__(self):
		pass
	def evaluate(self):
		return self
	def invoke2(self, arg0, arg1):
		return arg0.equals(arg1)
	
eq = Var(Symbol.from_string("="), Equals())


from clojure.lang.wrapfn import wrapfn

def println(o):
	print o

exec wrapfn("println", println)

from clojure.lang.var import _Globals
print _Globals.get_named()
