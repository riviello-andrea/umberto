#creo una lista
thislist = ["apple", "banana", "cherry"]
print(thislist)

#uso len() per determinare il numero di oggetti nella lista
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#stampo il secondo oggetto di una lista
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#uso i numeri negativi per contare partendo dall'ultimo oggetto della lista
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#stampo un range di oggetti
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#stampo tutti gli elementi della lista tranne uno
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#stampo un range di valori che va da uno scelto all'ultimo
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#controllo se un oggetto è presente nella lista
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
