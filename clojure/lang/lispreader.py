from clojure.lang.primitives import IntObj, Obj, StrObj, FloatObj
from clojure.lang.symbol import Symbol
from clojure.lang.list import List

_numbers = "1234567890"
_whitespace = " \t\n\r"


class LookAheadReader:
   """description of class"""
   def __init__(self, data):
       self.data = data
       self.head = 0
       
   def next(self):
       self.head += 1
       
   def peek(self):
       return self.data[self.head + 1]
   
   def has_more(self):
       return self.head < len(self.data)
   
   def current(self):
       return self.data[self.head]

class LispReader:
   """Reads Lisp Items"""
   
   def read_char(self, reader):
       """Reads a single character"""
       s = reader.current()
       if (s == '\\'):
           reader.next()
           return reader.current()
       return s

   def read_string(self, reader, endquote):
       reader.next()
       chars = []
       while reader.current() != '"':
           chars.append(reader.current())
           reader.next()
       return StrObj("".join(chars))
   
   @staticmethod
   def is_number(chr):
       return chr in _numbers
   
   @staticmethod
   def is_whitespace(chr):
       return 
   
   def read_number(self, reader):
       chars = []
       while self.is_number(reader.current()) or \
             reader.current() == '.' or \
             reader.current() == '-':
             chars.append(reader.current())
             reader.next()
       str = "".join(chars)
       if str == "-":
           return Symbol.from_string(str)
       if '.' in str:
           return FloatObj(float(str))
       return IntObj(int(str))
   
   def read_term(self, reader):
       if not reader.has_more():
           return None
       
       while reader.current() in _whitespace:
           reader.next()
           if not reader.has_more():
               return None
       
       cur = reader.current()
       
       if cur == '"':
           return self.read_string(reader, '"')
       
       if self.is_number(cur) or cur == '-':
           return self.read_number(reader)
       
       if cur == '(':
           return self.read_list('(', reader, ')')
       
       if cur == ')':
           return StrObj(cur)
       
       chrs = []
       
       
       while (not reader.current() in _whitespace) \
                 and (reader.current() != ')') \
                 and (reader.current() != '(') \
                 and reader.has_more():
           chrs.append(reader.current())
           reader.next()
       sym = "".join(chrs)
       
       #if sym.strip(_whitespace) == "":
       #    return None
       
       return Symbol.intern(StrObj(sym))
   
   def read_list(self, start, reader, end):
       lst = []
       reader.next()
       while True:
           term = self.read_term(reader)
           if term is None:
               raise Exception("EOF wile reading list")
           if isinstance(term, StrObj) and term.str_value() == ")":
               reader.next();
               return List.from_list(lst)
           lst.append(term)
       
	
