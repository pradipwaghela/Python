class car():
    def __init__(self,model):
        self.model=model
    
    def show(self):
        print("Model is with self",self.model)


audi=car("V1")
car.show()
