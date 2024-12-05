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
