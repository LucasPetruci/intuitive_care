COPY operadoras_ativas(
  registro_ans,
  cnpj,
  razao_social,
  nome_fantasia,
  modalidade,
  logradouro,
  numero,
  complemento,
  bairro,
  cidade,
  uf,
  cep,
  ddd,
  telefone,
  fax,
  endereco_eletronico,
  representante,
  cargo_representante,
  regiao_comercializacao,
  data_registro_ans
)
FROM '/var/lib/postgresql/data/Relatorio_cadop.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

-- SELECT * FROM operadoras_ativas;

-- 1T2023
COPY demonstracoes_contabeis(
  data,
  registro_ans,
  cd_conta_contabil,
  descricao,
  vl_saldo_inicial,
  vl_saldo_final
)
FROM '/var/lib/postgresql/data/1T2023.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

-- 2t2023
COPY demonstracoes_contabeis(
  data,
  registro_ans,
  cd_conta_contabil,
  descricao,
  vl_saldo_inicial,
  vl_saldo_final
)
FROM '/var/lib/postgresql/data/2t2023.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

-- 3T2023
COPY demonstracoes_contabeis(
  data,
  registro_ans,
  cd_conta_contabil,
  descricao,
  vl_saldo_inicial,
  vl_saldo_final
)
FROM '/var/lib/postgresql/data/3T2023.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

-- 4T2023
COPY demonstracoes_contabeis(
  data,
  registro_ans,
  cd_conta_contabil,
  descricao,
  vl_saldo_inicial,
  vl_saldo_final
)
FROM '/var/lib/postgresql/data/4T2023.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

--This select is for unformat data in csv, are using DD/MM/YYYY
-- SELECT *
-- FROM demonstracoes_contabeis
-- WHERE data LIKE '__/__/____';

--Update data to YYYY-MM-DD
UPDATE demonstracoes_contabeis
SET data = TO_CHAR(TO_DATE(data, 'DD/MM/YYYY'), 'YYYY-MM-DD')
WHERE data LIKE '__/__/____';

--Finally convert data to DATE
ALTER TABLE demonstracoes_contabeis
ALTER COLUMN data TYPE DATE
USING TO_DATE(data, 'YYYY-MM-DD');


--1T2024
COPY demonstracoes_contabeis(
    data,
    registro_ans,
    cd_conta_contabil,
    descricao,
    vl_saldo_inicial,
    vl_saldo_final
)
FROM '/var/lib/postgresql/data/1T2024.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

--2T2024
COPY demonstracoes_contabeis(
    data,
    registro_ans,
    cd_conta_contabil,
    descricao,
    vl_saldo_inicial,
    vl_saldo_final
)
FROM '/var/lib/postgresql/data/2T2024.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

--3T2024
COPY demonstracoes_contabeis(
    data,
    registro_ans,
    cd_conta_contabil,
    descricao,
    vl_saldo_inicial,
    vl_saldo_final
)
FROM '/var/lib/postgresql/data/3T2024.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

--4T2024
COPY demonstracoes_contabeis(
    data,
    registro_ans,
    cd_conta_contabil,
    descricao,
    vl_saldo_inicial,
    vl_saldo_final
)
FROM '/var/lib/postgresql/data/4T2024.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

-- SELECT * FROM demonstracoes_contabeis;

-- SELECT *
-- FROM demonstracoes_contabeis
-- ORDER BY data DESC
-- LIMIT 10;