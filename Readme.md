<h1 align="center"> Proyecto ML STEAM </h1>

<img src="https://www.trustedreviews.com/wp-content/uploads/sites/54/2023/04/Steam-Logo.jpg" alt="steam" width="500" style="display: block; margin: auto;">

## Introduccion

Bienvenidos a mi proyecto de Machine Learning. Soy Franco Benjamín Mattarollo, estoy cursando la carrera de Data Science en SOYHENRY.

La tarea que se presenta en este proyecto implica la creación de un flujo de trabajo para Machine Learning Operations (MLOps) que abarque fases de Ingeniería de Datos mediante Extraction, Transform and Load (ETL), avance hacia el aprendizaje automático con Exploratory Data Analysis (EDA), abordando la exploración y entrenamiento de modelos, culminando con la implementación tanto del modelo como de los puntos finales (endpoints).

## Rol a desarrollar

Empezaste a trabajar como **`Data Scientist`** en Steam, una plataforma multinacional de videojuegos. El mundo es bello y vas a crear tu primer modelo de ML que soluciona un problema de negocio: Steam pide que te encargues de crear un sistema de recomendación de videojuegos para usuarios.

Vas a sus datos y te das cuenta que la madurez de los mismos es poca (ok, es nula): Datos anidados, de tipo raw, no hay procesos automatizados para la actualización de nuevos productos, entre otras cosas… haciendo tu trabajo imposible. 

Debes empezar desde 0, haciendo un trabajo rápido de **`Data Engineer`** y tener un **`MVP`** (_Minimum Viable Product_) para el cierre del proyecto! Tu cabeza va a explotar 🤯, pero al menos sabes cual es, conceptualmente, el camino que debes de seguir. Así que espantas los miedos y pones manos a la obra

## Propuesta del Trabajo

**`Transformaciones`**:  Para este MVP no se te pide transformaciones de datos(` aunque encuentres una motivo para hacerlo `) pero trabajaremos en leer el dataset con el formato correcto. Puedes eliminar las columnas que no necesitan para responder las consultas o preparar los modelos de aprendizaje automático, y de esa manera optimizar el rendimiento de la API y el entrenamiento del modelo.

**`Feature Engineering`**:  En el dataset *user_reviews* se incluyen reseñas de juegos hechos por distintos usuarios. Debes crear la columna ***'sentiment_analysis'*** aplicando análisis de sentimiento con NLP con la siguiente escala: debe tomar el valor '0' si es malo, '1' si es neutral y '2' si es positivo. Esta nueva columna debe reemplazar la de user_reviews.review para facilitar el trabajo de los modelos de machine learning y el análisis de datos. De no ser posible este análisis por estar ausente la reseña escrita, debe tomar el valor de `1`.

**`Desarrollo API`**:   Propones disponibilizar los datos de la empresa usando el framework ***FastAPI***. Las consultas que propones son las siguientes:

<sub> Debes crear las siguientes funciones para los endpoints que se consumirán en la API, recuerden que deben tener un decorador por cada una (@app.get(‘/’)).<sub/>


```py
def PlayTimeGenre(genero: str):
```
    Debe devolver `año` con mas horas jugadas para dicho género.
  
Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}

```py
def UserForGenre(genero: str):
```
    Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.

Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf,
			     "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}

```py
def UsersRecommend(año: int):
```
    Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
  
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

Sistema de recomendación item-item:
    ```py
    def recomendacion_juego( id de producto ):
    ```
        Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.


## Objetivos del Proyecto
Nuestra meta principal consiste en desarrollar y lanzar un sistema de recomendación de juegos, incorporando endpoints accesibles online capaces de satisfacer las funciones solicitadas. Para lograr esto, nos enfocaremos en alcanzar los siguientes hitos específicos:

1. Procesamiento de Datos y Análisis Exploratorio:

    - Implementaremos técnicas de Extracción, Transformación y Carga (ETL) para optimizar la utilización de conjuntos de datos.
    - Realizaremos un análisis exploratorio de datos (EDA) para obtener insights valiosos.

2. Diseño e Implementación de API:

    - Desarrollaremos una API que estará disponible online para abordar las necesidades previamente identificadas.

3. Modelo de Machine Learning para Recomendaciones:

    - Crearemos un modelo de aprendizaje automático que pronosticará recomendaciones de juegos.
    - Al proporcionar el ID del ítem deseado, la API devolverá una lista con los 5 juegos recomendados según el género del juego seleccionado.

4. Despliegue de la API en Producción:

    - Implementaremos la API en un entorno de producción para garantizar su accesibilidad general.
    - Aplicaremos las mejores prácticas para asegurar un rendimiento óptimo y una experiencia de usuario fluida.

5. MLOps: Gestión Eficiente del Proyecto:

    - Estableceremos una infraestructura de MLOps para facilitar de manera eficiente todas las fases del proyecto, desde la transformación de datos hasta el despliegue.
    - Comprometidos con una operación sin contratiempos, buscaremos garantizar la eficiencia en todas las etapas del emocionante proyecto.

## Ámbito de Proyecto

- Procesamiento y exploración de datos de la base:

    [Análisis y limpieza de datos](ETL.ipynb)
  
    [Consultas y extracción de datos](2_Consultas.ipynb)

- Construcción del modelo de aprendizaje:

    [Modelo de Machine Learning basado en items](3_Modelo_ML.ipynb)

- Desarrollo de funciones y API's:

    [Testeo de las funciones](funciones.ipynb)
  
    [Funciones para la API](functions_c.py)
  
    [Main de las funciones](main.py)
  
    [Requisitos](requisitos.txt)
  

    Para poder ejecutar el primer archivo que carga los JSON, los transforma y crea los datasets limpios (ETL.ipynb) hay que descargar los JSON que contienen la información en bruto del proyecto y colocarlos dentro de la carpeta del proyecto.
  
    Enlace para descarga de los archivos JSON

    https://drive.google.com/drive/folders/17WXp9WirTzoV3fxmvZizTHtEqh02yoV_?usp=sharing

## Pasos realizados para el proyecto

- ETL (Extract, Transform, Load) y EDA (Exploratory Data Analysis)

    Esta etapa del proyecto consistió en las siguientes tareas:

    Extracción de Datos (Extract): Se obtuvieron los datos que nos facilitaron en Formato JSON. Son 3 bases con información de los juegos de Steam, Reviews y datos de usuarios.

    Transformación de Datos (Transform): Los datos fueron procesados y transformados para asegurar la coherencia y la integridad. Esto implicó la limpieza de datos, la estandarización de formatos, tipos de datos y la manipulación de variables para prepararlos para el análisis.

    Carga de Datos (Load): Los datos transformados fueron cargados en el entorno de trabajo,en formato .csv y cargados en github, para facilitar su acceso y análisis posterior.

    Análisis Exploratorio de Datos (EDA): Se realizó un análisis exploratorio para comprender mejor la naturaleza de los datos. Esto implicó la visualización de patrones, la identificación de tendencias y la detección de posibles relaciones entre variables clave.

- Machine Learning:

    Esta etapa del proyecto incluyó los siguientes pasos:

    Selección de Modelos: Se escogió el modelo de machine learning de relacion item-item, y se analizaron las bases propuestas para generear una solucion específica.

    Entrenamiento del Modelo: Los modelos escogidos fueron entrenados utilizando los datos previamente procesados durante la etapa ETL. Se realizaron ajustes y optimizaciones para mejorar el rendimiento del modelo.

    Validación del Modelo: Se realizaron pruebas y validaciones cruzadas para evaluar la precisión y la generalización del modelo en conjuntos de datos independientes.

    Optimización del Modelo: Se realizaron ajustes adicionales para optimizar el modelo.

- Deployment y API:

    Montaje de la API (Local): Se implementó un entorno virtual para permitir la interacción con el modelo de machine learning y las consultas antes pedidas.

    Despliegue en Render (Deploy-Render): Se procedió al despliegue de la API en un entorno de producción utilizando las plataformas Render y github en la nube. Esto permitió que la funcionalidad estuviera disponible de manera accesible para usuarios finales.

    Monitoreo y Mantenimiento: Se probaron tanto el modelo como los endpoints para chequear su rendimiento y velocidad de respuesta en tiempo real de la API desplegada.

## Video

Aqui explico mi proyecto en el video:
https://youtu.be/Ps8Kd2PD2ls

## Agradecimiento

Quiero agradecer a mi compañero de cohorte que me ayudo en desarrollar mi primer proyecto

Quiero agradecer a los que me ayudaron durante toda esta carrera a aprender y a progresar

Valoro enormemente el trabajo en equipo y la cooperación que mostraron en cada momento. Este logro es el resultado de la participación y la contribución de cada uno de ustedes.

Estoy muy agradecido de haber formado parte de este grupo tan profesional y entusiasta. Espero que sigamos trabajando juntos y compartiendo nuevos éxitos en nuestro camino académico y laboral.

Muchas gracias por su ayuda

| Francisco Rombini | Johanna Rangel | Juan Ochoa |
| --- | --- | --- |
| [<img src="https://avatars.githubusercontent.com/Frombini" width=75><br><sub>Francisco Rombini</sub>](https://github.com/Frombini) | [<img src="https://avatars.githubusercontent.com/JohannaRangel" width=75><br><sub>Johanna Rangel</sub>](https://github.com/JohannaRangel) | [<img src="https://avatars.githubusercontent.com/u/121000341?v=4" width=75><br><sub>Juan Ochoa</sub>](https://github.com/Juangabi8a) |