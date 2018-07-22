# todolisto_Django
## Integrantes

* Israel Jasma
* Christopher Patirro

## Respecto a los requerimientos:

### Es necesario tener instalar:

* Framework Django en su version 2.0
* XAMPP en su version 3.2.2
* Python 3

### Sistema Operativo:

* Windows 10
### Respecto a la instalacion:

* Se debe instalar el framework Django

* pip install django

* Es necesario instalar un cliente MySQL para usar la BD desde Python:

* pip install mysqlclient

### Respecto a la ejecucion:

* Iniciar, en XAMPP, los siguiente modulos:

    * 'Apache'
    * 'MySQL'

* source activate todolisto cd todolisto python manage.py runserver

* Se debe crear obligatoriamente un usuario con username: 'admin', quien será el administrador del sistema


### Respecto a los modelos:

* El sistema cuenta con tres modelos:
    * Tarea
    * EstadoTarea
    * TipoTarea

### Respecto a la base de datos:

* Debe crear una base de datos denomidada 'todolisto'. Para esto es necesario aplicar los siguientes comandos en la consola (shell) de XAMPP:

> mysql -u root -p CREATE DATABASE todolisto; CREATE USER ‘todo’@’%’ IDENTIFIED BY ‘listo’; GRANT ALL PRIVILEGES ON todolisto.* TO ‘todo’@’%’; FLUSH PRIVILEGES;

* Es necesario ingresar los nombres de los host y la cuenta de usuario por defecto con la contraseña en el archivo 'php.ini' (C:\xampp\php), en el nivel siguiente:

> ; Default host for mysql_connect() (doesn't apply in safe mode). ; http://php.net/mysqli.default-host mysqli.default_host='localhost'

> ; Default user for mysql_connect() (doesn't apply in safe mode). ; http://php.net/mysqli.default-user mysqli.default_user='todo'

> ; Default password for mysqli_connect() (doesn't apply in safe mode). ; Note that this is generally a bad idea to store passwords in this file. ; Any user with PHP access can run 'echo get_cfg_var("mysqli.default_pw") ; and reveal this password! And of course, any users with read access to this ; file will be able to reveal the password as well. ; http://php.net/mysqli.default-pw mysqli.default_pw='listo'