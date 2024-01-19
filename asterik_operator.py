# the * operator can be used to grab excess items in a list or tuple

def func():
  a, *b, c = ["car", "bike", "scooter", "bus", "train", "plane"]
  item = b
<<<<<<< HEAD
  print(item) # ['bike', 'scooter', 'bus', 'train']
=======
  print(item)
>>>>>>> 871843f58e2e6e37710964446ad31c799f222757
  return ("car" or "bus") in item 

print(func())


