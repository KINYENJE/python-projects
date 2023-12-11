class SortedPriorityQueue(PriorityQueueBase):
  def __init__(self):
    self._data = PositionalList()

  def __len__(self):
    return len(self._data)