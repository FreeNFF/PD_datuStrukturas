import csv

with open("dati.csv",encoding="utf-8") as file:
    csv1 = csv.reader(file)
    saraksts = list(csv1)



print("Izdruka: ")
print(saraksts)

print()
print("---------------------------------------------------------------")
print()
print("Masīva garums: ",len(saraksts))

print()
print("---------------------------------------------------------------")
print()
pedejie3 = saraksts[-4:-1]
print("Pēdējās 3 rindiņas:\n",pedejie3)

def Nosaukums():
    print('Faila nosaukums: ',file.name)

Nosaukums()

def Pirmais():
    pirmais = saraksts[1]
    print("Pirmā rindiņa:\n",pirmais)
Pirmais()