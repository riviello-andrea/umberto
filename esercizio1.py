#dichiaro due variabili x e y e le stampo
x = 5
y = "John"
print(x)
print(y)

#cambio il tipo di variabile
x = 4
x = "Sally"
print(x)

#specifico il tipo di dati di una variabile con cast
x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)

#stampo il tipo di una variabile
x = 5
y = "John"
print(type(x))
print(type(y))

#usare le virgolette o gli apici è uguale
x = "John"
print(x)
x = 'John'
print(x)

#i nomi delle variabili fanno distinzione tra maiuscole e minuscole
a = 4
A = "Sally"
print(a)
print(A)

#le variabili possono essere scritte nei seguenti modi
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

#assegno valori a variabili diverse sulla stessa riga
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#assegno lo stesso valore a più variabili sulla stessa riga
x = y = z = "Lilla"
print(x)
print(y)
print(z)

#estraggo dei valori da una lista e li assegno a delle variabili
x = y = z = "Orange"
print(x)
print(y)
print(z)

#stampo più variabili con un unico comando print (con la virgola o con +)
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#il comando + tra numeri funziona come operatore matematico
x = 5
y = 10
print(x + y)

#creo una variabile fuori dalla funzione (variabile globale) e la uso in una funzione
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()

#creo una variabile dentro la funzione che ha quel valore solo dentro la funzione
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

#col comando global creo una variabile dentro la funzione che funziona anche fuori dalla funzione
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

#uso global anche per cambiare una variabile dentro una funzione che valga anche fuori dalla funzione
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)



