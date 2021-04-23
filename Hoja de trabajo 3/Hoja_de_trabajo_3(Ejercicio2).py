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
        for n in seccionaAFemenino:
            if n == letra22:
                print(nombre, "Es de la seccion A")
                break
        else:
            print("Es de la seccion B")
        return False

    elif letra11 == "m":
        print("Es masculino")
        for n in seccionAMasculino:
            if n == letra22:
                print(nombre, "Es de la seccion A")
                break
        else:
            print("Es de la seccion B")
        return False

    return True

Seccion(sexo,nombre)