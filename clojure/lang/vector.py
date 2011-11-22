from primitives import Obj


class VectorNode(Obj):
   def __init__(self, items = None, children = None):
       self.items = items
       self.children = children
       
       
   def __getitem__(self, idx):
       if idx <= 31:
           return self.items[idx]
       newidx = idx >> 5
       return self.children[idx & 31][newidx]
   
   def set_item(self, idx, obj):
       if idx <= 31:
           if self.items is None:
               newitems = [None] * 32
           else:
               newitems = self.items[:]
           newitems[idx] = obj
           return VectorNode(newitems, self.children)
       
       newidx = idx >> 5
       if self.children is None:
           newchildren = [None] * 32
       else:
           newchildren = self.children[:]
       
       if newchildren[idx & 31] is None:
           newchildren[idx & 31] = VectorNode()

       newchildren[idx & 31] = newchildren[idx & 31].set_item(newidx, obj)
           
       return VectorNode(self.items, newchildren)
       
class Vector(Obj):
   def __init__(self, head, count):
       self.head = head
       self.count = count
   
   def __getitem__(self, idx):
       if idx < 0 or idx > self.count:
           raise Exception("Index out of range")
       return self.head[idx]
   
   def __repr__(self):
       s = []
       for x in range(self.count):
           s.append(str(self[x]))
       return "["+" ".join(s)+"]"
       
   def set_item(self, idx, obj):
       return Vector(self.head.set_item(idx, obj), self.count)
   
   @staticmethod
   def from_list(lst):
       vec = Vector()
       for x in range(len(lst)):
           vec = vec.cons(lst[x])
       return vec
   
   def cons(self, obj):
       if self.head is None:
           return Vector(VectorNode(None, None).set_item(0, obj), 1)
       return Vector(self.head.set_item(self.count, obj), self.count + 1)
