-- DROP TABLE IF EXISTS demonstracoes_contabeis;
-- DROP TABLE IF EXISTS operadoras_ativas;
CREATE TABLE operadoras_ativas (
    id SERIAL PRIMARY KEY,
    registro_ans VARCHAR(6) UNIQUE,
    cnpj VARCHAR(14) UNIQUE,
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(50),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(100),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf VARCHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(3),
    telefone VARCHAR(20),
    fax VARCHAR(15),
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(255),
    cargo_representante VARCHAR(100),
    regiao_comercializacao VARCHAR(100),
    data_registro_ans DATE
);

--set saldo_inicial and saldo_final to TEXT bc in csv file is using "," as decimal separator. Convert to numeric later after import
CREATE TABLE demonstracoes_contabeis (
    id SERIAL PRIMARY KEY,
    data DATE,
    registro_ans VARCHAR(20) NOT NULL,
    cd_conta_contabil VARCHAR(20),
    descricao TEXT,
    vl_saldo_inicial TEXT,
    vl_saldo_final TEXT
);

