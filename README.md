# Proyecto de API de Películas

Este repositorio contiene una API desarrollada en FastAPI para consultar y analizar información sobre películas. La API está diseñada para interactuar con un conjunto de datos que incluye detalles sobre películas, actores, directores y otros aspectos relacionados. A continuación, se detallan los endpoints disponibles y la estructura de los datasets utilizados.

## Endpoints

La API ofrece los siguientes endpoints para consultar la información de películas:

### 1. `cantidad_filmaciones_mes(Mes)`
-   Devuelve la cantidad de películas estrenadas en un mes específico del dataset.
- **Parámetro**: `Mes` (nombre del mes en formato de texto, e.g., "Enero").
- **Respuesta**: Cantidad de películas estrenadas en el mes solicitado.

### 2. `cantidad_filmaciones_dia(Dia)`
-   Devuelve la cantidad de películas estrenadas en un día específico de la semana.
- **Parámetro**: `Dia` (nombre del día de la semana en formato de texto, e.g., "Lunes").
- **Respuesta**: Cantidad de películas estrenadas en el día solicitado.

### 3. `score_titulo(titulo_de_la_filmación)`
-   Devuelve el título, el año de estreno y el score (valoración promedio) de una película específica.
- **Parámetro**: `titulo_de_la_filmación` (título de la película).
- **Respuesta**: Título de la película, año de estreno y score.

### 4. `votos_titulo(titulo_de_la_filmación)`
-   Devuelve el título, la cantidad de votos y el valor promedio de las votaciones si hay al menos 2000 valoraciones; en caso contrario, devuelve un mensaje indicando que no cumple con la condición.
- **Parámetro**: `titulo_de_la_filmación` (título de la película).
- **Respuesta**: Título de la película, cantidad de votos y valor promedio de las votaciones o un mensaje indicando la falta de suficiente información.

### 5. `get_actor(nombre_actor)`
-   Devuelve la cantidad de películas en las que ha participado el actor.
- **Parámetro**: `nombre_actor` (nombre del actor).
- **Respuesta**: `nombre_actor` ha participado en X cantidad de películas.

### 6. `get_director(nombre_director)`
-   Devuelve la cantidad de películas en las que ha participado el director.
- **Parámetro**: `nombre_director` (nombre del director).
- **Respuesta**: `nombre_director` ha participado en X cantidad de películas.

### 7. `modelo_recomendacion(titulo)`
-   Devuelve una lista de 5 películas similares a la película ingresada por el usuario, en orden descendente de puntuación de similitud.
- **Parámetro**: `titulo` (título de la película para la cual se desean recomendaciones).
- **Respuesta**: Lista de 5 títulos de películas similares.

## Datasets Utilizados

El proyecto utiliza los siguientes datasets:

### `df_movies_api_acotado`
-   Contiene información sobre películas.
- **Columnas**:
  - `id_collection`: Identificador de la colección.
  - `name_collection`: Nombre de la colección.
  - `budget`: Presupuesto de la película.
  - `id`: Identificador de la película.
  - `original_language`: Idioma original de la película.
  - `overview`: Descripción de la película.
  - `popularity`: Popularidad de la película.
  - `release_date`: Fecha de lanzamiento de la película.
  - `revenue`: Ingresos generados por la película.
  - `runtime`: Duración de la película en minutos.
  - `status`: Estado actual de la película.
  - `title`: Título de la película.
  - `vote_average`: Valoración promedio de la película.
  - `vote_count`: Número de votos recibidos.
  - `return`: Retorno de la película.
  - `release_year`: Año de lanzamiento de la película.
  - `id_genres`: Identificadores de géneros.
  - `name_genres`: Nombres de géneros.
  - `iso_3166_1_country`: Código de país.
  - `country`: Nombre del país.
  - `production_companies`: Compañías productoras.
  - `id_production_companies`: Identificadores de compañías productoras.

### `df_cast_api`
-   Contiene información sobre el elenco de las películas.
- **Columnas**:
  - `cast_id`: Identificador del cast.
  - `id`: Identificador de la película.
  - `name`: Nombre del actor.
  - `character`: Personaje interpretado por el actor.
  - `credit_id`: Identificador del crédito.

### `df_crew_api`
-   Contiene información sobre el equipo de producción de las películas.
- **Columnas**:
  - `credit_id`: Identificador del crédito.
  - `id`: Identificador de la película.
  - `name`: Nombre del miembro del equipo.
  - `job`: Rol o trabajo del miembro del equipo.
  - `department`: Departamento al que pertenece el miembro del equipo.

