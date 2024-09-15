from fastapi import FastAPI
import uvicorn
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity


# Instancia de FastAPI
app = FastAPI()

# Cargar los datasets
df_movies_api_acotado = pd.read_csv("movies_api_acotado_datasets.csv")
df_cast_api = pd.read_csv("cast_dataset.csv")
df_crew_api = pd.read_csv("crew_dataset.csv")

# Seleccionar las columnas relevantes
df_features = df_movies_api_acotado[['release_year', 'name_genres', 'iso_3166_1_country', 'popularity']].head(20000)

# Codificación One-Hot para columnas categóricas
df_features = pd.get_dummies(df_features, columns=['name_genres', 'iso_3166_1_country'])

# Normalización de columnas numéricas
scaler = StandardScaler()
df_features[['popularity']] = scaler.fit_transform(df_features[['popularity']])

# Asegurarnos de que las columnas estén en el orden correcto
df_features = df_features.sort_index(axis=1)

# Convertir la columna 'release_date' a tipo datetime
df_movies_api_acotado['release_date'] = pd.to_datetime(df_movies_api_acotado['release_date'], errors='coerce')

# Convertir la columna 'release_year' a tipo entero
df_movies_api_acotado['release_year'] = df_movies_api_acotado['release_year'].astype('Int64')

# Convertir la columna 'popularity' a tipo float
df_movies_api_acotado['popularity'] = df_movies_api_acotado['popularity'].astype(float)
df_movies_api_acotado['popularity'] = df_movies_api_acotado['popularity'].round(2)

# Eliminar valores nulos
df_movies_api_acotado.dropna(subset=['vote_count', 'revenue', 'budget', 'runtime', 'id_production_companies'], inplace=True)
df_movies_api_acotado['overview'] = df_movies_api_acotado['overview'].fillna('')
df_movies_api_acotado = df_movies_api_acotado.reset_index(drop=True)

# Calcular la matriz de similitud
cosine_sim = cosine_similarity(df_features, df_features)

# Defino ROOT
@app.get("/")
def read_root():
    return "Welcome to the API"

# Endpoint 1: Cantidad de filmaciones por mes
@app.get("/cantidad_filmaciones_mes/{mes}")
def cantidad_filmaciones_mes(mes: str):
    mes_map = {
        "enero": "01", "febrero": "02", "marzo": "03", "abril": "04",
        "mayo": "05", "junio": "06", "julio": "07", "agosto": "08",
        "septiembre": "09", "octubre": "10", "noviembre": "11", "diciembre": "12"
    }
    mes_num = mes_map.get(mes.lower())
    if not mes_num:
        return "Mes no válido"
    
    cantidad = df_movies_api_acotado[df_movies_api_acotado['release_date'].dt.strftime('%m') == mes_num].shape[0]
    return f"{cantidad} películas fueron estrenadas en el mes de {mes}"

# Endpoint 2: Cantidad de filmaciones por día
@app.get("/cantidad_filmaciones_dia/{dia}")
def cantidad_filmaciones_dia(dia: str):
    dia_map = {
        "lunes": 0, "martes": 1, "miércoles": 2,
        "jueves": 3, "viernes": 4, "sábado": 5, "domingo": 6
    }
    dia_num = dia_map.get(dia.lower())
    if dia_num is None:
        return "Día no válido"

    cantidad = df_movies_api_acotado[df_movies_api_acotado['release_date'].dt.dayofweek == dia_num].shape[0]
    return f"{cantidad} películas fueron estrenadas en el día {dia}"

# Endpoint 3: Score del título
@app.get("/score_titulo/{titulo_de_la_filmacion}")
def score_titulo(titulo_de_la_filmacion: str):
    pelicula = df_movies_api_acotado[df_movies_api_acotado['title'].str.contains(titulo_de_la_filmacion, case=False, na=False)]
    if pelicula.empty:
        return "Película no encontrada"
    
    pelicula = pelicula.iloc[0]
    titulo = pelicula['title']
    ano_estreno = pelicula['release_year']
    score = pelicula['popularity']
    return f"La película '{titulo}' fue estrenada en el año {ano_estreno} con un score/popularidad de {score}"

# Endpoint 4: Votos del título
@app.get("/votos_titulo/{titulo_de_la_filmacion}")
def votos_titulo(titulo_de_la_filmacion: str):
    pelicula = df_movies_api_acotado[df_movies_api_acotado['title'] == titulo_de_la_filmacion]
    if pelicula.empty:
        return f"La película '{titulo_de_la_filmacion}' no se encuentra en el dataset."
    
    votos = int(pelicula['vote_count'].values[0])
    if votos < 2000:
        return f"La película '{titulo_de_la_filmacion}' no tiene suficientes valoraciones."
    
    promedio_votos = pelicula['vote_average'].values[0]
    año_estreno = int(pelicula['release_year'].values[0])
    return (f"La película '{titulo_de_la_filmacion}' fue estrenada en el año {año_estreno}. "
            f"Tiene {votos} valoraciones, con un promedio de {promedio_votos:.2f}.")

# Endpoint 5: Cantidad de películas de un actor
@app.get("/get_actor/{nombre_actor}")
def get_actor(nombre_actor: str):
    peliculas_actor = df_cast_api[df_cast_api['name'].str.contains(nombre_actor, case=False, na=False)]
    cantidad_peliculas = len(peliculas_actor)
    if cantidad_peliculas > 0:
        return f"El actor {nombre_actor} ha participado en {cantidad_peliculas} películas."
    return f"No se encontraron películas para el actor '{nombre_actor}'."

# Endpoint 6: Cantidad de películas de un director
@app.get("/cantidad_peliculas_director/{nombre_director}")
def cantidad_peliculas_director(nombre_director: str):
    peliculas_director = df_crew_api[(df_crew_api['name'] == nombre_director) & (df_crew_api['job'] == 'Director')]
    cantidad_peliculas = len(peliculas_director)
    if cantidad_peliculas > 0:
        return f"El director {nombre_director} ha dirigido {cantidad_peliculas} películas."
    return f"No se encontraron películas para el director '{nombre_director}'."

# Modelo de recomendación
@app.get("/modelo_recomendacion/{title}")
def recommend_movies(title: str):
    # Verificar si el título existe en el DataFrame original
    if title not in df_movies_api_acotado['title'].values:
        return "Título no encontrado en el DataFrame."
    
    # Obtener el índice de la película seleccionada
    idx = df_movies_api_acotado.index[df_movies_api_acotado['title'] == title].tolist()[0]
    
    # Obtener las puntuaciones de similitud para la película seleccionada
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Ordenar las películas por la puntuación de similitud
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Seleccionar las 5 películas más similares (excluyendo la película propia)
    sim_scores = sim_scores[1:6]
    
    # Obtener los índices de las películas más similares
    movie_indices = [i[0] for i in sim_scores]
    
    # Devolver la lista de películas recomendadas
    recommended_movies = df_movies_api_acotado.iloc[movie_indices][['title', 'popularity', 'release_year', 'overview']]
    return recommended_movies.to_dict(orient='records')
