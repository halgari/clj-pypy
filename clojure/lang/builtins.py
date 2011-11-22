from clojure.lang.primitives import Obj, BoolObj
from clojure.lang.list import List, EmptyList
from clojure.lang.var import Var, push_frame
from clojure.lang.symbol import Symbol
from clojure.lang.primitives import Obj, IntObj

class UserFn(Obj):
    def __init__(self, bindings, forms):
        self._bindings = bindings
        self._forms = forms
    def evaluate(self):
        return self
    def invoke(self, args):
        binds = EmptyList()
        for x in range(len(self._bindings)):
            binds = binds.cons(self._bindings[x], args[x])
        push_frame(binds)
        form = self._forms
        res = None
        while form is not None:
            res = form.first().evaluate()
            form = form.rest()
        return res
        
        

class Fn(Obj):
    def __init__(self):
        pass
    def is_builtin(self):
        return BoolObj(True)
    def evaluate(self):
        return self
    def invoke(self, args):
        return UserFn(args[0], args[1:])
        
fn = Var(Symbol.from_string("fn"), Fn())	
        
