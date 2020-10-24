from usuarios import acciones
acciones_de_usuario = acciones.Acciones()

print("""
-----------------Acciones disponobles-----------------
-            ----registro                            -
-            ----login                               -
------------------------------------------------------             
""")

accion = input("Escriba la opcion que quiere:\n")

if accion == "registro":
    acciones_de_usuario.registro()
    
elif accion == "login":
    acciones_de_usuario.login()
    