import notas.nota as modelo
class Acciones:
    def crear(self, usuario):
        print(f"ok, {usuario[1]} crearemos una nora ")
        titulo=input("Ingresa el contenido de tu nota")
        descripcion = input("ingresa el contenido de tu nota")
        nota =modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0]>=1:
            print(f"{nota.titulo} ha sido guardada ")
        else:
            print(f" lo sentimos {usuario[1]} hubo un error al gurdar tu nota")

    def mostrar(self, usuario):
        print(f"Muy bien {usuario[1]} aqui estan tus cosas")
        nota = modelo.Nota(usuario[0], "", "")
        notas = nota.traerTodas()    

        print(notas)
        for e in notas:
                print(f"-----------------------Nota numero {e[0]}--------------------")
                print(" ____________________________________________________")
                print(f" ID: {e[0]}  -  ID usuario: {e[1]}  -  fecha: {e[4]}")
                print(" ____________________________________________________")
                print(f"-                -{e[2]}                     ")
                print(" ____________________________________________________")
                print(f"-  {e[3]}")
                print(" ____________________________________________________")

    def borrar(self, usuario):
        print(f"ok {usuario[1]} vamos a borrar una nota")
        titulo = input("ingrese el titulo de la nota que quiere eliminar")
        nota = modelo.Nota(usuario[0], titulo, "")

        eliminar=nota.eliminar()
        if eliminar[0]>=1:
            print(f"{nota.titulo} ha sido eliminada")
        else:
            print("error al eliminar la nota")
        

                
