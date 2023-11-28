from fastapi import FastAPI, HTTPException, Request
import pandas as pd
import json
import numpy as np
from fastapi.responses import JSONResponse, HTMLResponse
from functions_c import PlayTimeGenre
from functions_c import UserForGenre
from functions_c import UsersRecommend
from functions_c import recomendacion_juego

app = FastAPI()

@app.get('/', response_class=HTMLResponse)
def hola():
    html_content = """
        <!DOCTYPE html>
        <html lang="es">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Mi Página Personalizada</title>
                <style>
                    body {
                        background-color: #e6f7ff; /* Cambiar a tu color de fondo deseado */
                        color: #333; /* Texto negro */
                        margin: 20px;
                        font-family: 'Verdana', sans-serif; /* Puedes cambiar la fuente si lo deseas */
                    }

                    h1 {
                        font-size: 2.5em; /* Tamaño de la fuente para h1 */
                        color: #3366cc; /* Cambiar el color del título */
                    }

                    h2 {
                        font-size: 1.8em; /* Tamaño de la fuente para h2 */
                        color: #3366cc; /* Cambiar el color del subtítulo */
                    }

                    p {
                        line-height: 1.5; /* Espaciado entre líneas del párrafo */
                    }

                    ul {
                        list-style-type: square; /* Cambiar el tipo de viñeta de la lista */
                        padding-left: 20px;
                    }

                    li {
                        margin-bottom: 8px; /* Espacio entre elementos de la lista */
                    }

                    a {
                        color: #990000; /* Color del enlace (rojo en este caso) */
                        text-decoration: underline; /* Subrayado de los enlaces */
                    }

                    a:hover {
                        color: #cc0000; /* Cambiar el color al pasar el mouse sobre el enlace */
                    }
                </style>
            </head>
            <body>
                <h1>Bienvenido a mi API</h1>
                <p>Hola, soy Franco Benjamín Mattarollo de SOYHENRY y estoy en la cohorte dataft-17.</p>

                <h2>Endpoints:</h2>
                <ul>
                    <li><a href="https://pi-ml-ops-proyecto.onrender.com//PlayTimeGenre/Action">/PlayTimeGenre/Action</a></li>
                    <li><a href="https://pi-ml-ops-proyecto.onrender.com/UserForGenre/Adventure">/UserForGenre/Adventure</a></li>
                    <li><a href="https://pi-ml-ops-proyecto.onrender.com/UsersRecommend/2012">/UsersRecommend/2012</a></li>
                    <li><a href="https://pi-ml-ops-proyecto.onrender.com/recomendacion_juego/10">/recomendacion_juego/10</a></li>
                </ul>
            </body>
        </html>
    """

@app.get("/PlayTimeGenre/{genero}")
async def play_time_genre(genero:str):
    try:
        resultado = PlayTimeGenre(genero)
        return resultado
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/UserForGenre/{genero}")
async def user_for_genre(genero:str):
    try:
        resultado = UserForGenre(genero)
        return resultado
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/UsersRecommend/{anio}")
async def users_recommend(anio:int):
    try:
        anio_int = int(anio)
    except ValueError:
        return {"detail": [{"type": "invalid_input", "msg": "El año debe ser un número entero"}]}

    result = UsersRecommend(anio_int)
    return result

@app.get("/recomendacion_juego/{id_juego}")
async def recomendacion_juego_route(id_juego:int):
    try:
        id_juego = int(id_juego)
    except ValueError:
        return {"detail": [{"type": "invalid_input", "msg": "El año debe ser un número entero"}]}

    result = recomendacion_juego(id_juego)
    return result     