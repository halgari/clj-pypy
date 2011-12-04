from clojure.lang.afn_gen import AFn
class PolymorphicFn(AFn):
	def __init__(self):
		self.dispatches = {}
	def add(self, tp, fn):
		self.dispatches[tp] = fn
		def invoke1(self, arg0):
			tp = arg0.type()
			if tp in self.dispatches:
				self.dispatches[tp].invoke1(arg0)
			else:
				raise Exception("No polymorph for " + tp.__repr__())
		def invoke2(self, arg0, arg1):
			tp = arg0.type()
			if tp in self.dispatches:
				self.dispatches[tp].invoke2(arg0, arg1)
			else:
				raise Exception("No polymorph for " + tp.__repr__())
		def invoke3(self, arg0, arg1, arg2):
			tp = arg0.type()
			if tp in self.dispatches:
				self.dispatches[tp].invoke3(arg0, arg1, arg2)
			else:
				raise Exception("No polymorph for " + tp.__repr__())
		def invoke4(self, arg0, arg1, arg2, arg3):
			tp = arg0.type()
			if tp in self.dispatches:
				self.dispatches[tp].invoke4(arg0, arg1, arg2, arg3)
			else:
				raise Exception("No polymorph for " + tp.__repr__())
		def invoke5(self, arg0, arg1, arg2, arg3, arg4):
			tp = arg0.type()
			if tp in self.dispatches:
				self.dispatches[tp].invoke5(arg0, arg1, arg2, arg3, arg4)
			else:
				raise Exception("No polymorph for " + tp.__repr__())
		def invoke6(self, arg0, arg1, arg2, arg3, arg4, arg5):
			tp = arg0.type()
			if tp in self.dispatches:
				self.dispatches[tp].invoke6(arg0, arg1, arg2, arg3, arg4, arg5)
			else:
				raise Exception("No polymorph for " + tp.__repr__())
		def invoke7(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6):
			tp = arg0.type()
			if tp in self.dispatches:
				self.dispatches[tp].invoke7(arg0, arg1, arg2, arg3, arg4, arg5, arg6)
			else:
				raise Exception("No polymorph for " + tp.__repr__())
		def invoke8(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7):
			tp = arg0.type()
			if tp in self.dispatches:
				self.dispatches[tp].invoke8(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7)
			else:
				raise Exception("No polymorph for " + tp.__repr__())
		def invoke9(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
			tp = arg0.type()
			if tp in self.dispatches:
				self.dispatches[tp].invoke9(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)
			else:
				raise Exception("No polymorph for " + tp.__repr__())
		def invoke10(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
			tp = arg0.type()
			if tp in self.dispatches:
				self.dispatches[tp].invoke10(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9)
			else:
				raise Exception("No polymorph for " + tp.__repr__())
		def invoke11(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10):
			tp = arg0.type()
			if tp in self.dispatches:
				self.dispatches[tp].invoke11(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10)
			else:
				raise Exception("No polymorph for " + tp.__repr__())
		def invoke12(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11):
			tp = arg0.type()
			if tp in self.dispatches:
				self.dispatches[tp].invoke12(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11)
			else:
				raise Exception("No polymorph for " + tp.__repr__())
		def invoke13(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12):
			tp = arg0.type()
			if tp in self.dispatches:
				self.dispatches[tp].invoke13(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12)
			else:
				raise Exception("No polymorph for " + tp.__repr__())
		def invoke14(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13):
			tp = arg0.type()
			if tp in self.dispatches:
				self.dispatches[tp].invoke14(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13)
			else:
				raise Exception("No polymorph for " + tp.__repr__())
		def invoke15(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14):
			tp = arg0.type()
			if tp in self.dispatches:
				self.dispatches[tp].invoke15(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14)
			else:
				raise Exception("No polymorph for " + tp.__repr__())
		def invoke16(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15):
			tp = arg0.type()
			if tp in self.dispatches:
				self.dispatches[tp].invoke16(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15)
			else:
				raise Exception("No polymorph for " + tp.__repr__())
		def invoke17(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16):
			tp = arg0.type()
			if tp in self.dispatches:
				self.dispatches[tp].invoke17(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16)
			else:
				raise Exception("No polymorph for " + tp.__repr__())
		def invoke18(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17):
			tp = arg0.type()
			if tp in self.dispatches:
				self.dispatches[tp].invoke18(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17)
			else:
				raise Exception("No polymorph for " + tp.__repr__())
		def invoke19(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18):
			tp = arg0.type()
			if tp in self.dispatches:
				self.dispatches[tp].invoke19(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18)
			else:
				raise Exception("No polymorph for " + tp.__repr__())
