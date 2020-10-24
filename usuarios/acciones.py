from usuarios import usuario as modelo
import notas.acciones
class Acciones:

    def registro(self):
        print("Vamos a registrarnos\n")
        nombre= input("Escribe tu nombre\n")
        apellidos = input("Escribe tus apellidos\n")
        email= input("Escribe tu email\n")
        contrasenia = input("Escribe tu contraseña\n")

        usuario = modelo.Usuario(nombre, apellidos, email, contrasenia)
        registro = usuario.registro()
        if registro[0]>=1:
            print(registro[1].nombre)
        else:
            print("Hubo un error con tu registro")

    def login(self):
        print("-----------Login----------")
        try:
            email= input("Escribe tu email\n")
            contrasenia = input("Escribe tu contraseña\n")

            usuario = modelo.Usuario("", "", email, contrasenia)
            identificar = usuario.identificar()

            
            
        except Exception as e:
            print("")
            print(f"Su email o contraseña no son correctos por favor verifique.  {type(e).__name__}")
        
        if email == identificar[3]:
            print(f"Bienvenido {identificar[1]}")
            self.proximas_acciones(identificar)

    def proximas_acciones(self, usuario):
        print("""
        ____________________________________________
        -____________Menu de acciones______________-
        -      -Crear nota (1 o "crear")           -
        -      -Mostrar nota (2 o "mostrar")       -
        -      -Eliminar nota (3 o eliminar)       -
        -      -Salir (cualquier tecla)            -
        ____________________________________________

        """)
        accion=input("-____________¿Que quieres hacer?____________-")

        hazEl = notas.acciones.Acciones()

        if accion == "1" or accion =="crear":

            hazEl.crear(usuario)
            
            self.proximas_acciones(usuario)
        elif accion == "2" or accion =="mostrar":

            print("ok vamos a mostrar una nota")

            hazEl.mostrar(usuario)
            
            self.proximas_acciones(usuario)
        elif accion == "3" or accion == "eliminar":
            print("ok vamos a eliminar una nota")
            hazEl.mostrar(usuario)

            hazEl.borrar(usuario)

            self.proximas_acciones(usuario)
        else:
            exit()