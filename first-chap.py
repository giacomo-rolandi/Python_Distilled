#Primo Capitolo del libro

x = 7

y = 4

"""
Stampa di valore assoluto, div/mod, potenza, approsimazione

print(abs(-(x/y)))
print(divmod(x,y))
print(pow(x, 2, 7))
print(round(x/y))


"""





"""
Nel primo caso stampa la stringa con le varie funzioni, nel secondo così com'è scritto
N.B. Per selezionare più righe premere SHIFT, Per spostarle ALT, e per ricopiarle su o giù SHIFT+ALT

print(str("\n \n \n"))
print(repr("\n \n \n"))

"""

n1 = 9
n2 = -23



"""
Stampa binario

print(bin(n2))
print(" " + bin(n1))
print(bin(~n1))
print(~n1)

"""




"""
While con la funzione continue

x = 10

while x < 11:
    x += 1
    if x == 11:
        print("dentro")
        continue
    print("ciao")

print("fatto")

"""




"""
Rimozione/scambio lettere in una stringa

a= "Hello World "

print(a.strip("ld ") + "c")

"""




"""


Apre un file e stampa riga per riga 



with open (r"/home/jackzzzr/Desktop/Python/P-Dist/prova.txt") as file:
    for line in file:
        print (line, end="")
                     Di base con end impostato a \n


"""

"""

Variante senza with


file = open ("./prova.txt")

for line in file:
    print(line, end="")
file.close()


"""

"""

"""

