atzimes = {10:'izcili', 9:'teicami', 8:'ļoti labi', 7:'labi', 6:'gandrīz labi', 5:'viduvēji', 4:' gandrīz viduvēji', 3:'nesekmīgs', 2:'nesekmīgs', 1:'nesekmīgs'}

print(atzimes)

while True:
    try:
        ievade= int(input("Ievadiet skaitli no 1-10: "))
        if 1<= ievade <=10:
            break
        else:
            print('Ievadītais skaitlis nav atbilstošs nosacījumiem.')
    except ValueError:
        print("Ievadītajam skaitlim jābut veselam skaitlim.")

skaidrojums = atzimes[ievade]
print("Vārdiskais skaidrojums atzīmei ir: ",skaidrojums) 
    