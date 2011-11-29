


class Type(Obj):
	_immutable_fields_ = ["fields", "name"]
	def __init__(self, name, fields):
		fields.append(Symbol.intern("meta"))
		self.fields = fields
		self.name = name
		
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
		
def gen_type(name, args):
	fields = []
	for x in range(len(args)):
		fields.append(Symbol.intern(args[x]))
	return Type(Symbol.intern(name), fields)		
		
list_type = gen_type("PersistentList", ["count", "first", "rest"])

def list_node(
