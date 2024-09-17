# API de Recomendación de Películas

Esta es una API basada en FastAPI que proporciona datos relacionados con películas y recomendaciones. A partir los datasets, responde consultas sobre la cantidad de películas estrenadas por mes, por día, características de las mismas, información sobre actores, directores y un sistema de recomendación de películas basado en la similitud de coseno.

## Características

La API tiene los siguientes endpoints:

1. **Cantidad de Filmaciones por Mes:**

    URL: /cantidad_filmaciones_mes/{mes}
    
    Devuelve la cantidad de películas estrenadas en un mes específico.


2. **Cantidad de Filmaciones por Día:**

    URL: /cantidad_filmaciones_dia/{dia}
    
    Devuelve la cantidad de películas estrenadas en un día específico de la semana.


3. **Puntuación de una Película por Título:**

    URL: /score_titulo/{titulo_de_la_filmacion}
    
    Devuelve la puntuación de popularidad de una película específica.


4. **Votos de una Película por Título:**

    URL: /votos_titulo/{titulo_de_la_filmacion}
    
    Devuelve la cantidad de votos de una película y su puntuación promedio si tiene más de 2000 votos.


5. **Cantidad de Películas de un Actor:**

    URL: /get_actor/{nombre_actor}
    
    Devuelve la cantidad de películas en las que ha participado un actor específico.


6. **Cantidad de Películas Dirigidas por un Director:**

    URL: /get_director/{nombre_director}
    
    Devuelve la cantidad de películas dirigidas por un director específico.


7. **Recomendación de Películas:**

    URL: /modelo_recomendacion/{title}
    
    Devuelve una lista de 5 películas recomendadas con su título, popularidad, año de estreno y sinopsis.


## Archivos de Dataset:

movies_api_acotado_datasets.parquet: Contiene información sobre las películas.

cast_dataset.csv: Contiene información sobre los actores.

crew_dataset.csv: Contiene información sobre el personal involucrado en las películas.
