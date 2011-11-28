from clojure.lang.primitives import Obj, BoolObj
from clojure.lang.list import List, EmptyList
from clojure.lang.var import Var, push_frame, Binding, pop_frame
from clojure.lang.symbol import Symbol
from clojure.lang.primitives import Obj, IntObj

class RecurInfo(Obj):
	def set_recur(self, recur):
		self._inrecur = recur
	def get_recur(self):
		return self._inrecur

_RecurInfo = RecurInfo()

class UserFn(Obj):
    def __init__(self, bindings, forms):
        self._bindings = bindings
        self._forms = forms
    def evaluate(self):
        return self
    def invoke(self, args):
    	res = None
    	while True:
    		res = self.inner_invoke(args)
    		if _RecurInfo.get_recur() is not None:
    			args = _RecurInfo.get_recur()
    		else:
    			break
    		_RecurInfo.set_recur(None)
    	return res		
    def inner_invoke(self, args):
        binds = EmptyList()
        bs = self._bindings
        for x in range(self._bindings.length().int_value()):
            binds = binds.cons(Binding(bs.first(), args[x]))
            bs = bs.rest()
        push_frame(binds)
        form = self._forms
        res = None
        for x in range(len(form)):
            res = form[x].evaluate()
        pop_frame()
        return res
    def is_builtin(self):
        return BoolObj(False)
        
        

class Fn(Obj):
    def __init__(self):
        pass
    def is_builtin(self):
        return BoolObj(True)
    def evaluate(self):
        return self
    def invoke(self, args):
        return UserFn(args[0], args[1:])
        
class If(Obj):
	def __init__(self):
		pass
	def is_builtin(self):
		return BoolObj(True)
	def evaluate(self):
		return self
	def invoke(self, args):
		res = args[0].evaluate().bool_value()
		if res:
			return args[1].evaluate()
		if len(args) == 2:
			return None
		return args[2].evaluate()
		
class Def(Obj):
	def __init__(self):
		pass
	def is_builtin(self):
		return BoolObj(True)
	def evaluate(self):
		return self
	def invoke(self, args):
		val = args[1].evaluate()
		return Var(args[0], val)


class Recur(Obj):
	def __init__(self):
		pass
	def is_builtin(self):
		return BoolObj(True)
	def evaluate(self):
		return self
	def invoke(self, args):
		nlist = []
		for x in range(len(args)):
			nlist.append(args[x].evaluate())
		_RecurInfo.set_recur(nlist)
		return None
  
recur = Var(Symbol.from_string("recur"), Recur())  
d = Var(Symbol.from_string("def"), Def())	    	
fn = Var(Symbol.from_string("fn"), Fn())	
    	
ifsym = Var(Symbol.from_string("if"), If())	
        
