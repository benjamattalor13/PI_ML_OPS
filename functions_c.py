import pandas as pd
import numpy as np

def PlayTimeGenre(genero: str):
    '''
    ### 1)
    ```py
    def PlayTimeGenre( genero : str ):
    ```
    Debe devolver año con mas horas jugadas para dicho género.
    Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}
    '''
    consulta1 = pd.read_csv('consulta1.csv')
    
    def acomodar_palabras(genres):
        palabras = genres.split(', ')
        palabras_juntas = ''.join(palabra.replace(' ', '') for palabra in palabras)
        return palabras_juntas.capitalize()
    
    consulta1['aco_genres'] = consulta1['genres'].apply(acomodar_palabras)
    consulta1['aco_genres'] = consulta1['aco_genres']
    
    consulta1 = consulta1.drop('genres', axis=1)
    consulta1 = consulta1.rename(columns={'aco_genres': 'genres'})
    genero = genero.capitalize()

    filtered_df = consulta1[consulta1['genres'] == genero]

    if filtered_df.empty:
        return {"Género no encontrado en el conjunto de datos"}

    grouped_df = filtered_df.groupby('release_date')['playtime_forever'].sum()

    max_year = grouped_df.idxmax()

    result = {"Año de lanzamiento con más horas jugadas para {}:".format(genero): max_year}

    return result

def UserForGenre(genero: str):
    '''
    ### 2)
    ```py
    def UserForGenre( genero : str ):
    ```
    Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
    Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}
    '''
    consulta2 = pd.read_csv('consulta2.csv')
    
    def acomodar_palabras(genres):
        palabras = genres.split(', ')
        palabras_juntas = ''.join(palabra.replace(' ', '') for palabra in palabras)
        return palabras_juntas.capitalize()
    
    consulta2['aco_genres'] = consulta2['genres'].apply(acomodar_palabras)
    consulta2['aco_genres'] = consulta2['aco_genres']
    
    consulta2 = consulta2.drop('genres', axis=1)
    consulta2 = consulta2.rename(columns={'aco_genres': 'genres'})
    
    genero = genero.capitalize()
    
    genre_data = consulta2[consulta2['genres'] == genero]

    top_user = genre_data.loc[genre_data['playtime_forever'].idxmax()]['user_id']

    hours_by_year = genre_data.groupby('release_date')['playtime_forever'].sum().reset_index()
    hours_by_year = hours_by_year.rename(columns={'release_date': 'Año', 'playtime_forever': 'Horas'})
    hours_by_year['Horas'] = (hours_by_year['Horas'] / 60).astype(int)
    hours_list = hours_by_year.to_dict(orient='records')

    result = {
        "Usuario con más horas jugadas para Género {}".format(genero): top_user,
        "Horas jugadas": hours_list
    }

    return result

def UsersRecommend(año: int):
    consulta3 = pd.read_csv('consulta3.csv')
    if type(año) != int:
        return {"Debes colocar el año en entero, EJ:2015"}
    if año < consulta3['year_posted'].min() or año > consulta3['year_posted'].max():
        return {"Año no encontrado en el conjunto de datos"}
    
    filtered_reviews = consulta3[(consulta3['year_posted'] == año)]
    top3_games = filtered_reviews.nlargest(3, 'total_sentiment_analysis')[['tags', 'total_sentiment_analysis']]
    
    # Crear el formato de retorno
    result = [{f"Puesto {i+1}": juego} for i, juego in enumerate(top3_games['tags'])]

    return result

def UsersWorstDeveloper(anio:int):
    consulta4 = pd.read_csv('consulta4.csv')
    if type(anio) != int:
        return {"Debes colocar el año en entero, EJ:2015"}
    if anio < consulta4['year_posted'].min() or anio > consulta4['year_posted'].max():
        return {"Año no encontrado en el conjunto de datos"}

    filtered_df = consulta4[consulta4['year_posted'] == anio]

    top_worst = filtered_df.groupby('developer')['sentiment_analysis'].sum().nlargest(3).reset_index()

    result = [{"Puesto {}: {}".format(i + 1, row['developer'])} for i, row in top_worst.iterrows()]

    return result

def sentiment_analysis(develop:str):
    consulta5 = pd.read_csv('consulta5.csv')
    def juntar_palabras(genres):
        palabras = genres.split(', ')
        palabras_juntas = ''.join(palabra.replace(' ', '') for palabra in palabras)
        return palabras_juntas.capitalize()

    consulta5['developer'] = consulta5['developer'].apply(juntar_palabras)

    develop = develop.capitalize()
    if type(develop) != str:
        return "Debes colocar un desarrollador de tipo str, EJ:'Valve'"
    if len(develop) == 0:
        return "Debes poner un desarrolador en tipo String"
    filtered_df = consulta5[consulta5['developer'] == develop]
    sentiment_counts = filtered_df['sentiment_analysis'].value_counts()
    result = {develop: f"[Negative = {sentiment_counts.get(0, 0)}, Neutral = {sentiment_counts.get(1, 0)}, Positive = {sentiment_counts.get(2, 0)}]"}
    return result

def recomendacion_juego(id_juego:int):
    modelo_df = pd.read_csv('consulta6.csv')
    if id_juego not in modelo_df["item_id"].values:
        return "El id ingresado no existe en el dataset"

    indice_juego = modelo_df[modelo_df["ItemId"] == id_juego].index[0]

    recomendaciones = modelo_df.iloc[indice_juego]["recomendaciones_top_5"]

    return recomendaciones