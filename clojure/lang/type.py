
from clojure.lang.internal_atom import InternalAtom
from clojure.lang.symbol import sym


class TypeDef:
	def __init__(self, name):
		self.name = name
	def name():
		return self.name
	def __repr__(self):
		return "TypeDef<"+self.name.__repr__()+">"
		
		
class Protocol(Obj):
	def __init__(self, name, fns):
		Var(name, self)
		self.implementors = {}
	def add_implementor(self, tp):
		self.implementors[tp] = tp
	def implements(self, obj)
		from clojure.lang.primitives import BoolTrue, BoolFalse
		if obj.type() in self.implementors:
			return BoolTrue
		return BoolFalse
	
		

class Record(Obj):
	_immutable_fields_ = ["tp", "vals"]
	def __init__(self, tp, vals = None):
		if (vals == None):
			vals = [].extend(tp.field_count())
		self.tp = tp
		self.vals = vals
		
	@purefunction
	def	assoc(self, sym, val):
		nvals = self.vals[:]
		nvals[tp.field_offset()] = val
		return Record(self.tp, nvals)
		
	@purefunction
	def get(self, sym):
		return self.vals[tp.field_offset()]

class ProtocolRegistry(Obj):
    def __init__(self):
        self.registry = AppendDictObj({})
    def register(self, name, protocol):
        self.registry.assoc(name, protocol)
    def get(self, name):
        return self.registry.get(name)
    
    
_protocols = ProtocolRegistry()

class Protocol(Obj)
    def __init__(self, name, fns):
        self.name = name
        self.fns = fns
        _protocols.register(name, self)
		
def gen_type(name, args):
	fields = []
	for x in range(len(args)):
		fields.append(Symbol.intern(args[x]))
	return Type(Symbol.intern(name), fields)
	

def with_meta(obj, m):
    return obj.assoc(sym("meta"), m)

def list_conj(lst, itm):
    return     
		
list_type = gen_type("PersistentList", 
                     ["count", "first", "rest"]
                     {sym("cons"), )

def list_node(
