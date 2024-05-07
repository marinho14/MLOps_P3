# MLOps_P3 Video

[![Texto alternativo](https://img.youtube.com/vi/YPbuRMIL1H8/0.jpg)](https://www.youtube.com/watch?v=YPbuRMIL1H8)

# MLOps_P3 readme
1. Posterior a activar la VPN de la univeridad, conectese a la maquina virtual con las credenciales del grupo 2.
2. por favor ubicarse sobre el directorio del proyecto 3 con el comando
   ```url
	cd /home/estudiante/MLOps_P3
3. una vez alli ejecutar el comando:  
	```url
	docker compose up
4. ingresar a la url:
    ```url
    http://10.43.101.151:8086/login
	```
5. ingresar las siguientes credenciales en la ventana de inicio de sesion <br />
	Usuario: admin <br />
	Password: supersecret <br />
	![alt text](https://github.com/marinho14/MLops_P2/blob/main/images/minio_0.png)
6. En caso de no existir, cree un nuevo bucket llamado mlflow
	![alt text](https://github.com/marinho14/MLops_P2/blob/main/images/minio_1.png)
    ![alt text](https://github.com/marinho14/MLops_P2/blob/main/images/minio_2.png)
    ![alt text](https://github.com/marinho14/MLops_P2/blob/main/images/minio_3.png)
7. ingresar a la url:
    ```url
    http://10.43.101.151:8080/
	```
	Ingresar las siguientes credenciales en la ventana de inicio de sesion <br />
	Usuario: airflow <br />
	Password: airflow <br />
	![alt text](https://github.com/marinho14/MLops_P2/blob/main/images/airflow_0.png) <br />

8. Haga clic en el boton que dispara el DAG, si lo desea puede seguir el desarrollo de la ejecucion haciendo clic en la celda last run que ahora tiene la fecha actual del ultimo run enviado.

   inserte imagen del airflow con el boton del dag encerrado

Una vez esta ejecucion termine con las 3 cajas del grafo en status success el modelo estara disponible en mlflow.
9. Ingresar a la url:
    ```url
    http://10.43.101.151:8087/
	```
	Ingrese a la interfaz de mlflow a traves de la direccion http://10.43.101.151:8087/#/models en esta ventana encontrara listados los modelos generados y vera que ya cuentan con el alias de produccion que permite distinguirlos de los otros modelos. <br />
 En caso de no tener modelos registrados, el procedimiento es el siguiente:
 
10. ingresar a la url http://10.43.101.151:8082/ , en esta direccion se encuentra alojada la aplicacion streamlit en la cual se encuentra la siguiente interfaz grafica:

   inserte imagen streamlit

   En esta interfaz puede modificar los datos de prediccion o dejar los ya existentes, una vez ha revisado / modificado los datos para predecir puede hacer clic en el boton "realizar prediccion". El sistema devolvera una estructura Json donde encontrara el nombre del modelo utilizado y el valor predicho como se observa en la imagen:

   inserte imagen del json y el boton
