class myclass():
    def __init__(self, name:str,age:int):
        self.name=name
        self.age=age
    def out(self,vec):
        print(vec)

item=myclass("sai",24)
item.out(56)