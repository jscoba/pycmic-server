INSERT INTO usuarios (nombre, usercode, copias_max, copias_used, last_login) VALUES ('TEST_USER', 12345678, 1500, 1000, DATE('now'));
INSERT INTO usuarios (nombre, usercode, copias_max, copias_used, last_login) VALUES ('TEST2', 987654321 , 1000, 1000, DATE('now'));

INSERT INTO trazabilidad (usercode, origin, timestamp, copias) VALUES (12345678, 'CLIENT', DATE('2020-02-01 12:00:00'), 600);
INSERT INTO trazabilidad (usercode, origin, timestamp, copias) VALUES (12345678, 'CLIENT', DATE('2020-02-01 18:00:00'), 500);