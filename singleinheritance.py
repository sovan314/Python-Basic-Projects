class one:
    def func1(self):
        print("one class")

class two(one):
 def func2(self):
  print("two class")

obj=two()
obj.func1()
obj.func2()