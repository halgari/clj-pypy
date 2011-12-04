from clojure.lang.afn_gen import AFn
class OverloadedFn(AFn):
	_immutable_fields_ = ['fns']
	def __init__(self, fns):
		self.fns = fns
	def invoke0(self):
		if 0 in self.fns:
			AFn.invoke0(self)
		elif -1 in self.fns:
			AFn.apply(self, List.from_list([]))
		else:
			raise Exception("No overload for 0")
	def invoke1(self, arg0):
		if 1 in self.fns:
			AFn.invoke1(self, arg0)
		elif -1 in self.fns:
			AFn.apply(self, List.from_list([arg0]))
		else:
			raise Exception("No overload for 1")
	def invoke2(self, arg0, arg1):
		if 2 in self.fns:
			AFn.invoke2(self, arg0, arg1)
		elif -1 in self.fns:
			AFn.apply(self, List.from_list([arg0,arg1]))
		else:
			raise Exception("No overload for 2")
	def invoke3(self, arg0, arg1, arg2):
		if 3 in self.fns:
			AFn.invoke3(self, arg0, arg1, arg2)
		elif -1 in self.fns:
			AFn.apply(self, List.from_list([arg0,arg1,arg2]))
		else:
			raise Exception("No overload for 3")
	def invoke4(self, arg0, arg1, arg2, arg3):
		if 4 in self.fns:
			AFn.invoke4(self, arg0, arg1, arg2, arg3)
		elif -1 in self.fns:
			AFn.apply(self, List.from_list([arg0,arg1,arg2,arg3]))
		else:
			raise Exception("No overload for 4")
	def invoke5(self, arg0, arg1, arg2, arg3, arg4):
		if 5 in self.fns:
			AFn.invoke5(self, arg0, arg1, arg2, arg3, arg4)
		elif -1 in self.fns:
			AFn.apply(self, List.from_list([arg0,arg1,arg2,arg3,arg4]))
		else:
			raise Exception("No overload for 5")
	def invoke6(self, arg0, arg1, arg2, arg3, arg4, arg5):
		if 6 in self.fns:
			AFn.invoke6(self, arg0, arg1, arg2, arg3, arg4, arg5)
		elif -1 in self.fns:
			AFn.apply(self, List.from_list([arg0,arg1,arg2,arg3,arg4,arg5]))
		else:
			raise Exception("No overload for 6")
	def invoke7(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6):
		if 7 in self.fns:
			AFn.invoke7(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6)
		elif -1 in self.fns:
			AFn.apply(self, List.from_list([arg0,arg1,arg2,arg3,arg4,arg5,arg6]))
		else:
			raise Exception("No overload for 7")
	def invoke8(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7):
		if 8 in self.fns:
			AFn.invoke8(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7)
		elif -1 in self.fns:
			AFn.apply(self, List.from_list([arg0,arg1,arg2,arg3,arg4,arg5,arg6,arg7]))
		else:
			raise Exception("No overload for 8")
	def invoke9(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
		if 9 in self.fns:
			AFn.invoke9(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)
		elif -1 in self.fns:
			AFn.apply(self, List.from_list([arg0,arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8]))
		else:
			raise Exception("No overload for 9")
	def invoke10(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
		if 10 in self.fns:
			AFn.invoke10(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9)
		elif -1 in self.fns:
			AFn.apply(self, List.from_list([arg0,arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9]))
		else:
			raise Exception("No overload for 10")
	def invoke11(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10):
		if 11 in self.fns:
			AFn.invoke11(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10)
		elif -1 in self.fns:
			AFn.apply(self, List.from_list([arg0,arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9,arg10]))
		else:
			raise Exception("No overload for 11")
	def invoke12(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11):
		if 12 in self.fns:
			AFn.invoke12(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11)
		elif -1 in self.fns:
			AFn.apply(self, List.from_list([arg0,arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9,arg10,arg11]))
		else:
			raise Exception("No overload for 12")
	def invoke13(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12):
		if 13 in self.fns:
			AFn.invoke13(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12)
		elif -1 in self.fns:
			AFn.apply(self, List.from_list([arg0,arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9,arg10,arg11,arg12]))
		else:
			raise Exception("No overload for 13")
	def invoke14(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13):
		if 14 in self.fns:
			AFn.invoke14(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13)
		elif -1 in self.fns:
			AFn.apply(self, List.from_list([arg0,arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9,arg10,arg11,arg12,arg13]))
		else:
			raise Exception("No overload for 14")
	def invoke15(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14):
		if 15 in self.fns:
			AFn.invoke15(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14)
		elif -1 in self.fns:
			AFn.apply(self, List.from_list([arg0,arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9,arg10,arg11,arg12,arg13,arg14]))
		else:
			raise Exception("No overload for 15")
	def invoke16(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15):
		if 16 in self.fns:
			AFn.invoke16(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15)
		elif -1 in self.fns:
			AFn.apply(self, List.from_list([arg0,arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9,arg10,arg11,arg12,arg13,arg14,arg15]))
		else:
			raise Exception("No overload for 16")
	def invoke17(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16):
		if 17 in self.fns:
			AFn.invoke17(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16)
		elif -1 in self.fns:
			AFn.apply(self, List.from_list([arg0,arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9,arg10,arg11,arg12,arg13,arg14,arg15,arg16]))
		else:
			raise Exception("No overload for 17")
	def invoke18(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17):
		if 18 in self.fns:
			AFn.invoke18(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17)
		elif -1 in self.fns:
			AFn.apply(self, List.from_list([arg0,arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9,arg10,arg11,arg12,arg13,arg14,arg15,arg16,arg17]))
		else:
			raise Exception("No overload for 18")
	def invoke19(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18):
		if 19 in self.fns:
			AFn.invoke19(self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18)
		elif -1 in self.fns:
			AFn.apply(self, List.from_list([arg0,arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9,arg10,arg11,arg12,arg13,arg14,arg15,arg16,arg17,arg18]))
		else:
			raise Exception("No overload for 19")
