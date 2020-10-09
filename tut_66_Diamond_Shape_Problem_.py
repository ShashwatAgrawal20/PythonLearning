# Diamond Shape Problem is noting but a Confusion That is Created using the multiple inherithece..iss me smj me nhi aata hai jaldi ki ye kha se aa rha hai.. ye jo hai ye python me to easy hai mgr aur programming languages mai bhot hard ho jata hai..iss lye kuch kuch-kuch languages support hi nhi kr ti hai iss ke lye iss lye single inheritance use kr na hai nhi to multilevel inheritance use krna hona chiyea.. 

class A:
    def met(self):
        print("I am a Variable form class A")
class B(A):
    def met(self):
        print("I am a Variable form class B")
class C(A):
    def met(self):
        print("I am a Variable form class C")
class D(B, C):
    def met(self):
        print("I am a Variable form class D")


a = A()
b = B()
c = C()
d = D()

a.met()
b.met()
c.met()
d.met()