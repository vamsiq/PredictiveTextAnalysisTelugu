
class Krishna:
    name=''
    def __init__(self,u):
        self.name=u


    def hello(self):
        print("oh dear"+self.name)

class Rama:
    k=0
    def __init__(self,k):
        self.k=k
        k=Krishna("ramakrishna")
        k.hello()



    def rama(self):
        print("rama")



#here it calls

r1=Rama(56)
print(r1.k)
r1.rama()

