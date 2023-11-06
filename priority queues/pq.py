class PriorityQueue:
  # abstract base class for priority queue
  class Item:
    __slots__ = '_key', '_value'

    def __init__(self, k, v):
      self._key = k
      self._value = v

    def __lt__(self, other):
      return self._key < other._key
    
    
  def is_empty(self):
    return len(self) == 0
  
  # def __len__(self):
  #   raise NotImplementedError('must be implemented by subclass')
  

x = PriorityQueue()

item1 = x.Item(1, 2)
item2 = x.Item(1, 3)
item3 = x.Item(1, 2)
print(item1 < item3)
print(item2)
