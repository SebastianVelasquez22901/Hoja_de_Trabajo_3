sexo = str(input("Ingrese su sexo: "))
nombre = str(input("Ingrese su nombre: "))

def Seccion(s,n):
    letra1 = s[0]
    letra2 = n[0]
    seccionaAFemenino = ["A","B","C","D","E","F","G","H","I","J","K","L","M"]
    seccionAMasculino = ["N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    letra11 = letra1.lower()
    letra22 = letra2.upper()


    if letra11 == "f":
        print("Es femenino")
        for a in seccionaAFemenino:
            if a == letra22 :
                print("Es de la seccion A")
            
            else: 
                print("Es de la seccion B")
            break 
        return False

    elif letra11 == "m":
        print("Es masculino")
        for b in seccionAMasculino:
            if b == letra22 :
                print("Es de la seccion A")
            
            else: 
                print("Es de la seccion B")
            break
        return False

    return True

Seccion(sexo,nombre)