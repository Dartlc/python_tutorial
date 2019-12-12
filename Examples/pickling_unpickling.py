import pickle

a = {1: "A", 2: "B", 3: "c"}

pickle_on = open("EMP.pickle", "wb")
pickle.dump(a, pickle_on)
pickle_on.close()

pickle_off = open("EMP.pickle", "rb")
a = pickle.load(pickle_off)
print(a)

