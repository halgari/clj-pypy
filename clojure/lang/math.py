from clojure.lang.var import Var
from clojure.lang.symbol import Symbol
from clojure.lang.primitives import Obj, IntObj



class Add(Obj):
	def __init__(self):
		pass
	def evaluate(self):
		return self
	def invoke(self, args):
		return IntObj(args[0].int_value() + args[1].int_value())
		
add = Var(Symbol.from_string("+"), Add())

class Sub(Obj):
	def __init__(self):
		pass
	def evaluate(self):
		return self
	def invoke(self, args):
		return IntObj(args[0].int_value() - args[1].int_value())
		
sub = Var(Symbol.from_string("-"), Sub())

class Equals(Obj):
	def __init__(self):
		pass
	def evaluate(self):
		return self
	def invoke(self, args):
		return args[0].equals(args[1])
	
eq = Var(Symbol.from_string("="), Equals())


