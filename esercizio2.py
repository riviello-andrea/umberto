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

#sostiusco un item della lista
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#sostituisco due oggetti in una lista
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#sostituisco un oggetto della lista con due oggetti
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#sostuisco al posto di due oggetti un oggetto solo
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#inserisco un oggetto nella lista in una posizione scelta
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) 

#inserisco alla fine della lista un oggetto
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#aggiungo gli elementi di una lista ad un'altra lista
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#rimuovo un oggetto dalla lista
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#rimuovo un oggetto dalla lista a seconda della sua posizione
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#posso usare anche
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#rimuovo l'ultimo oggetto dalla lsita
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#cancello la lista
thislist = ["apple", "banana", "cherry"]
del thislist

#svuoto la lista
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#stampo in colonna i valori di una lista
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#creo una copia della lista
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

