CREATE DATABASE IF NOT EXISTS projeto_teste;
USE projeto_teste;

show DATABASES;

CREATE TABLE eleitores (
	id INT PRIMARY KEY,
    chave_acesso VARCHAR(200) NOT NULL,
    nome_completo VARCHAR(50) NOT NULL,
    titulo_eleitor VARCHAR(12) NOT NULL,
    cpf_criptografado VARCHAR(30) NOT NULL,
    mesario BOOLEAN NOT NULL,
    status_voto BOOLEAN NOT NULL
);

CREATE TABLE candidatos (
	id INT PRIMARY KEY,
    nome_completo VARCHAR(50) NOT NULL,
    numero_votacao INT NOT NULL,
    nome_partido VARCHAR(20)
);

CREATE TABLE registro_logs (
	id_log INT PRIMARY KEY,
    data_hora_log DATETIME NOT NULL,
    tipo VARCHAR(15) NOT NULL,
    descricao VARCHAR(50)
);

CREATE TABLE tabela_votos (
	id_voto INT PRIMARY KEY,
    id_eleitor INT NOT NULL,
    id_candidato INT NOT NULL,
    data_hora_voto INT NOT NULL,
    protocolo_criptografado VARCHAR(30) NOT NULL
);

show TABLES from projeto_teste;
select * from  tabela_votos;
