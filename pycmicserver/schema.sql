DROP TABLE IF EXISTS usuarios;
DROP TABLE IF EXISTS trazabilidad;
DROP TABLE IF EXISTS stats;

CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    usercode INTEGER UNIQUE NOT NULL,
    copias_max INTEGER,
    copias_used INTEGER, 
    last_login INTEGER,
    dni TEXT
);

CREATE TABLE trazabilidad (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usercode INTEGER NOT NULL,
    origin TEXT NOT NULL,
    timestamp INTEGER NOT NULL,
    copias INTEGER
);

CREATE TABLE stats (
    clave TEXT NOT NULL,
    valor TEXT
);

CREATE UNIQUE INDEX user_usercode ON usuarios(usercode);

/* Insertar los valores por defecto en la tabla de estadísticas */
INSERT INTO stats VALUES ('last_check', '0');
INSERT INTO stats VALUES ('num_users', '0');
INSERT INTO stats VALUES ('web_access', '0');
INSERT INTO stats VALUES ('client_access', '0');
INSERT INTO stats VALUES ('bad_requests', '0');