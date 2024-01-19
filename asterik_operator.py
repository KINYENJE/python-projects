# the * operator can be used to grab excess items in a list or tuple

def func():
  a, *b, c = ["car", "bike", "scooter", "bus", "train", "plane"]
  item = b
  print(item) # ['bike', 'scooter', 'bus', 'train']
  return ("car" or "bus") in item 

print(func())


