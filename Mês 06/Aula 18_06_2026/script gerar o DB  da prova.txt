-- 1. Criação do Banco de Dados
CREATE DATABASE IF NOT EXISTS avaliacao_sql;
USE avaliacao_sql;

-- 2. Limpeza prévia das tabelas (para permitir reexecução do script)
DROP TABLE IF EXISTS livros;
DROP TABLE IF EXISTS produtos;
DROP TABLE IF EXISTS equipe;
DROP TABLE IF EXISTS categorias;
DROP TABLE IF EXISTS clientes;
DROP TABLE IF EXISTS cursos;

-- ==========================================
-- CRIAÇÃO E POPULAÇÃO DAS TABELAS
-- ==========================================

-- Tabela para as Questões 1 e 8 (Clientes)
CREATE TABLE clientes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    cidade VARCHAR(50),
    data_cadastro DATE
);

INSERT INTO clientes (nome, email, telefone, cidade, data_cadastro) VALUES
('Carlos Silva', 'carlos@email.com', '(41) 99999-1111', 'Curitiba', '2026-01-15'),
('Ana Souza', 'ana.souza@email.com', '(11) 98888-2222', 'São Paulo', '2026-02-20'),
('Marcos Santos', 'marcos@email.com', '(21) 97777-3333', 'Rio de Janeiro', '2026-03-05'),
('Juliana Lima', 'ju.lima@email.com', '(11) 96666-4444', 'São Paulo', '2026-03-12');

-- Tabela para as Questões 2, 7 e 9 (Produtos)
CREATE TABLE produtos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    estoque INT NOT NULL,
    categoria_id INT
);

INSERT INTO produtos (nome, preco, estoque, categoria_id) VALUES
('Teclado Mecânico', 180.00, 15, 5),
('Mouse Gamer', 120.00, 0, 5), -- Esgotado (Q7)
('Monitor 24 polegadas', 850.00, 8, 5),
('Cabo HDMI 2m', 30.00, 50, 2),
('Headset Wireless', 350.00, 12, 5);

-- Tabela para a Questão 4 (Equipe/Funcionários)
CREATE TABLE equipe (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    cargo VARCHAR(50),
    salario DECIMAL(10,2) NOT NULL
);

INSERT INTO equipe (nome, cargo, salario) VALUES
('Fernando Almeida', 'Desenvolvedor Pleno', 5500.00),
('Beatriz Costa', 'Tech Lead', 9200.00),
('Rodrigo Pires', 'Estagiário QA', 1800.00),
('Camila Rocha', 'Analista de Sistemas', 6200.00);

-- Tabela para a Questão 5 (Categorias)
CREATE TABLE categorias (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome_categoria VARCHAR(50) NOT NULL
);

INSERT INTO categorias (nome_categoria) VALUES
('Sistemas Operacionais'),
('Cabos e Conectores'),
('Componentes de Hardware');

-- Tabela para a Questão 10 (Livros)
CREATE TABLE livros (
    id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(100) NOT NULL,
    autor VARCHAR(100) NULL, -- Aceita NULL para validar a Q10
    ano INT
);

-- Inserindo alguns dados iniciais padrão
INSERT INTO livros (titulo, autor, ano) VALUES
('O Cortiço', 'Aluísio Azevedo', 1890),
('Memórias Póstumas de Brás Cubas', 'Machado de Assis', 1881);

-- A tabela "cursos" da Questão 6 não foi populada previamente 
-- de propósito para que o comando CREATE TABLE seja testado do zero.