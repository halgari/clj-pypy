from pypy.rlib.jit import JitDriver

def get_location(form):
	return form.__repr__()


jitdriver = JitDriver(greens=['form'], reds=['frames'],
	get_printable_location = get_location)


