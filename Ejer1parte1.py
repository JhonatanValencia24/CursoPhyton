# con la funcion printf, imprimo los textos de encabezado
# y los literales de las preguntas
print('Empezando a trabajar con Python') 
print('Realizado por:"Jhonatan Valencia"')
print('Consultando los tipos de valores:')
print("El tipo de dato 875 es:")
#la funcion type(),identifica el tipo de dato que ingresamos dentro del parentesis
# para que imprima el resultado de la funcion type, la anidamos con la funcion print
print(type(875))
print('El tipo de dato de 4.89 es:')
print(type(4.89))
print('El tipo de dato del texto: Now is better than never. es:')
print(type('Now is better than never.'))
print('El tipo de dato de 1.32 es:')
print(type(1.32))
print('¿El valor 5 + 8i corresponde a un valor entero?')
#la funcion isinstance(), realiza una comparacion entre el valor y tipo de dato que ingresemos en le parentesis
# y devuelve un verdadero o falso de ser el caso, para mostrar el resultado la anidamos con la funcion print
print(isinstance(5+8j, int))
print('¿El valor 8.2 corresponde a un valor entero?')
print(isinstance(8.2, int))
print('¿El texto: Readability counts. corresponde a un string?')
print(isinstance('Readability counts.', str))