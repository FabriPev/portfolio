import os.path
import io


class Proyecto:
    def __init__(self, nombre_usuario, repositorio, descripcion, fecha_actu, lenguaje, likes, tags, url):
        self.nombre_usuario = nombre_usuario
        self.repositorio = repositorio
        self.descrpicion = descripcion
        self.fecha_actu = fecha_actu
        self.lenguaje = lenguaje
        self.likes = likes
        self.tags = tags
        self.url = url


def to_string(proyecto):
    sep = '-' * 121
    cadena = f'| {proyecto.nombre_usuario:<18} | {proyecto.repositorio:<23} | {proyecto.descripcion:<22} | ' \
             f'{proyecto.fecha_actualizacion:>12} | {proyecto.lenguaje:<30} | {proyecto.likes:<10} | {proyecto.tags:<20} | ' \
             f'{proyecto.url:<30} | \n{sep:<121}'
    return cadena


def encabezado():
    sep = '=' * 121
    cadena = f'| {"Nombre":^10} | {"Repositorio":^23} | {"Descripcion":^22} | {"Fecha de Actualizacion":^12} | '\
             f'{"Lenguaje":^30} | {"Likes:^10"} | {"Tags:^20"} | {"Url:^30"} | \n{sep:<121}'
    titulo = f'{sep:<121}\n|{"Listado de Proyectos":<119}|\n{sep:<121}\n{cadena:<121}'
    return titulo
