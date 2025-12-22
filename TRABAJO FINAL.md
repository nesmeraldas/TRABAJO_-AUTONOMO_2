# TRABAJO FINAL

El presente trabajo final tiene como objetivo reunir y aplicar los conocimientos adquiridos durante el módulo. Para muchos de nosotros, la programación era un tema nuevo que al inicio generaba cierto temor; sin embargo, con el avance de las clases pudimos comprender mejor cómo se crea, organiza, ejecuta y mejora un programa.

Nuestro aprendizaje se enfocó en Python, un lenguaje de programación ampliamente utilizado por su facilidad y versatilidad.

En las siguientes secciones explicaremos de manera ordenada cómo desarrollamos cada etapa del proyecto y cómo este proceso nos llevó al resultado que presentamos en este informe.

-DISEÑO DEL PROYECTO

Inicialmente se nos solicitó diseñar el proyecto utilizando diagramas de flujo o diagramas de funcionalidad. Estos recursos, basados en el tema seleccionado, nos permitieron representar de forma teórica cómo esperábamos que se comportara nuestro programa. En mi caso, opté por presentar el proyecto mediante un diagrama de flujo, ya que es una de las herramientas con las que me siento más familiarizado y que me permitió estructurar mejor el proceso lógico del sistema.
<img width="1140" height="657" alt="image" src="https://github.com/user-attachments/assets/84597ae8-a0bb-49b9-864f-40e75ad9dffa" />
En la imagen presentada se evidencia la forma en la que deseaba que se ejecutara el programa. El diseño del diagrama muestra una interfaz que primero solicita al usuario seleccionar si desea generar una contraseña simple o compleja. Posteriormente, el sistema pide ingresar la cantidad de caracteres. Una vez definidas estas variables, el programa ejecuta el proceso correspondiente y finalmente genera la contraseña.

-EJECUCIÓN DEL PROGRAMA

Luego de elaborar el diseño inicial mediante diagramas de flujo, se procedió a trasladar dicha estructura al programa Raptor, una herramienta que permite representar visualmente la lógica de un algoritmo y, además, ejecutarlo para comprobar su comportamiento. En Raptor se construyó la estructura lógica del programa utilizando los recursos que la aplicación ofrece, tales como asignación de entradas, declaración de variables, incorporación de procesos lógicos y uso de bucles. Gracias a esta representación, fue posible simular el funcionamiento del programa y validar su lógica antes de implementarlo mediante líneas de código en Python.

<img width="777" height="893" alt="image" src="https://github.com/user-attachments/assets/07fa1be5-321a-4321-93c9-b4dd079e8f9a" />
<img width="685" height="880" alt="image" src="https://github.com/user-attachments/assets/52edd2ff-2656-4d0b-bf07-826037cfb8b6" />

-PROGRAMACION EN PYTHON

Una vez finalizados todos los pasos previos, procedimos a iniciar con la programación de nuestro proyecto en Python. Gracias al conocimiento adquirido durante el proceso, fue posible desarrollar y ejecutar el programa de manera satisfactoria.

Para permitir la generación aleatoria de la contraseña, fue necesario importar las librerías correspondientes. Asimismo, aplicando los conceptos aprendidos, declaramos las variables esenciales que garantizan el correcto funcionamiento de esta primera versión del programa.

Tras ejecutar el código, pudimos comprobar que el programa cumple con el objetivo planteado, generando contraseñas de acuerdo con los parámetros establecidos por el usuario.

A continuación, se anexan imágenes del código implementado y de cómo este fue interpretado durante su ejecución en la terminal.

<img width="1247" height="624" alt="image" src="https://github.com/user-attachments/assets/89ac5a5e-b617-42f4-81d3-912368d209ec" />

Como se menciono antes se importo librerias que nos permitan ejecutar la programacion de manera exitosa

<img width="1648" height="935" alt="image" src="https://github.com/user-attachments/assets/7b1119d8-272a-4848-ab3c-78d817e03908" />

En la segunda imagen se puede observar como se declararon las variables y en la termonal se puede observar el programa ya ejecutado de manera exitosa

-VERSION MEJORADA DEL PROYECTO (USO DE FUNCIONES, LISTA, TUPLAS O DICCIONARIOS)
En esta última etapa del proyecto se procedió a optimizar el código previamente desarrollado, incorporando funciones, listas y un validador de seguridad para fortalecer la estructura del programa. Estas mejoras permiten simplificar las líneas de código, incrementar la modularidad y garantizar un funcionamiento más robusto y escalable.

Uno de los principales cambios fue la implementación de funciones, lo cual facilita dividir el programa en bloques lógicos, cada uno encargado de una tarea específica. Esto mejora la legibilidad, reutilización del código y organización general del programa. Entre las funciones implementadas se incluyen:

Una función para seleccionar el tipo de contraseña.

Una función responsable de generar la contraseña según los parámetros ingresados.

Un validador encargado de comprobar el nivel de seguridad de la contraseña generada.

Adicionalmente, se incorporó una lista como repositorio en donde se almacenan todas las contraseñas generadas durante la ejecución del programa. Esto permite llevar un registro interno y visualizar el historial cuando sea necesario. Esta estructura de datos brinda flexibilidad para futuras ampliaciones, como exportar las contraseñas o aplicar filtros.

Finalmente, el código se reorganizó para hacerlo más claro y eficiente, reduciendo redundancias presentes en la versión inicial. Las nuevas funciones y el repositorio permiten que la lógica principal del programa sea más sencilla y directa, potenciando la funcionalidad general del sistema.

-DICCIONARIO
En el codigo se anadio el diccionaro CHARSETS, este cambio nos permite simplificar las lineas de codigo ya que no tenemos que usar el IF de manera redundante para elegir los caracteres

<img width="1011" height="149" alt="image" src="https://github.com/user-attachments/assets/5a7b991f-db07-4c21-93b1-73407caab04f" />

-FUNCIONES
También se añadió las funciones solicitar_tipo(), solicitar_longitud las cuales permite interpretar de manera más precisa la petición del usuario respecto al tipo de contraseña y la longitud que desea generar. Gracias a esta función, el programa puede validar la opción ingresada, asegurarse de que sea correcta y devolver el valor adecuado para continuar con el proceso. Esto mejora la interacción con el usuario y evita errores durante la selección del tipo de contraseña y la lomgitud de la misma

<img width="879" height="611" alt="image" src="https://github.com/user-attachments/assets/bfefb4cf-5df6-4044-b7ec-96be4d77d6f4" />

Las funciones mencionadas anteriormente permiten que el programa tenga una ejecución más organizada y simplificada. Además, se incorporaron nuevas funciones que vuelven al sistema más robusto y agregan características adicionales que mejoran la experiencia del usuario.

Entre las funciones implementadas se encuentran: evaluar_seguridad(password), mostrar_historial(historial) y la función principal main(), las cuales amplían las capacidades del programa y facilitan su uso de manera más eficiente.

<img width="871" height="686" alt="image" src="https://github.com/user-attachments/assets/ece7ba53-079c-4164-a505-28c681c0e5b1" />

<img width="1198" height="829" alt="image" src="https://github.com/user-attachments/assets/00785ba7-8e15-4fb7-ab85-2c34ea8e8a3f" />

<img width="1075" height="952" alt="image" src="https://github.com/user-attachments/assets/45e08950-d77f-4ca7-b54a-561aefdeb36b" />

Para finalizar, podemos señalar que realizar este proyecto de manera estructurada y siguiendo cada uno de los pasos descritos nos permitió comprender de forma más sólida el mundo de la programación y su amplio campo de aplicación. Los conocimientos adquiridos en este módulo representan el inicio de nuestra formación, y depende de nosotros aplicarlos, fortalecerlos y desarrollarlos con profesionalismo y ética.









