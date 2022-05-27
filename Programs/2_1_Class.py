
class father():
    def __init__(self,name):
        self.fname=name
    def println(self):
        print(f"Father name  is {self.fname}")

class child(father):
    def __init__(self,name):
        super().__init__(name)
        super().println()

c1 = child("Pradip")
