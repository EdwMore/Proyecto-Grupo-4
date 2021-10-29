import db
from werkzeug.security import generate_password_hash, check_password_hash

class usuario():
    nombre = ''
    usuario = ''
    correo = ''
    password = ''

    def __init__(self, p_nombre, p_usuario, p_correo, p_password):
        self.nombre = p_nombre
        self.usuario = p_usuario
        self.correo = p_correo
        self.password = p_password

    @classmethod
    def cargar(cls, p_usuario):
        sql = "SELECT * FROM usuarios WHERE usuario = ?;"
        try:
            obj = db.select(sql, [p_usuario])

            if obj:
                if len(obj) > 0:
                    return cls(obj[0]["nombre"], obj[0]["usuario"], obj[0]["correo"], obj[0]["password"])
                
                return None
        except:
            print("Ha ocurrido un error")
            return None
    
    def insertar(self):
        sql = "INSERT INTO usuarios (usuario, nombre, correo, password) VALUES (?,?,?,?);"
        
        pwd_hashed = generate_password_hash(self.password, method="pbkdf2:sha256", salt_length=32)
        try:
            afectadas = db.insert(sql, [self.usuario, self.nombre, self.correo, pwd_hashed])
            return (afectadas > 0)
        except:
            print("Ocurrio un error: ")
            return -1
    
    def verificar(self):
        sql = "SELECT * FROM usuarios WHERE usuario = ?;"

        try:
            ob_usuario = db.select(sql, [self.usuario])
            if ob_usuario:
                if len(ob_usuario) > 0:
                    if check_password_hash(ob_usuario[0]["password"], self.password):
                        return True
        except Exception as error:
            print("Ha ocurrido un error: ")
            return False

    @staticmethod
    def eliminarUsuario(id):
        sql = "DELETE FROM usuarios WHERE id = ?;"

        try:
            delete = db.insert(sql, [id])
            print(len(delete))
            if len(delete) > 0: 
                return True
        except:
            print("Ha ocurrido un error al eliminar: ")
            return False
 
    @staticmethod
    def listadoUsuarios():
        sql = "SELECT id, nombre, usuario FROM usuarios ORDER BY id DESC;"
        return db.select(sql, None)

class Jugo():
    nombre = ''
    descripcion = ''

    def __init__(self, p_nombre, p_descripcion):
        self.nombre = p_nombre
        self.descripcion = p_descripcion
    
    @classmethod
    def cargar(cls, p_nombre):
        sql = "SELECT * FROM usuarios WHERE nombre = ?;"
        try:
            obj = db.select(sql, [p_nombre])

            if obj:
                if len(obj) > 0:
                    return cls(obj[0]["nombre"], obj[0]["descripcion"])
                
                return None
        except:
            print("Ha ocurrido un error")
            return None
    
    def insertar(self):
        sql = "INSERT INTO crearJugo (nombreJugo, descripcion) VALUES (?,?);"

        try:
            afectadas = db.insert(sql, [self.nombre, self.descripcion])
            return (afectadas > 0)
        except:
            print("Ocurrio un error: ")
            return -1
    
    @staticmethod
    def listadoJugos():
        sql = "SELECT * FROM crearJugo ORDER BY id DESC;"
        return db.select(sql, None)