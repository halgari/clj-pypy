class Obj:
   """Base object all other object in PhaLinks inherit this"""
   def __init__(self):
       pass
   def to_str(self):
       return StrObj("UnknownObjType")
   def equals(self, other):
       return BoolObj(False)
   def is_builtin(self):
   	   return BoolObj(False)
   def __len__(self):
   	   return 0	   	   

class BoolObj(Obj):
   def __init__(self, value):
       self.boolvalue = value
   def bool_value(self):
       return self.boolvalue
   def __repr__(self):
       return "Bool("+str(self.boolvalue)+")"
   def type(self):
       from runtime.symbols import BoolType
       return BoolType
   def to_str(self):
       return str(self.boolvalue)
   def equals(self, other):
       if other.bool_value() == self.bool_value():
           return BoolObj(True)
       else:
           return BoolObj(False)
       return BoolObj(False)
   def evaluate(self):
   	   return self
   	   
class AppendDictObj(Obj):
    def __init__(self, init):
        self.dict = init
        
    def get(self, sym):
        return DictObj._static_get(sym)
        
    @purefunction
    @staticmethod
    def _static_get(d, sym):
        if sym in d:
            return d[sym]
        return None
            
    def assoc(self, sym, value):
        self.dict = self.dict.copy()[sym] = value

@purefunction
def boolean(v):
    return BoolObj(v)
    
BoolFalse = boolean(False)
BoolTrue = boolean(True)
       
class TypeObj(Obj):
   def __init__(self, value):
       self.typevalue = value
   def type_value(self):
       return self.typevalue
   def __repr__(self):
       return "Type("+str(self.typevalue)+")"
   

class FloatObj(Obj):
   """Represents a integer"""
   def __init__(self, value):
       self.floatvalue = value
   def float_value(self):
       return self.floatvalue
   def __repr__(self):
       return "Float("+str(self.floatvalue)+")"
   def evaluate(self):
   	   return self;

class IntObj(Obj):
   """Represents a integer"""
   def __init__(self, value):
       self.intvalue = value
   def int_value(self):
       return self.intvalue
   def __repr__(self):
       return "Int("+str(self.intvalue)+")"
   def type(self):
       from runtime.symbols import IntType
       return IntType
   def equals(self, other):
	   if other.int_value() == self.int_value():
		   return BoolObj(True)
	   else:
		   return BoolObj(False)
   def evaluate(self):
   	   return self       
   
class StrObj(Obj):
   """Represents a string"""
   def __init__(self, value):
       self.strvalue = value
   def str_value(self):
       return self.strvalue
   def evaluate(self):
   	   return self       
