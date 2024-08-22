import math

print("SCEGLI LA FIGURA GEOMETRICA:\n")
i = (input("PREMI 1 ---> QUADRATO\nPREMI 2 ---> CERCHIO\nPREMI 3 ---> RETTANGOLO\n\n"))

print(f"\nHai scelto {i}\n")

#QUADRATO
if i == "1":
    
    print("***PERIMETRO DEL QUADRATO***")

    l = float(input("\nInserisci LATO del QUADRATO in metri: "))
    per = l * 4

    print(f"Il PERIMETRO del QUADRATO e' {per} m.\n")
    
   

#CERCHIO
elif i == "2":
    
    print("***CIRCONFERENZA DEL QUADRATO***")

    r = float(input("\nInserisci RAGGIO del CERCHIO in metri: "))
    cir = math.pi * (2 * r)

    print(f"La CIRCONFERENZA del CERCHIO e' {cir} m.\n")
    
 
#RETTANGOLO
elif i == "3":
    
    print("***AREA DEL RETTANGOLO***")   

    b = float(input("\nInserisci BASE del RETTANGOLO in metri: "))
    h = float(input("Inserisci ALTEZZA del RETTANGOLO in metri: "))
    area = b * 2 + h * 2

    print(f"L' AREA del RETTANGOLO e' {area} m.\n")
    
    
    
else : print("SCELTA NON VALIDA!")





