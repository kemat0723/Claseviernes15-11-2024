# Práctica NLTK análisis de frecuencia de palabras

import nltk
from nltk.tokenize import word_tokenize #Divide el texto en palabras
from nltk.corpus import stopwords # Elimina los conectores
from nltk.probability import FreqDist # Calcula la frecuencia de las palabras 

texto = """Yo pensaba que la vida
Era distinta
Cuando era chiquitín
Yo creía que las cosas
Eran fácil como ayer
Que mi madre preocupada
Se esmeraba por darme todo lo que necesitaba
Yo me doy cuenta que tanto así no es Porque a mi madre la veo cansada
De trabajar por mi hermano y por mí
Y ahora con ganas quisiera ayudarla
Y por ella la peleo hasta el fin
Por ella lucharé hasta que me muera
Y por ella no me quiero morir
Tampoco que se me muera mi vieja
Pero yo sé que el destino es así Within AI, there are subfields such as machine learning, where systems improve their performance over time by learning from data, and natural language processing (NLP), which enables machines to understand and generate human language.

In summary, AI aims to mimic aspects of human intelligence to make machines more efficient, autonomous, and capable of solving complex problems."""

# Tokenizar el texto 

palabras = word_tokenize(texto, language='spanish')
print(palabras)

# Stopwords Eliminar los conectores

stopwords = set(stopwords.words('spanish'))

# Filtramos las palabras que no estan en la lista de stop words 

palabras_filtradas = [palabra for palabra in palabras if palabra.lower() not in stopwords and palabra.isalpha()]
print(palabras_filtradas)

# Analisis de frecuencia de palabras
frecuencia_palabras = FreqDist(palabras_filtradas)

# Mostrar la frecuencia de las 10 palabras más comunes 

print(frecuencia_palabras.most_common(7))