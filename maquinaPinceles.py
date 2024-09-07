class MaquinaHacerPinceles:
    
    def __init__(self,tipo_pelo,cantidad_pelos,encender):
        self.tipo_pelo = tipo_pelo
        self.cantidad_cerdas = cantidad_pelos
        self.encender = encender
        self.produccion_total = 0

    # Selecion del tipo de Cerda que va en el pincel

    def seleccionar_tipo_de_pelo(self, nuevo_tipo):
        tipos_validos = ["cerdas", "nylon", "sintetico","cerda de tejon","mixto"]
        if nuevo_tipo.lower() in tipos_validos:
            self.tipo_pelo = nuevo_tipo
            print(f"Nuevo tipo de pelo: {self.tipo_pelo} agregado ")
        else:
            print("Tipo de pelo no válido.")
    
    # Ensamble del pincel

    def ensamblar_pincel(self,encender):
        cantidad = int(input("Ingrese la Cantidad de pinceles que quiere ensamblar: "))
        cont = 0
        if encender:
            for pedido in range(cantidad):
                pasos = ["Insertando pelo en la férula...", "Fijando la férula al mango", "Añadiendo adhesivo"]
                print("**** Inicio de Proceso ****")
                for paso in pasos:
                    print(paso)
                print("**** Pincel ensamblado con éxito ****\n")
                cont += 1
            self.produccion_total = cont
        else:
            print("Debe cambiar de estado para iniciar la maquina")
        print(f"El total de pinceles ensamblados es de: {self.produccion_total}")

        # Calcula el costo de producion de cada pincel

    def calcular_costo_produccion(self, costo_material):

        return self.produccion_total * costo_material



    
                




    
    
    

        



