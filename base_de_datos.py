bienvenida = input("""Hola binvenido a la base de datos, quieres crear tu primera base de datos?
Si es asi presiona "SI" para comenzar: """)

res = "SI"

if bienvenida == res:
    nombre = input("Para empezar a crear tu primera base de datos digite su nombre: ")

    print("Hola", nombre, """ estamos satisfechos de que estes aqui, bienvenido a nuestra base de datos,
    esperamos que la disfrutes mucho, GRACIAS!!! \n""")

    print("""

=======================
>>>>>BASE DE DATOS<<<<<
=======================
created by: HL15


                EN MANTENIMIENTO
                """)
   

    print("Nuestra BASE DE DATOS tiene las siguientes opciones disponibles \n")
    print("=== MUJER ===")
    print("=== HOMBRE ===")
    print("=== ALTURA ===")
    print("=== NOMBRE ===")
    print("=== HOGAR ===")
    print("=== EDAD ===")
    print("=== OBESO ===")
    print("=== FLACO === \n")
    
    nombres = input("Para empezar como se llama la persona? : ")
    personalidad = input("La persona es hombre o mujer? : ")
    altura = input("La persona cuanto mide exactamente? : ")
    hogar = input("Donde vive la persona? : ")
    edad = input("Cuantos años tiene la persona? : ")
    cuerpo = input("La persona es obesa o flaca? : ")

    print("===", nombres, "===")
    print("===", personalidad, "===")
    print("===", altura, "===")
    print("===", hogar, "===")
    print("===", edad, "===")
    print("===", cuerpo, "=== \n")
    fin = input("Los DATOS imprimidos en pantalla son correctos? (SI/NO) :")
    print("Muchas gracias", nombre, """por usar nuestra base de datos te esperamos en el
futuro con mas actualizaciones""")
    
else:
    print("""No has escrito "SI" en mayusculas""")
   
 

