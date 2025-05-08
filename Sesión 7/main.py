# Escribe esta linea de código
print("Bienvenido al entrenamiento con Python, vamos a disfrutar al máximo esta sesión")

"""
   descuento en una compra: 
   si compras mas de $1000, obtienes un descuento del 20%
   pide el monto de la compra y muestra el precio final 
"""

# Pedir datos por teclado al usuario int (entero) float (decimales) str (cadenas de caracteres) bool (booleano unos o ceros)

compra = float(input("Digite el valor de la compra: "))

# Si compra mas de $1000, obtienes un descuento del 20%
# Siempre que la salida tenga mas de un camino de resolución, debo implementar condicionales.
# Operadores combinados.
# Operadores de asignación =, operadores aritmeticos + - /, operadores lógicos and y, or o, not 
# Operadores de comparación ==, !=, >, <, >=, <=

if compra > 1000: 
   descuento = compra * 0.2
   compra -= descuento 
   # Compra = compra - descuento
   print(f"El descuento es de {descuento}, por lo tanto su valor a pagar es: {compra}")