import hashlib
import usuarios.coneccion as conneccion

conn = conneccion.conectar()
database = conn[0]
cursor =conn[1]

class Usuario:
    def __init__(self, nombre, apellidos, email, contrasenia):
        self.nombre=nombre
        self.apellidos=apellidos
        self.email=email
        self.contrasenia=contrasenia

    def registro(self):
        try:
            sql = "INSERT INTO usuarios VALUES(null,%s,%s,%s,%s,%s)"
            fecha="20-10-2020"

            cifrado=hashlib.sha256()
            cifrado.update(self.contrasenia.encode('utf8'))

            usuario= (self.nombre, self.apellidos, self.email,cifrado.hexdigest(), fecha)
            cursor.execute(sql, usuario)
            database.commit()

            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result

    def identificar(self):
        try:
            cifrado=hashlib.sha256()
            cifrado.update(self.contrasenia.encode('utf8'))

            sql= "SELECT * FROM usuarios WHERE email=%s AND contrasenia = %s"
            usuario = (self.email, cifrado.hexdigest())

            cursor.execute(sql, usuario)
            database.commit()

            result = cursor.fetchone()
            return result
        except:
            result = None
            return result

        