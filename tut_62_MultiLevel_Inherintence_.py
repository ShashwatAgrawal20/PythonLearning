# ye bhot imp hai ye bhi kam me aata hai aage chal ke ye kam me aata hai jo multilevel Inheritence hoti hai jo ye aache se preparre kr na hai ye kam me aati hai .. piche ka sb agr yad nhi aaye to revise mar aache se

class Dad:
    football = 10
class Son(Dad):
    dance = 34
    Computer = 11

    def iscomputer(self):
        return f"The number of computer we have {self.Computer}"


class Grandson(Son):
    Computer = 1
    
    def iscomputer(self):
        return f"Ham garib hai hamare pass ek hi hai  {self.Computer}"

lala = Dad()
hagra = Son()
gandu = Grandson()
print(gandu.iscomputer())
# print(Son.iscomputer())
print(hagra.iscomputer())