pdw = "contra"
def Pass(CON):
    pdw1 = str(input("Ingrese su contraseña: "))
    if pdw1 == pdw: 
        print(pdw1, "y", pdw, "son iguales")
        return False
    else :
        print("No son la misma")    
    return True
Pass(pdw)



