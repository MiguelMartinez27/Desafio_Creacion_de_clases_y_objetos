from pizza import Pizza

# a) Mostrar valores de los atributos de clase sin crear una instancia
print(f"Precio de la pizza: ${Pizza.precio}")
print(f"Tamaño de la pizza: {Pizza.tamaño}")
"""
Muestra los valores de los atributos de clase `precio` y `tamaño` de la clase `Pizza` sin necesidad de crear una instancia.
"""

# b) Verificar si 'salsa de tomate' está en la lista ['salsa de tomate', 'salsa bbq']
print(Pizza.validar_ingrediente("salsa de tomate", ["salsa de tomate", "salsa bbq"]))
"""
Verifica si el ingrediente 'salsa de tomate' está presente en la lista `['salsa de tomate', 'salsa bbq']` 
utilizando el método estático `validar_ingrediente` de la clase `Pizza`.
"""

# c) Crear una instancia de la clase Pizza y realizar un pedido
mi_pizza = Pizza()
mi_pizza.realizar_pedido()
"""
Crea una instancia de la clase `Pizza` llamada `mi_pizza` y ejecuta el método `realizar_pedido`, 
permitiendo al usuario seleccionar ingredientes y tipo de masa para la pizza.
"""

# d) Mostrar los ingredientes y tipo de masa, y si la pizza es válida o no
print(f"Ingredientes vegetales: {mi_pizza.ingrediente_vegetal_1}, {mi_pizza.ingrediente_vegetal_2}")
print(f"Ingrediente proteico: {mi_pizza.ingrediente_proteico}")
print(f"Tipo de masa: {mi_pizza.tipo_masa}")
print("¿La pizza es válida?:", mi_pizza.es_valida)
"""
Muestra los ingredientes vegetales, el ingrediente proteico, el tipo de masa seleccionados, y 
verifica si la pizza es válida o no.
"""

# e) Intentar acceder a la validez de la pizza desde la clase (esto debería generar un error)
print(Pizza.es_valida)
"""
Intenta acceder al atributo de instancia `es_valida` desde la clase `Pizza`, lo que debería generar un error, 
ya que `es_valida` es un atributo de instancia y no de clase.
"""
