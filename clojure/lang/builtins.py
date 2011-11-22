from clojure.lang.primitives import Obj, BoolObj
from clojure.lang.list import List, EmptyList
from clojure.lang.var import Var, push_frame, Binding
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
        bs = self._bindings
        for x in range(len(self._bindings)):
            binds = binds.cons(Binding(bs.first(), args[x]))
            bs = bs.rest()
        push_frame(binds)
        form = self._forms
        res = None
        print ">>>->>", len(form)
        for x in range(len(form)):
            print ">>> form ", x, form[x]
            res = form[x].evaluate()
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
        
fn = Var(Symbol.from_string("fn"), Fn())	
        
