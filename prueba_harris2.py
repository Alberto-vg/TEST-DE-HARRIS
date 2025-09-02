def preg(ss=''):
    ban = 1
    while ban == 1:
        res = input(ss + ' : ')
        if res == '0' or res == '1':
            ban = 0
    return int(res)

preguntas = '''
DOMINANCIA DE LA MANO 
1.- Tirar una pelota
2.- Sacar punta a un lapicero
3.- Clavar un clavo
4.- Cepillarse los dientes
5.- Girar el pomo de la puerta
6.- Sonarse
7.- Utilizar las tijeras
8.- Cortar con un cuchillo
9.- Peinarse
10.- Escribir
DOMINANCIA DEL PIE
1.- Dar una patada a un balón
2.- Escribir una letra con el pie
3.- Saltar a la pata coja unos 10 metros
4.- Mantener el equilibrio sobre un pie
5.- Subir un escalón
6.- Girar sobre un pie
7.- Sacar un balón de algún rincón o debajo de una silla
8.- Conducir un balón unos 10 mts.
9.- Elevar una pierna sobre una mesa o silla.
10.- Pierna que adelantas al desequilibrarte adelante
DOMINANCIA DEL OJO 
1.- Sighting (cartón de 15 x 25 con un agujero en el centro de 0,5 cm diamétro)
2.- Telescopio ( tubo largo de cartón )
3.- Caleidoscopio - Cámara de fotos
DOMINANCIA DEL OÍDO 
1.- Escuchar en la pared
2.- Coger el teléfono
3.- Escuchar en el suelo
'''

# Separar las preguntas por categorías
lineas = preguntas.strip().split('\n')
categorias = {}
categoria_actual = ''

for linea in lineas:
    if linea.strip() and not linea.strip().startswith(('1.-', '2.-', '3.-', '4.-', '5.-', '6.-', '7.-', '8.-', '9.-', '10.-')):
        categoria_actual = linea.strip()
        categorias[categoria_actual] = []
    elif linea.strip() and categoria_actual:
        categorias[categoria_actual].append(linea.strip())

# Función para realizar el test de una categoría
def test_categoria(nombre_categoria, preguntas_categoria, instruccion):
    print(f"\n\n{nombre_categoria}")
    print(f"{instruccion}\n")
    
    suma = 0
    for i, pregunta in enumerate(preguntas_categoria, 1):
        res = preg(f"{i}. {pregunta}")
        suma += res
    
    print(f"Total {nombre_categoria.split()[0].lower()}: {suma}/{len(preguntas_categoria)}")
    return suma

# Realizar todos los tests
print("=== TEST DE DOMINANCIA ===")

# Mano
suma_mano = test_categoria(
    "DOMINANCIA DE LA MANO", 
    categorias["DOMINANCIA DE LA MANO"], 
    "Introduzca 0 - si lo hace con la mano izquierda o 1 - mano derecha"
)

# Pie
suma_pie = test_categoria(
    "DOMINANCIA DEL PIE", 
    categorias["DOMINANCIA DEL PIE"], 
    "Introduzca 0 - si lo hace con el pie izquierdo o 1 - pie derecho"
)

# Ojo
suma_ojo = test_categoria(
    "DOMINANCIA DEL OJO", 
    categorias["DOMINANCIA DEL OJO"], 
    "Introduzca 0 - si usa el ojo izquierdo o 1 - ojo derecho"
)

# Oído
suma_oido = test_categoria(
    "DOMINANCIA DEL OÍDO", 
    categorias["DOMINANCIA DEL OÍDO"], 
    "Introduzca 0 - si usa el oído izquierdo o 1 - oído derecho"
)

# Resultados finales
print("\n\n=== RESULTADOS FINALES ===")
print(f"Mano: {suma_mano}/10 - {'Derecha' if suma_mano > 5 else 'Izquierda' if suma_mano < 5 else 'Ambidiestra'}")
print(f"Pie: {suma_pie}/10 - {'Derecho' if suma_pie > 5 else 'Izquierdo' if suma_pie < 5 else 'Ambidiestro'}")
print(f"Ojo: {suma_ojo}/3 - {'Derecho' if suma_ojo > 1.5 else 'Izquierdo' if suma_ojo < 1.5 else 'Ambidiestro'}")
print(f"Oído: {suma_oido}/3 - {'Derecho' if suma_oido > 1.5 else 'Izquierdo' if suma_oido < 1.5 else 'Ambidiestro'}")

# Determinar dominancia general
puntajes = [suma_mano/10, suma_pie/10, suma_ojo/3, suma_oido/3]
promedio = sum(puntajes) / len(puntajes)

if promedio > 0.6:
    dominancia = "DERECHA"
elif promedio < 0.4:
    dominancia = "IZQUIERDA"
else:
    dominancia = "MIXTA/AMBIDIESTRA"

print(f"\nDOMINANCIA GENERAL: {dominancia}")
