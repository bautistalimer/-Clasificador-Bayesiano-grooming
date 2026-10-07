# Detector de Grooming con Naive Bayes (Python)

Implementación educativa de un **Clasificador Bayesiano Ingenuo (*Naive Bayes*) Multinomial** desarrollado desde cero en Python puro, diseñado para la detección automática de posibles casos de grooming (acoso a menores en línea) en mensajes de texto[cite: 188].

---

## 🎯 Objetivo del Proyecto
Entrenar un modelo de aprendizaje automático supervisado utilizando la lógica matemática del Teorema de Bayes y suavización de Laplace para clasificar mensajes de chat en dos categorías:
* `grooming` (mensajes sospechosos o de acoso)[cite: 188]
* `no_grooming` (mensajes cotidianos o seguros)[cite: 188]

---

## ⚙️ Características Técnicas
* **Sin dependencias externas:** Utiliza únicamente librerías nativas de Python (`collections.defaultdict`), ideal para comprender la lógica interna del algoritmo.
* **Procesamiento de texto básico:** Normalización a minúsculas y tokenización por espacios.
* **Suavización de Laplace:** Previene la anulación de probabilidades ante la aparición de palabras no vistas en el conjunto de entrenamiento.
* **Evaluación de rendimiento:** Calcula la **precisión total (accuracy)** y genera una **matriz de confusión** detallada por clases.

---

## 🚀 Instrucciones de Uso

### Requisitos
* Tener instalado **Python 3.x**.

### Ejecución
Clona el repositorio, asegúrate de tener el archivo de código fuente (por ejemplo, `LIMER_BAYES_CODE_GROOMING.py`) y ejecútalo desde tu terminal:

```bash
python LIMER_BAYES_CODE_GROOMING.py
