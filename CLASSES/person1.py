class person:
    def __init__ (self,_name,_age):
        self.name = _name
        self.age = _age
    def sayhi(self):
        print('hello my name is' + str(self.name) +'i am'+ str(self.age) +  'years old')
person1 = person('bob',16)        
person1.sayhi()
person2 = person ("james",24)
person2.sayhi()

