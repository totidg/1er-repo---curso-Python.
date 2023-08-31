'''Dado el siguiente código:
Si en la función obtener_valor_valido, no usaras el método
isnumeric o isdigit, y solicitaras el ingreso del valor
de la siguiente forma:
    valor_valido = input(mensaje)
cómo reescribirías el código utilizando el mecanismo de excepciones?'''

'''def obtener_valor_valido(mensaje):
    valor_valido = input(mensaje)
    while not valor_valido.isnumeric():
        print('debe ingresar un valor numerico, reingrese valor')
        valor_valido = input(mensaje)
    return int(valor_valido)'''

#-------------------------------------------------------#
'''
Para reescribir el código utilizando el mecanismo de excepciones,
podemos usar la siguiente estructura:
En este caso, la función obtener_valor_valido() intentará convertir
el valor ingresado por el usuario a un número entero. Si la conversión
falla, se lanzará una excepción ValueError. En ese caso, la función
imprimirá un mensaje de error y solicitará al usuario que ingrese un
valor nuevamente.
Esta solución es más eficiente que la original, ya que no requiere
que la función itere repetidamente hasta que se ingrese un valor
numérico válido.
'''

def obtener_valor_valido(mensaje):
    try:
        valor_valido = int(input(mensaje))
    except Exception:
        print('debe ingresar un valor numerico, reingrese valor')
        valor_valido = input(mensaje)
        return int(valor_valido)
    return valor_valido

#-------------------Bloque Principal-------------------#
edad = obtener_valor_valido('Edad: ')
print('La edad ingresada es: ',edad)



