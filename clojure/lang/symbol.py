from primitives import Obj, StrObj

_symbols = {}

_interned = {}

SymbolType = None

def intern(value):
   if value in _interned:
       return _interned[value]
   _interned[value] = value
   return value

class Symbol(Obj):
   """Defines a symbol. these are basically interned strings"""
   def __init__(self, value):
       self.value = value
   
   @staticmethod
   def intern(value):
       var = intern(value.str_value())
       if var in _symbols:
          return _symbols[var]
       sym = Symbol(var)
       _symbols[var] = sym
       return sym
   
   @staticmethod
   def from_string(str):
       return Symbol.intern(StrObj(str))
   
   def type(self):
       return SymbolType
   
   def __repr__(self):
       return "Sym("+self.value+")"
   def evaluate(self):
   	   from clojure.lang.var import lookup
   	   return lookup(self).evaluate()
   

SymbolType = Symbol.from_string("SymbolType")
