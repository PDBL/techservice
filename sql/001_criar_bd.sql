DROP DATABASE IF EXISTS techservice_db;

CREATE DATABASE techservice_db
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE techservice_db;

CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(100) NOT NULL UNIQUE,
    nif VARCHAR(20) UNIQUE,
    morada VARCHAR(200),
    status TINYINT NOT NULL DEFAULT 1,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NULL,
    deleted_at DATETIME NULL
)Engine=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE equipamentos (
    id_equipamento INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    numero_serie VARCHAR(100) NOT NULL UNIQUE,
    data_compra DATE,
    observacoes VARCHAR(200),
    status TINYINT NOT NULL DEFAULT 1,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NULL,
    deleted_at DATETIME NULL,
    CONSTRAINT fk_equipamento_cliente FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
)Engine=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE ordens_servico (
    id_ordem INT AUTO_INCREMENT PRIMARY KEY,
    id_equipamento INT NOT NULL,
    data_abertura DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    defeito_relatado VARCHAR(500) NOT NULL,
    diagnostico VARCHAR(500),
    solucao VARCHAR(500),
    status_ordem ENUM('ABERTA', 'EM_ANDAMENTO', 'AGUARDANDO_PECAS', 'CONCLUIDA', 'CANCELADA') NOT NULL DEFAULT 'ABERTA',
    prioridade ENUM('BAIXA', 'MEDIA', 'ALTA') NOT NULL DEFAULT 'MEDIA',
    valor_servico DECIMAL(10,2) DEFAULT 0.00,
    valor_pecas DECIMAL(10,2) DEFAULT 0.00,
    desconto DECIMAL(10,2) DEFAULT 0.00,
    valor_total DECIMAL(10,2) DEFAULT 0.00,
    observacoes VARCHAR(300),
    status TINYINT NOT NULL DEFAULT 1,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NULL,
    deleted_at DATETIME NULL,
    CONSTRAINT fk_ordem_equipamento FOREIGN KEY (id_equipamento) REFERENCES equipamentos(id_equipamento)
)Engine=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE historico_ordens_servico (
    id_historico INT AUTO_INCREMENT PRIMARY KEY,
    id_ordem INT NOT NULL,
    status_anterior VARCHAR(50),
    status_novo VARCHAR(50) NOT NULL,
    observacao VARCHAR(300),
    data_alteracao DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status TINYINT NOT NULL DEFAULT 1,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NULL,
    deleted_at DATETIME NULL,
    CONSTRAINT fk_historico_ordem FOREIGN KEY (id_ordem) REFERENCES ordens_servico(id_ordem)
)Engine=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;