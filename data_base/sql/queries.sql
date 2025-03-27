-- Query 1
--TODO: ADD Date filter
SELECT 
    oa.registro_ans,
    oa.razao_social,
    SUM(dc.vl_saldo_final::DECIMAL) AS total_despesas
FROM 
    demonstracoes_contabeis dc
JOIN 
    operadoras_ativas oa ON dc.registro_ans = oa.registro_ans
WHERE 
    dc.descricao LIKE '%EVENTOS%SINISTROS%CONHECIDOS OU AVISADOS%ASSISTÊNCIA A SAÚDE%MEDICO HOSPITALAR%'
GROUP BY 
    oa.registro_ans, oa.razao_social
ORDER BY 
    total_despesas DESC
LIMIT 10;