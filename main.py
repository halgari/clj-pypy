from clojure.lang.lispreader import LispReader, LookAheadReader
from clojure.lang.math import *

rdr = LookAheadReader("(+ 1 2)")
lisp = LispReader()

term = lisp.read_term(rdr)

print term

ev = term.evaluate()

print ev
