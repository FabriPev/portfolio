class Trabajos:
    def __init__(self, num_iden, descrip, tipo, importe, personal):
        self.nume_iden = num_iden
        self.descrip = descrip
        self.tipo = tipo
        self.importe = importe
        self.personal = personal


def write(trabajo):
    print("Numero de identificacion: ", trabajo.nume_iden)
    print("Descripcion del trabajo: ", trabajo.descrip)
    print("Tipo de trabajo: ", trabajo.tipo)
    print("Costo a cobrar: ", trabajo.importe)
    print("Cantidad e personal Afectado: ", trabajo.personal)


def validar_mayor_a(cota_inf, mensaje="Ingrese un numero"):
    num = cota_inf
    while num <= cota_inf:
        num = int(input(mensaje))
        return num


def ordenar(vector):
    for i in range(len(vector) - 1):
        for j in range(i + 1, len(vector)):
            if vector.repositorio[i] == vector.repositorio[j]:
                vector[i], vector[j] = vector[j], vector[i]





def str_toproyecto(linea):
    token = linea.split("|")
    nombre_usuario = token[0]
    repositorio = token[1]
    descripcion = token[2]
    fecha_actu = token[3]
    lenguaje = token[4]
    likes = float(token[5])
    tags = token[6]
    url = token[7]
    if url == "":
        url = token[6]
    poyecto = Proyecto(nombre_usuario, repositorio, descripcion, fecha_actu, lenguaje, likes, tags, url)
    return poyecto
