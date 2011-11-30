import sys
sys.path.append('/home/tim/pypy')

from clojure.lang.lispreader import LispReader, LookAheadReader
from clojure.lang.builtins import *
from clojure.lang.math import *

from pypy.rlib.streamio import open_file_as_stream

def jitpolicy(driver):
    from pypy.jit.codewriter.policy import JitPolicy
    return JitPolicy()

def entry_point(argv):
	if len(argv) == 2:
		print "running" , argv[1]
		code = open_file_as_stream(argv[1]).readall()
		
		rdr = LookAheadReader(code)
		lisp = LispReader()
		ev = None
		while True:
			
			term = lisp.read_term(rdr)
		
		
			if term is None:
				break
			
			ev = term.evaluate()
			
		try:
			#print ev.int_value()
			pass
		except Exception:
			pass
	return 0


# _____ Define and setup target ___

def target(driver, args):
    driver.exe_name = 'pypy-clj-%(backend)s'
    return entry_point, None

if __name__ == '__main__':
    entry_point(sys.argv)
