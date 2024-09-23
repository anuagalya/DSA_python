class stack_class():
  def __init__(self):
    self.stack = []
    self.limit = 5
  def isfull(self):
    if(len(self.stack))==self.limit:
      k=True
    else:
      k=False
    return k
  def isempty(self):
    if(len(self.stack))==0:
      k=True
    else:
      k=False
    return k
  def push(self, item):
    full = self.isfull()
    if full != True:
      self.stack.append(item)
    else:
      print("stack is full")
  def pop(self):
    empty = self.isempty()
    if empty != True:
      self.stack.pop()
    else:
      print("stack is empty")
obj = stack_class()
obj.push( str(1))
obj.push( str(2))
obj.push( str(3))
obj.push( str(4))
obj.push( str(5))
obj.push( str(6))
print(obj.stack)
obj.pop()
obj.pop()
obj.pop()
obj.pop()
obj.pop()
obj.pop()
print(obj.stack)
