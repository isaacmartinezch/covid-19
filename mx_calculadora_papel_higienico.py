#Definir el consumo de papel higiénico en México.
#Fuente de información: https://www.statista.com/outlook/80000000/116/tissue-hygiene-paper/mexico#market-volume
print("De acuerdo con datos de www.statista.com, en el 2019, cada mexicano, en promedio, consumió alrededor de 7.49kg de papel higiénico al año.")
print("Cada rollo contiene aproximadamente 90g, lo que equivale a 83 rollos de papel por año.")
print("La Secretaría de Salud en México ha sugerido un periodo de aislamiento de 30 días. Por lo tanto, usted necesitará papel higiénico suficiente para un mes.")
print("La siguiente pregunta lo orientará para comprar la cantidad de papel necesaria para su cuarentena: ")
#Los paquetes de papel contienen 4,6,12,18,24,36 y 48 rollos.
w_roll = 90/1000 #Convertimos el peso de los rollos en gramos a kilogramos.
kg_person = 7.49 #Consumo anual expresado en kilogramos.
annual_cons = kg_person/w_roll #Obtenemos el total de rollos.
monthly_cons = annual_cons/12 #Obtenemos los rollos que necesita una persona al mes.
family_size = int(input("¿Cuántas personas viven en su hogar? "))
paq_size = 0
#Definición de la cantidad de rollos que se necesitan en el hogar.
if family_size == 1:
    monthly_cons = int(monthly_cons * 1)
    print(f"Usted necesita {monthly_cons} rollos de papel por mes.")
else:
    monthly_cons = int(monthly_cons * family_size)
    print(f"En su hogar necesitan {monthly_cons} rollos de papel por mes.")
#Definición de la cantidad y tamaño de los paquetes que debería comprar
if monthly_cons <= 6:
    paq_size = 6
elif monthly_cons <= 12:
    paq_size = 12
elif monthly_cons <= 18:
    paq_size = 18
elif monthly_cons <= 24:
    paq_size = 24
elif monthly_cons <= 36:
    paq_size = 36
elif monthly_cons <= 48:
    paq_size = 48
    print(f"Se aconseja que compre solamente un paquete de {paq_size} rollos para toda la cuarentena.")
else:
    print("Necesita más de un paquete de 48 rollos. Calcule 6 rollos adicionales por persona a partir de 8 personas")
print("Sea solidario con los demás y compre únicamente lo que necesita.")

