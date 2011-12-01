import inspect
from clojure.lang.symbol import sym

class CodeGeneratorBackend:
	def begin(self, tab="\t"):
		self.code = []
		self.tab = tab
		self.level = 0
	def end(self):
		return "".join(self.code)
	def writeln(self, string):
		return self.write(string+"\n")
	def write(self, string):
		self.code.append(self.tab * self.level + string)
	def indent(self):
		self.level = self.level + 1
	def dedent(self):
		import sys
		if self.level == 0:
			raise SyntaxError, "internal error in code generator"
		self.level = self.level - 1

def get_arglist(argc, prefix):
	if prefix == None:
		arglist = []
	else:
		arglist = [prefix]
		
	for x in range(argc):
		arglist.append("arg"+str(x))
	return "(" + ", ".join(arglist) +")"	

def get_invokedef(argc):		
	return "def invoke" + str(argc)+get_arglist(argc, "self") + ":"

ccount = 0

def wrapfn(name, fn):
	global ccount
	ccount = ccount + 1
	sm = sym(name)
	cg = CodeGeneratorBackend()
	cg.begin()
	cg.writeln("from clojure.lang.afn import AFn")
	cg.writeln("class _WrapClass_" + str(ccount) + "(AFn):")
	cg.indent()
	argc = len(inspect.getargspec(fn))
	cg.writeln(get_invokedef(argc))
	cg.indent()
	cg.writeln(fn.__name__ + get_arglist(argc, None))
	cg.dedent()
	cg.dedent()
	cg.writeln("Var(Symbol.from_string(\""+name+"\"), _WrapClass_"+str(ccount)+"())")
	return cg.end()
