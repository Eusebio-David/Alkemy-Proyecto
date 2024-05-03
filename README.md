# Alkemy Proyecto

Este es un proyecto basico para un crud. Puede clonar este repositorio para correrlo en tu servidor local, hay errores en cuanto a la forma de listar los productos y proveedores, 
solo puedo hacer uso de modificar, ver y eliminar en los primeros items de la tabla, estoy trabajando para poder solucionarlo. 
Para que los estilos se vean correctamente hay que correrlo en modo producción con DEBUG=True, en el archivo setting.py se puede observar el mismo, tambien estoy trabajando para poder solucionarlo. 
En concreto tiene errores pero no deja de ser un crud básico, y estoy tratando de solucionar todos estos inconvenientes. para correrlo puedes clonar el repositorio:

- crear un entorno virtual, en mi caso use python venv
- installar con pip el requiremnts.txt
- hacer las migraciones necesarias con python manage.py makemigratios, luego python manage.py migrate
- la base de datos ya viene por defecto que es SQLite
- y para finalizar ejecutar el comando python manage.py runserver
