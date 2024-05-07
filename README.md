# MLOps_P3

1. Video 

[![Texto alternativo](https://img.youtube.com/vi/YPbuRMIL1H8/0.jpg)](https://www.youtube.com/watch?v=YPbuRMIL1H8)

3. INgrese a la interfaz grafica de Airflow en la direccion: http://10.43.101.151:8080/home y haga clic en el boton que dispara el DAG, si lo desea puede seguir el desarrollo de la ejecucion haciendo clic en la celda last run que ahora tiene la fecha actual del ultimo run enviado.

   inserte imagen del airflow con el boton del dag encerrado

Una vez esta ejecucion termine con las 3 cajas del grafo en status success el modelo estara disponible en mlflow.

4. ingrese a la interfaz de mlflow a traves de la direccion http://10.43.101.151:8087/#/models en esta ventanaencontrara listados los modelos generados y vera que ya cuentan con el alias de produccion que permite distinguirlos de los otros modelos.

inserte imagen del mlflow

6. ingresar a la url http://10.43.101.151:8082/ , en esta direccion se encuentra alojada la aplicacion streamlit en la cual se encuentra la siguiente interfaz grafica:

   inserte imagen streamlit

   En esta interfaz puede modificar los datos de prediccion o dejar los ya existentes, una vez ha revisado / modificado los datos para predecir puede hacer clic en el boton "realizar prediccion". El sistema devolvera una estructura Json donde encontrara el nombre del modelo utilizado y el valor predicho como se observa en la imagen:

   inserte imagen del json y el boton
