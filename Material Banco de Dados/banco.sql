-- ============================================================
-- BANCO DE DADOS: LOCADORA DE CARROS
-- Arquivo: banco.sql
-- Execute este script no MySQL Workbench antes de rodar o app
-- ============================================================

-- Cria o banco se não existir e o seleciona
CREATE DATABASE IF NOT EXISTS locadora_carros
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE locadora_carros;

-- ============================================================
-- TABELA 1: cliente (locatário)
-- Armazena os dados de quem vai alugar o veículo
-- ============================================================
CREATE TABLE IF NOT EXISTS cliente (
    id          INT          AUTO_INCREMENT PRIMARY KEY,
    nome        VARCHAR(100) NOT NULL,
    cpf         VARCHAR(14)  NOT NULL UNIQUE,   -- formato: 000.000.000-00
    telefone    VARCHAR(15),
    email       VARCHAR(100),
    cnh         VARCHAR(20)  NOT NULL,           -- número da habilitação
    data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- TABELA 2: veiculo (veículos de passeio disponíveis)
-- ============================================================
CREATE TABLE IF NOT EXISTS veiculo (
    id          INT          AUTO_INCREMENT PRIMARY KEY,
    marca       VARCHAR(50)  NOT NULL,
    modelo      VARCHAR(50)  NOT NULL,
    ano         YEAR         NOT NULL,
    placa       VARCHAR(8)   NOT NULL UNIQUE,    -- formato: ABC-1234 ou ABC1D23
    cor         VARCHAR(30),
    diaria      DECIMAL(8,2) NOT NULL,           -- valor por dia em R$
    disponivel  TINYINT(1)   DEFAULT 1           -- 1 = disponível, 0 = alugado
);

-- ============================================================
-- TABELA 3: aluguel (relaciona cliente e veículo)
-- ============================================================
CREATE TABLE IF NOT EXISTS aluguel (
    id              INT         AUTO_INCREMENT PRIMARY KEY,
    cliente_id      INT         NOT NULL,
    veiculo_id      INT         NOT NULL,
    data_retirada   DATE        NOT NULL,
    data_devolucao  DATE        NOT NULL,
    valor_total     DECIMAL(10,2),              -- calculado automaticamente
    status          ENUM('ativo','encerrado','cancelado') DEFAULT 'ativo',
    -- Chaves estrangeiras garantem integridade referencial
    FOREIGN KEY (cliente_id) REFERENCES cliente(id),
    FOREIGN KEY (veiculo_id) REFERENCES veiculo(id)
);

-- ============================================================
-- DADOS DE EXEMPLO
-- ============================================================
INSERT INTO cliente (nome, cpf, telefone, email, cnh) VALUES
('Ana Paula Silva',  '111.222.333-44', '(44) 99001-0001', 'ana@email.com',  'CNH-00001'),
('Bruno Costa',      '222.333.444-55', '(44) 99001-0002', 'bruno@email.com','CNH-00002'),
('Carla Mendes',     '333.444.555-66', '(44) 99001-0003', 'carla@email.com','CNH-00003');

INSERT INTO veiculo (marca, modelo, ano, placa, cor, diaria) VALUES
('Fiat',       'Argo',     2022, 'ABC-1234', 'Prata',  120.00),
('Chevrolet',  'Onix',     2023, 'DEF-5678', 'Branco', 130.00),
('Volkswagen', 'Polo',     2021, 'GHI-9012', 'Preto',  140.00);

INSERT INTO aluguel (cliente_id, veiculo_id, data_retirada, data_devolucao, valor_total, status) VALUES
(1, 1, '2026-06-10', '2026-06-13', 360.00, 'ativo'),
(2, 2, '2026-06-08', '2026-06-10', 260.00, 'encerrado');

-- ============================================================
-- FIM DO SCRIPT
-- ============================================================
