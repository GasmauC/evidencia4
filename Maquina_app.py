from maquinaPinceles import MaquinaHacerPinceles

# OBJETO 1
pincel1 = MaquinaHacerPinceles("Cerda",500,False)
pincel1.seleccionar_tipo_de_pelo("NYLON")
pincel1.ensamblar_pincel(True)
print(f"El costo total por la cantidad de pinceles fabricados es de: ${pincel1.calcular_costo_produccion(800)} pesos")
# OBJETO 2
pincel2 = MaquinaHacerPinceles("Cerda", 1000,True)
pincel2.seleccionar_tipo_de_pelo("SINTETICO")