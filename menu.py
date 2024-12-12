def main():

    print("MENU CALCULADORA");

def mostrar_menu():

    print("1. Suma");
    print("2. Resta");
    print("3. Division");
    print("4. Multipplicacion");
    print("0. SALIR")

    
    mostrar_menu()

        opcion = input("Ingresa el número de la operación que deseas realizar: ")
        
        if opcion == '0':
            print("Saliendo del programa...")
            break
        
        if opcion in ['1', '2', '3', '4']:
            try:
                a = float(input("Ingresa el primer número: "))
                b = float(input("Ingresa el segundo número: "))
                
            except ValueError:
                print("Por favor ingresa números válidos.")
                continue