class plant:
 def type(self):
  print("small plant")

class flower:
 def kind(self):
  print("sunflower")

class purchaser(plant,flower):
 def by(self):
  print("Buy flower as well as plant")
obj = purchaser()
obj.type()
obj.kind()
obj.by()