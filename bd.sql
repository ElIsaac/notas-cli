CREATE DATABASE IF NOT EXISTS proyecto_py;
use proyecto_py

CREATE TABLE IF NOT EXISTS usuarios(
    id          int(50) auto_increment not null,
    nombre      varchar(100),
    apellidos   varchar(255),
    email       varchar(255) not null,
    password    varchar(255) not null,
    fecha       date not null,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)

)ENGINE = InnoDb;

CREATE TABLE IF NOT EXISTS notas(
    id          int(255) auto_increment not null,
    usuario_id  int(50)                 not null,
    titulo      varchar(255),
    descripcion MEDIUMTEXT,
    fecha       date                    not null,
    CONSTRAINT pk_notas PRIMARY KEY(id),
    CONSTRAINT fk_notas_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)ENGINE=InnoDb;