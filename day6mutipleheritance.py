class Father:
    def Father_speak():
        return"father class"
class Mother:
    def Mother_speak():
        return"Mother class"
class Kid(Father,Mother):
     def kid_speak():
        return"Im kid.Im having the properties of class father and class mother"
obj1=Kid
print(obj1.Father_speak())
print(obj1.Mother_speak())
print(obj1.kid_speak())