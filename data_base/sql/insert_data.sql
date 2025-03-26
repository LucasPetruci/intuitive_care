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









