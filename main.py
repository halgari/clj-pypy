from clojure.lang.lispreader import LispReader, LookAheadReader
from clojure.lang.builtins import *
from clojure.lang.math import *

f = open("scratch-space.clj").read()
rdr = LookAheadReader(f)
lisp = LispReader()

while True:
	term = lisp.read_term(rdr)


	if term is None:
		break
	
	ev = term.evaluate()
	
	print ev
