# Pycmic-server - Esquema de base de datos y rutas de API

## Tablas de base de datos

### Tabla usuarios

| Campo       | Tipo      | Descripción                           |
| ----------- | --------- | ------------------------------------- |
| id          | int       | AUTOINCREMENT                         |
| nombre      | varchar   | Nombre tal como viene de la impresora |
| usercode    | int       | Clave, not null, indice.              |
| copias_max  | int       | Número máximo de pasos                |
| copias_used | int       | Número de pasos usados                |
| last_login  | timestamp | Último inicio de sesión               |
| dni         | text      | Usuario en la web del centro          |

### Tabla trazabilidad

| Campo     | Tipo      | Descripción                                   |
| --------- | --------- | --------------------------------------------- |
| id        | int       | AUTOINCREMENT                                 |
| usercode  | int       | Codigo del usuario                            |
| origin    | enum      | CLIENT; WEB; ADMIN                            |
| timestamp | timestamp | Momento de la petición                        |
| copias    | int       | Copias restantes en el momento de la petición |
### Tabla stats

| Campo | Tipo    | Descripción                      |
| ----- | ------- | -------------------------------- |
| clave | varchar | Clave del valor de configuración |
| valor | varchar | Valor de la configuración        |

#### Datos en la tabla de estadísticas.

| Clave         | Valor                                      |
| ------------- | ------------------------------------------ |
| last_check    | timestamp de la última actualización       |
| num_users     | Número de usuarios                         |
| web_access    | Número de accesos desde la API web         |
| client_access | Número de accesos desde la API del cliente |
| bad_requests  | Número de accesos inválidos al sistema     |

## Endpoints de la API

| Ruta                       | Descripción                                 | Perfil      |
| -------------------------- | ------------------------------------------- | ----------- |
| /status                    | Status OK y last update                     | Público     |
| /get_user/\<usercode:int\> | Devolución de un usuario, cuenta como login | WEB, CLIENT |
| /get_users                 | Devolución de todos los usuarios            | ADMIN       |
| /force_update              | Forzar actualización de la BD               | ADMIN       |
| /link_user                 | Enlazar dni y usercode                      | WEB, ADMIN  |
| /get_pasos/\<DNI:string>   | Devuelve los pasos restantes de un correo   | WEB         |

