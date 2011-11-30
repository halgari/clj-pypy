from clojure.lang.primitives import Obj

class InternalAtom(Obj):
    def __init__(self, value):
        self.value = value
    def deref(self):
        return self.value
    def set(self, fn):
        self.value = fn(self.value) 
            
