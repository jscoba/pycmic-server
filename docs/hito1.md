# Pycmic-server - Documentación Hito 1

En este proyecto vamos a usar las siguientes herramientas:

- Flask como framework para crear la API
- Pytest como herramienta de testing de la aplicación
- Make como herramienta de ejecución y gestor de tareas
- pip como herramienta de instalación de dependencias.

Además vamos a usar los servicios Travis y CircleCI para ejecutar las pruebas de integración continua a cada commit que hagamos en el repositorio.

La estructura del proyecto es la siguiente:

```bash
.
├── docs #Documentación del proyecto
│
├── instance #Carpeta local donde se guarda la base de datos de la instancia
│   └── pycmic_server.sqlite
├── LICENSE #Licencia del proyecto
├── Makefile #Herramienta de construcción
├── pycmicserver #Paquete principal
│   ├── db.py
│   ├── __init__.py
│   ├── pycmicinterface #Librería de control de la impresora
│   └── schema.sql
├── README.md
├── requirements.txt #Dependencias de la aplicación
└── tests #Localización de los ficheros de testing
```

