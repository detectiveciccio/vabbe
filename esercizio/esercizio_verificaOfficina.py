#Crea un programma in Python basato sulla flowchart della verifica scorso.

print("L'auto arriva in officina")
print("Controllo danni")
danni = input("inserisci il tipo di danno: ")
if danni == "lieve":
    print("i danni possono essere: \n abrasione \n graffio \n ammacatura \n altri")
else:
    if danni == "gravi":
        print("i danni possono essere: \n cofano anteriore \n motore \n parabrezza \n altri")
print("....stima dei danni....")
print("l'auto sta venendo riparata! ")
pagamento = input("chi pagherà i danni? ")
if pagamento == "assicurazione":
    print("l'assicurazione pagherà i danni ")
else:
    if pagamento == "cliente":
        print("il cliente pagherà i danni ")
        print("l'AUTO è STATA RIPARATA CON SUCCESSO!!")

        
