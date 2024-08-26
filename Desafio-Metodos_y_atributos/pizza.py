from ingredientes import proteicos, vegetales, masas

class Pizza:
    """
    Representa una pizza con la capacidad de elegir ingredientes y verificar si el pedido es válido.

    Atributos de clase:
    - precio (int): Precio base de la pizza.
    - tamaño (str): Tamaño estándar de la pizza.

    Atributos de instancia:
    - ingrediente_proteico (str): Ingrediente proteico seleccionado para la pizza.
    - ingrediente_vegetal_1 (str): Primer ingrediente vegetal seleccionado para la pizza.
    - ingrediente_vegetal_2 (str): Segundo ingrediente vegetal seleccionado para la pizza.
    - tipo_masa (str): Tipo de masa seleccionado para la pizza.
    - es_valida (bool): Indica si el pedido de la pizza es válido.
    """

    # Atributos de clase
    precio = 10000
    tamaño = "familiar"

    def __init__(self):
        """
        Inicializa una nueva instancia de la clase Pizza con valores por defecto.
        """
        self.ingrediente_proteico = None
        self.ingrediente_vegetal_1 = None
        self.ingrediente_vegetal_2 = None
        self.tipo_masa = None
        self.es_valida = False

    @staticmethod
    def validar_ingrediente(ingrediente, lista_ingredientes):
        """
        Valida si un ingrediente dado está presente en una lista de ingredientes permitidos.

        Args:
        - ingrediente (str): El ingrediente a validar.
        - lista_ingredientes (list): Lista de ingredientes permitidos.

        Returns:
        - bool: True si el ingrediente está en la lista, False en caso contrario.
        """
        return ingrediente in lista_ingredientes

    def realizar_pedido(self):
        """
        Realiza un pedido de pizza solicitando los ingredientes y el tipo de masa al usuario.

        Este método también valida los ingredientes seleccionados y determina si la pizza es válida.
        """
        self.ingrediente_proteico = input("Ingrese el ingrediente proteico: ")
        self.ingrediente_vegetal_1 = input("Ingrese el primer ingrediente vegetal: ")
        self.ingrediente_vegetal_2 = input("Ingrese el segundo ingrediente vegetal: ")
        self.tipo_masa = input("Ingrese el tipo de masa: ")

        # Validación de ingredientes
        if (self.validar_ingrediente(self.ingrediente_proteico, proteicos) and
                self.validar_ingrediente(self.ingrediente_vegetal_1, vegetales) and
                self.validar_ingrediente(self.ingrediente_vegetal_2, vegetales) and
                self.validar_ingrediente(self.tipo_masa, masas)):
            self.es_valida = True
        else:
            self.es_valida = False
