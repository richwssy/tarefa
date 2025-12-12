CREATE DATABASE Produtoria;

use Produtoria;

CREATE TABLE professores (
    id INT NOT NULL,
    Matricula VARCHAR(50) NOT NULL,
    Nome VARCHAR(100) NOT NULL,
    Disciplina VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);