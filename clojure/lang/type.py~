
from clojure.lang.internal_atom import InternalAtom
from clojure.lang.symbol import sym

class Type(Obj):
	_immutable_fields_ = ["fields", "name"]
	def __init__(self, name, fields, fns, protocols):
		fields.append(Symbol.intern("meta"))
		self.fields = fields
		self.name = name
		self.fns = InternalAtom(fns)
		self.protocols = InternalAtom(protocols)
	
	def extend(self, name, fn):
	    dr = self.fns.deref()
	    if name in dr:
	        raise Exception("fn " + name.__repr__() + "already implemented")
	    self.fns.set(lambda o: o[name] = fn)

    
    def extends(self, name)
        proto = self.protocols.deref()
        Type._static_extends(proto, name)
    
    @staticmethod
    @purefunction
    def _static_extends(proto, name):
        if name not in proto:
            return BoolFalse
        return BoolTrue
 
    def get_fn(self, name):
        Type._static_get_fn(name, self.fns.deref())
        
    @staticmethod
    @purefunction
    def _static_get_fn(name, fns):
        if name not in fns:
            return None
        return fns[name]

	@purefunction
	def field_count(self):
		return self.fields
		
	@purefunction
	def field_offset(self, sym):
		for x in range(len(self.fields)):
			if fields[x] == sym:
				return x
				
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
