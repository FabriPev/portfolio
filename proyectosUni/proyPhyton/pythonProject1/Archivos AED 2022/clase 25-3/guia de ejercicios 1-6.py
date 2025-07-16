# Actividad N6

# Un vehículo parte de la ciudad de Córdoba y se dirige a Rosario por autopista.
# La distancia aproximada entre ambas ciudades es de 400 kilómetros.
# El vehículo se desplaza con velocidad promedio de 122 km/h.
# Desarrolle un programa que calcule el tiempo total en horas que demorará ese vehículo en llegar a Rosario.
# De nuevo, no es necesario convertir a horas, minutos y segundos:
# exprese en resultado como un número real, tal cual lo haya obtenido del cálculo.


print("Calculo de tiempo")

# El cálculo de posicion en mru es x=x0+v+t, nuestro x0 = 0 por lo que no se lo tiene en cuenta

velocidad = 122
distancia = 400

tiempo = distancia/velocidad

print("A 122km/h te tomaría", tiempo, "horas en llegara Rosario desde Córdoba")

