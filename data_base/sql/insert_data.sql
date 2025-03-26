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

1T2023
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

-- SELECT * FROM demonstracoes_contabeis;

-- SELECT *
-- FROM demonstracoes_contabeis
-- ORDER BY data DESC
-- LIMIT 10;








