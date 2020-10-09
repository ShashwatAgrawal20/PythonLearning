import pickle


# pickleing means koi chiz ko preserve kr na !!!!!!!!!! ye sadhe pickle ka hota hai .. 

# cars = ["Audi", "BMW", "MarutiSuzuki", "RollsRoyals", "Tata", "Jaguar", "Bugati"]
# file = "mycar.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(cars, fileobj)
# fileobj.close()

# koi object ko depickle kaise kre

file = "mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))


pickle.loads()