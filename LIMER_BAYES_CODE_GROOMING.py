from collections import defaultdict

mensajes = [
    {"texto":"¿Cuántos años tenés? No le digas a nadie que hablamos. ", "clase":"grooming"},
    {"texto":"Hola, ¿cómo estás? ¿Querés jugar algo online? ", "clase":"no_grooming"},
    {"texto":"Sos muy linda, no le muestres esto a tus papás. ", "clase":"grooming"},
    {"texto":"¿Terminaste la tarea de matemáticas? ", "clase":"no_grooming"},
    {"texto":"Podés mandarme una foto tuya, pero que sea solo para mí. ", "clase":"grooming"},
    {"texto":"¿Querés que te ayude con el juego que no podías pasar? ", "clase":"no_grooming"},
    {"texto":"No le contés a nadie que hablamos por acá, ¿sí? ", "clase":"grooming"},
    {"texto":"¿Te gustó la película de ayer?", "clase":"no_grooming"},
    {"texto":"¿Estás solo en casa ahora? ", "clase":"grooming"},
    {"texto":"¿Querés hacer una videollamada para estudiar juntos?", "clase":"no_grooming"},
    {"texto":"No le digas a tus padres que te escribí, es nuestro secreto.", "clase":"grooming"},
    {"texto":"¿Cómo te fue en el examen de historia?", "clase":"no_grooming"},
    {"texto":"Mandame una foto tuya, pero que nadie más la vea.", "clase":"grooming"},
    {"texto":"¿Jugamos Minecraft esta tarde?", "clase":"no_grooming"},
    {"texto":"Sos muy especial para mí, no le cuentes a nadie lo que hablamos.", "clase":"grooming"},
    {"texto":"¿Querés que te pase los apuntes de biología?", "clase":"no_grooming"},
    {"texto":"¿Podés mostrarme cómo estás vestida ahora?", "clase":"grooming"},
    {"texto":"¿Tenés ganas de salir a andar en bici mañana?", "clase":"no_grooming"},
    {"texto":"No hace falta que le digas a nadie que hablamos tanto. ", "clase":"grooming"},
    {"texto":"¿Querés que estudiemos juntos para el parcial?", "clase":"no_grooming"},
    ]   

for item in mensajes:
    item["palabras"] = item["texto"].lower().split()

conteo_clases = defaultdict(int)
for item in mensajes:
    clase= item["clase"]
    conteo_clases[clase] += 1

total_mensajes = len(mensajes)
P_clase = {}
for clase, conteo in conteo_clases.items():
    P_clase[clase]= conteo / total_mensajes

conteo_palabras = defaultdict(lambda: defaultdict(int))
total_palabras_por_clase = defaultdict(int)
vocabulario = set()

for item in mensajes:
    clase = item["clase"]
    for palabra in item["palabras"]:
        conteo_palabras[clase][palabra] += 1
        total_palabras_por_clase[clase] +=1
        vocabulario.add(palabra)

def probabilidad_palabra_dada_clase(palabra, clase):
    return (conteo_palabras[clase][palabra] + 1) / (total_palabras_por_clase[clase] + len(vocabulario))

def clasificar_texto(lista_palabras):
    probabilidades = {}
    for clase in P_clase:
        prob = P_clase[clase]
        for palabra in lista_palabras:

            if palabra in vocabulario:
                prob *= probabilidad_palabra_dada_clase(palabra, clase)
        probabilidades[clase] = prob

    maximo = max(probabilidades.values())
    for clase, prob in probabilidades.items():
        if prob == maximo:
            return clase

aciertos = 0
matriz_confusion = {
    "grooming": {"grooming": 0, "no_grooming": 0},
    "no_grooming": {"grooming": 0, "no_grooming": 0}
}

for item in mensajes:
    clase_real = item["clase"]
    clase_predicha = clasificar_texto(item["palabras"])
    
    matriz_confusion[clase_real][clase_predicha] += 1
    if clase_real == clase_predicha:
        aciertos += 1

precision_total = (aciertos / total_mensajes) * 100

print(f'''RESULTADOS:
    Precisiocion total (accuracy): {precision_total: }

    Matriz de confusión: 
    (filas: real | columnas: predicho)
    real grooming » predicho grooming: {matriz_confusion['grooming']['grooming']} | real grooming» predicho no grooming: {matriz_confusion['grooming']['no_grooming']}
    real no grooming » predicho grooming: {matriz_confusion['no_grooming']['grooming']} | real no grooming » predicho no grooming: {matriz_confusion['no_grooming']['no_grooming']}
''')

nuevos_mensajes = [ 
"¿Podés mandarme una foto tuya? No se la muestres a nadie.", 
"¿Jugamos Minecraft esta tarde?",
"No le digas a tus papás que hablamos, ¿sí?",
"¿Terminaste el trabajo práctico de historia?"
] 
print("================================================================================================")
print("clasificacion de mensajes acusados de grooming")
for i, texto in enumerate(nuevos_mensajes, 1):
    palabras_nuevas = texto.lower().split()
    resultado = clasificar_texto(palabras_nuevas)
    print(f"{i}. {texto} » {resultado}")
