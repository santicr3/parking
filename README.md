# Detector de matriculas
### Santi y David

## Gestión de IA

### Captura de imagen
#### Opencv

### Detección matrículas
#### YOLO

## Base de datos

### MySQL

#### Tablas
Coche:

|  id  |  matricula  | id_usuario |h_entrada | h_salida  | pagado |
|------|-------------|------------|----------|-----------|--------|
| int  | varchar(12) |     int    |timestamp | timestamp |  bool  |

Usuario:

|  id  |    nombre   |    dni    |   pagado   |
|------|-------------|-----------|------------|
| int  | varchar(12) | string(9) | timestamp  |
|||unique||

## Backend

### Flask

#### Endpoints

/coche_entra -> Se escanea la matricula e introducen los datos en la BBDD
/coche_sale -> Se escanea la matricula y actualizan los datos en la BBDD
/pago -> Se realiza el pago

## Frontend

### Flet
