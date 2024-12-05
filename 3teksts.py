file= open('Cits kosmoss.txt', encoding="utf-8")#nolasa teksta datni, utf-8 - valoda
print("\nFaila nosaukums: ",file.name,"\n\n------------------------------------------------------\n")#izdrukā faila nosaukumu
data = file.read()#pārveido tekstu uz nezināmo data
print(data,"\n\n------------------------------------------------------\n")#izdrukā visu tekstu

file= open('Cits kosmoss.txt', encoding="utf-8")#nolasa teksta datni, utf-8 - valoda
print("Simbolu skaits: ", len(data))#izdrukā simbola skaitu
words = data.split()#sadala tekstu vārdos
count_words= len(words)#vārdu skaitu pārvērš mar nezināmo
print("Vārdu skaits: ", count_words)#izdrukā vārdu skaitu

file= open('Cits kosmoss.txt', encoding="utf-8")#nolasa teksta datni, utf-8 - valoda
lines = file.readlines()#failu bnolasa līnijās, pārvērš par nezinināmo
line_count = len(lines)#izskaita līnijas
print("Teksta līnijas kopā:", line_count,"\n\n------------------------------------------------------\n")#izdrukā līnijas skaitu

file= open('Cits kosmoss.txt', encoding="utf-8")#nolasa teksta datni, utf-8 - valoda
data = file.read()#pārveido tekstu uz nezināmo data
print("Pirmie 20 simboli:",data[0:20])#tiek izdrukāti pirmie 20 simboli
print("Pirmie 1. simbols:",data[0])#tiek izdrukāti pirmais simbols
print("Pirmie 2. simbols:",data[1])#tiek izdrukāti otrais simbols

print("\n------------------------------------------------------\n")

def Cits_kosmoss():#definē funkciju
    file= open('Cits kosmoss.txt', encoding="utf-8")#nolasa teksta datni, utf-8 - valoda
    lines = file.readlines()#failu bnolasa līnijās, pārvērš par nezinināmo
    print('Pirmā rindiņa: ',lines[0])#izdrukā 1. rindiņu
Cits_kosmoss()#izdara funckiju Cirs_kosmoss