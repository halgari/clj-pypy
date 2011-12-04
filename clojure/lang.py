"""
Clojure-PyPy
---

The purpose of this document is to provide a semi-literate approach
to documenting the source of Clojure-PyPy

"""



class Obj(object):
    """
    Every object in a RPython program must inherit from the same class.
    this allows RPython to understand what boxed and unboxed types are.
    So let's start be defining an abstract boxed type.
    """
    def __init__(self):
        pass

    def typedef(self):
        """
        This method should be overridden by all children and return the typedef
        that defines that type
        """
        raise Exception(sym("AbstractMethodCall"))



"""
To start with, we should begin by explaining how the type system works.
There are three python classes that will define the majority of the
type system.

The first of these is the TypeDef.
"""

class TypeDef(Obj):
    """
    The typedef will contain a name
    and a list of fields. We provide methods for retreiving the index of
    certain fields. We will mark the fields as immutable. This will allow
    for easy retreival of the field indexes. We will extend the fields
    to also support metadata.
    """
    def __init__(self, name, fields=None):
        """
        Defines a new type named by the given symbol and with the specified
        fields.
        """
        Obj.__init__(self)
        if fields is None:
           fields = []
        fields.extend("meta")
        self.name = name
        self.fields = fields

    def __repr__(self):
        return "TypeDef<" + self.name + ">"

    def field_index(self, name):
        """
        Returns the index of a field a unboxed type. Expects a
        symbol
        """
        for x in range(len(self.fields)):
            if self.fields[x] == name:
                return x
        raise Exception("Field not found")

    def field_count(self):
        """
        Returns the number of fields in this type
        """
        return len(self.fields)

    def typedef(self):
        """
        Can't call typedef() on a type
        """
        raise Exception(sym("TypeOfTypeCall"))


class Type(Obj):
    """
    We need a simple way to create immutable types. This class will we will call
    Type. We will store the contents of the type in a array for easy access
    """
    _immutable_fields_ = ["fields", "data"]

    def __init__(self, type_def, data=None):
        if data is None:
            data = [].extend(typedef.field_count())
        self.type_def = type_def
        self.data = data

    def    assoc(self, field, val):
        """
        Creates a new Type that inherits all the same data with a single
        field replaced
        """
        new_data = self.vals[:]
        new_data[self.type_def.field_offset(field)] = val
        return Type(self.type_def, new_data)

    def get(self, field):
        """
        Gets the value of a given field
        """
        return self.vals[self.type_def.field_offset()]

    def typedef(self):
        return self.typedef


"""
One of the core types in Clojure is the symbol. Unlike Clojure we will
intern all symbols. We will put these symbols into a dict for later
retreival.
"""

_interned_symbols_ = {}

class Symbol(Obj):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def name(self):
        return self.name

def sym(name):
    """
    Define a symbol with the given @name. If a symbol with this name already exists, the
    previously created symbol will be returned.
    """
    s = intern(name)
    if s not in _interned_symbols_:
        _interned_symbols_[name] = Symbol(name)
    return _interned_symbols_[name]

Symbol._type = TypeDef(sym("Symbol"), [sym("name")])

class Nil(Obj):
    """
    Several of the following classes and functions will need the nil value. Here we are actually
    defining a nil type so that we can use it in polymorphic dispatches. That is, we want to
    override the behavior of certain functions if they are passed a Nil
    """
    _type = TypeDef("Nil")
    def __init__(self):
        Obj.__init__(self)
        pass
    def typedef(self):
        return Nil._type

nil = Nil()



"""
Next we will begin by creating boxed types for most prmitives. These types
will inherit from Obj.
"""

class Bool(Obj):
    def __init__(self, value):
        self._bool_value = value

    def bool_value(self):
        return self._bool_value


class Integer(Obj):
    def __init__(self, value):
        self._int_value = value

    def integer_value(self):
        return self._int_value


class String(Obj):
    def __init__(self, value):
        self._string_value = value

    def string_value(self):
        return self._string_value

"""
Next let's define a few helper 'constants'
"""

false = Bool(False)
true = Bool(True)

"""
The next building block of any Clojure system is a function. First of all, we need a
few helpers for creating code on-the-fly.
"""

class CodeGenerator:
    def __init__(self, tab="\t"):
        self.code = []
        self.tab = tab
        self.level = 0

    def end(self):
        return "".join(self.code)

    def writeln(self, string):
        return self.write(string + "\n")

    def write(self, string):
        self.code.append(self.tab * self.level + string)

    def indent(self):
        self.level = self.level + 1

    def dedent(self):
        if self.level == 0:
            raise SyntaxError, "internal error in code generator"
        self.level = self.level - 1

    def inject(self):
        exec "".join(self.code, "")

"""
Now we will define the standard AFn class as seen in standard clojure. Basically this
is an abstract class with invoke0 through invoke20. There will also be an apply_form
function that will accept a form to be evaluated. We will also define a apply function
that will allow a ISeq to be applied to the function. We will use a few functions and
constructs that are not yet defined. But we will define these later.
"""

def get_arg_list(arg_count, prefix=None):
    """
    Returns a string containing a argument list. If prefix is non-None, then prefix
    is added at the beginning of the list. Thus get_arglist(2, 'self') returns
    '(self, arg0, arg1)'
    """
    if prefix is nil:
        arg_list = []
    else:
        arg_list = [prefix]

    for x in range(arg_count):
        arg_list.append("arg" + str(x))
    return "(" + ", ".join(arg_list) + ")"


def get_invoke_def(arg_count):
    """
    Returns a def invoke
    """
    return "def invoke" + str(arg_count) + get_arg_list(arg_count, "self") + ":"


"""
Next we will generate the actual AFn class
"""

max_args = 20


def gen_std_fn(name, evaluate, max_args = 20):
    cg = CodeGenerator()
    cg.writeln("class " + name + "(Obj):")
    cg.indent()
    cg.writeln("_type = TypeDef(sym('" + name + "'), [])")
    cg.writeln("def __init__(self):")
    cg.indent()
    cg.writeln("Obj.__init__(self)")
    cg.dedent()
    cg.writeln("def typedef(self):")
    cg.indent()
    cg.writeln("return " + name + "._type")
    cg.dedent()
    for x in range(max_args):
        cg.writeln(get_invoke_def(x))
        cg.indent()
        cg.writeln("raise Exception(sym('BadArity" + str(x) + "'))")
        cg.dedent()
    cg.writeln("def apply_form(s):")
    cg.indent()
    for carg in range(max_args):
        cg.writeln("if count(s).int_value() == " + str(carg) + ":")
        cg.indent()
        for x in range(carg):
            if evaluate:
                cg.writeln("arg" + str(x) + " = first(s).evaluate()")
            else:
                cg.writeln("arg" + str(x) + " = first(s)")
            if x != carg - 1:
                cg.writeln("s = rest(s)")
        cg.writeln("self.invoke" + str(carg) + get_arg_list(carg, "self"))
        cg.dedent()
    cg.writeln("args = []")
    cg.writeln("while s is not nil:")
    cg.indent()
    if evaluate:
        cg.writeln("args.append(first(s).evaluate())")
    else:
        cg.writeln("args.append(first(s))")

    cg.writeln("s = rest(s)")
    cg.dedent()
    cg.writeln("args.apply(Array(args))")
    cg.dedent()
    cg.writeln("def apply(s):")
    cg.indent()
    for carg in range(max_args):
        cg.writeln("if count(s).int_value() == " + str(carg) + ":")
        cg.indent()
        for x in range(carg):
            cg.writeln("arg" + str(x) + " = first(s)")
            if x != carg - 1:
                cg.writeln("s = rest(s)")
        cg.writeln("self.invoke" + str(carg) + get_arg_list(carg, "self"))
        cg.dedent()
    cg.dedent()
    cg.dedent()
    return cg.end()

"""
Now that we've generated this massive code block we will execute it. If
the above code seems a bit complex, that's because it is. Feel free to
call

print cg.end()

This will dump the code generator output and will make it a bit clearer why
we are writing code this way.
"""

exec gen_std_fn("AFn", True)

"""
Now the above code works just fine for standard functions, but builtin
functions like if, def, etc., don't require calling .evaluate() on each
and every argument. So next we will simply copy-paste the above code
with a slightly
"""

exec gen_std_fn("BuiltinFn", False)


"""
Next we will define overloaded functions. Overloaded functions dispatch
based on the number of arguments in the function call.
"""


def gen_overload(cg, argc):
    """
    creates a invoke definition for the given argument count
    """
    cg.writeln(get_invoke_def(argc))
    cg.indent()
    cg.writeln("if "+str(argc)+" in self.fns:")
    cg.indent()
    cg.writeln("AFn.invoke"+str(argc)+get_arg_list(argc, "self"))
    cg.dedent()
    cg.writeln("elif -1 in self.fns:")
    cg.indent()
    args = []
    for x in range(argc):
        args.append("arg"+str(x))
    cg.writeln("AFn.apply(self, Array(["+",".join(args)+"]))")
    cg.dedent()
    cg.writeln("else:")
    cg.indent()
    cg.writeln("raise Exception(sym('NoOverload"+str(argc)+"'))")
    cg.dedent()
    cg.dedent()


def gen_overloadfn(max_count = 20):
    cg = CodeGenerator()
    cg.writeln("class OverloadedFn(AFn):")
    cg.indent()
    cg.writeln("_immutable_fields_ = ['fns']")
    cg.writeln("def __init__(self, fns):")
    cg.indent()
    cg.writeln("self.fns = fns")
    cg.dedent()
    for x in range(max_count):
        gen_overload(cg, x)
    return cg.end()

"""
Now that we have the overloads generated, run the code.
"""
exec gen_overloadfn()

"""
Next we will define polymorphic functions. Polymorphic functions dispatch on
the type of the first argument
"""

def gen_polymorph(cg, argc):
    cg.writeln(get_invoke_def(argc))
    cg.indent()
    cg.writeln("tp = arg0.typedef()")
    cg.writeln("if tp in self.dispatches:")
    cg.indent()
    cg.writeln("return self.dispatches[tp].invoke"+str(argc)+get_arg_list(argc, nil))
    cg.dedent()
    cg.writeln("else:")
    cg.indent()
    cg.writeln("raise Exception(\"No polymorph for \" + tp.__repr__())")
    cg.dedent()
    cg.dedent()

def gen_polymorphic_fn(max_count = 20):
    cg = CodeGenerator()
    cg.writeln("class PolymorphicFn(AFn):")
    cg.indent()
    cg.writeln("def __init__(self):")
    cg.indent()
    cg.writeln("self.dispatches = {}")
    cg.dedent()
    cg.writeln("def add(self, tp, fn):")
    cg.indent()
    cg.writeln("self.dispatches[tp] = fn")
    cg.dedent()
    for x in range(1, max_count):
        gen_polymorph(cg, x)
    return cg.end()

"""
And execute it
"""

exec gen_polymorphic_fn()

"""
Vars are also critical to a Clojure system as very soon we will be defining global
functions, we should probably start defining how Vars work.
"""

class Globals(Obj):
    """
    PyPy is unhappy with changing global defines. So we will put our mutable data
    into a singleton class
    """
    def __init__(self):
        self._named = dict()
        self._frames = nil

    def push_frame(self, frame):
        """
        pushes a frame seq onto the stack
        """
        self._frames = cons(self._frames, frame)

    def pop_frame(self):
        """
        removes a frame from the stack of current frames
        """
        self._frames = rest(self._frames)

    def get_frames(self):
        return self._frames

    def get_named(self):
        return self._named

    def add_def(self, name, value):
        self._named[name] = value

_globals = Globals()

def push_frame(frame):
    _globals.push_frame(frame)

def pop_frame():
    _globals.pop_frame()

def lookup(symbol):
    _frames = _globals.get_frames()
    if _frames is not nil and not _frames.length().int_value():
        h = _frames.first()
        while h is not None:
            if h.first().k() is sym:
                return h.first().v()
            h = h.rest()
    return _globals.get_named()[symbol].value()


class Var(Obj):
    def __init__(self, name, value):
        self._name = name
        self._value = value
        _globals.get_named()[name] = self
    def value(self):
        return self._value
    def evaluate(self):
        return self._value.evaluate()


"""
Often in the definition of this program we will want to define a python function
that should also be reflected in Clojure code. It would be nice then if we had a elegant
way to wrap a python function in a AFn function. Well let's generate some code to do just
that.
"""


ccount = 0

def wrapfn(name, fn):
    global ccount
    import inspect

    ccount += 1
    sm = sym(name)
    cg = CodeGenerator()
    cg.writeln("class _WrapClass_" + str(ccount) + "(AFn):")
    cg.indent()
    cg.writeln("def __init__(self):")
    cg.indent()
    cg.writeln("AFn.__init__(self)")
    cg.dedent()
    argc = len(inspect.getargspec(fn).args)
    cg.writeln(get_invoke_def(argc))
    cg.indent()
    cg.writeln("return " + fn.__name__ + get_arg_list(argc, nil))
    cg.dedent()
    cg.dedent()
    cg.writeln("Var(sym(\""+name+"\"), _WrapClass_"+str(ccount)+"())")
    return cg.end()


class Protocol(Obj):
	def __init__(self, name, fns):
		Var(name, self)
		self.implementors = {}
	def add_implementor(self, tp):
		self.implementors[tp] = tp
	def implements(self, obj):
		if obj.type() in self.implementors:
			return true
		return false



def protocol(name, funcs):
    Protocol(sym(name), funcs)
    for x in range(len(funcs)):
        Var(sym(funcs[x]), PolymorphicFn())

def extend(polymorph, type, fn):
    poly = lookup(sym(polymorph))
    poly.add(type, fn)



protocol("ISeqable", ["seq"])
protocol("ISeq", ["first", "rest"])


def seq(obj):
    return lookup(sym("seq")).invoke1(obj)

def first(obj):
    return lookup(sym("first")).invoke1(obj)

def rest(obj):
    return lookup(sym("rest")).invoke1(obj)

class Array(Obj):
    _type = TypeDef("Array")
    def __init__(self, array):
        Obj.__init__(self)
        self.array = array
    def typedef(self):
        return Array._type

class ArraySeq(Obj):
    _type = TypeDef("ArraySeq")
    def __init__(self, array, idx):
        Obj.__init__(self)
        self.idx = idx
        self.array = array
    def typedef(self):
        return ArraySeq._type

def ArraySeq_first(arr):
    return arr.array[arr.idx]

def ArraySeq_rest(arr):
    if arr.idx + 1 >= len(arr.array):
        return nil
    return ArraySeq(arr.array, arr.idx + 1)

def Array_seq(arr):
    return ArraySeq(arr.array, 0)

x = wrapfn("array-seq", Array_seq)
exec x
exec wrapfn("first-arrayseq", ArraySeq_first)
exec wrapfn("rest-arrayseq", ArraySeq_rest)


extend("seq", Array._type, lookup(sym("array-seq")))
extend("first", ArraySeq._type, lookup(sym("first-arrayseq")))
extend("rest", ArraySeq._type, lookup(sym("rest-arrayseq")))


v = Array([1, 2, 3, 4, 5])

s = seq(v)

while s is not nil:
    print first(s)
    s = rest(s)