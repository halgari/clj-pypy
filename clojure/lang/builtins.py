from clojure.lang.primitives import Obj, BoolObj
from clojure.lang.list import List, EmptyList
from clojure.lang.var import Var, push_frame, Binding, pop_frame
from clojure.lang.symbol import Symbol
from clojure.lang.primitives import Obj, IntObj
from clojure.lang.afn import AFn

class RecurInfo(Obj):
	def __init__(self):
		self._inrecur = None
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
    def apply(self, args):
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
			binds = binds.cons(Binding(bs.first(), args.first().evaluate()))
			args = args.rest()
			bs = bs.rest()
        push_frame(binds)
        form = self._forms
        res = None
        res = form.evaluate()
        pop_frame()
        return res
    def is_builtin(self):
        return BoolObj(False)
        
        

class Fn(AFn):
    def __init__(self):
        pass
    def is_builtin(self):
        return BoolObj(True)
    def evaluate(self):
        return self
    def invoke2(self, arg0, arg1):
        return UserFn(arg0, arg1)
        
class If(AFn):
	def __init__(self):
		pass
	def is_builtin(self):
		return BoolObj(True)
	def evaluate(self):
		return self
	def invoke3(self, arg0, arg1, arg2):
		res = arg0.evaluate().bool_value()
		if res:
			return arg1.evaluate()
		return arg2.evaluate()
		
class Def(AFn):
	def __init__(self):
		pass
	def is_builtin(self):
		return BoolObj(True)
	def evaluate(self):
		return self
	def invoke2(self, arg0, arg1):
		val = arg1.evaluate()
		return Var(arg0, val)


class Recur(Obj):
	def __init__(self):
		pass
	def is_builtin(self):
		return BoolObj(True)
	def evaluate(self):
		return self
	def apply(self, args):
		nlist = []
		while args is not None:
			nlist.append(args.first().evaluate())
			args = args.rest()
		_RecurInfo.set_recur(List.from_list(nlist))
		return None
  
recur = Var(Symbol.from_string("recur"), Recur())  
d = Var(Symbol.from_string("def"), Def())	    	
fn = Var(Symbol.from_string("fn"), Fn())	
    	
ifsym = Var(Symbol.from_string("if"), If())	
        
