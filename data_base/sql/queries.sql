SELECT 
    oa.registro_ans,
    oa.razao_social,
    SUM(ABS(vl_saldo_final::DECIMAL - vl_saldo_inicial::DECIMAL)) AS total_despesas
FROM 
    demonstracoes_contabeis dc
JOIN 
    operadoras_ativas oa ON dc.registro_ans = oa.registro_ans
WHERE 
    dc.descricao LIKE '%EVENTOS%SINISTROS%CONHECIDOS OU AVISADOS%ASSISTÊNCIA A SAÚDE%MEDICO HOSPITALAR%'
    AND dc.data BETWEEN '2024-10-01' AND '2024-12-31'
GROUP BY 
    oa.registro_ans, oa.razao_social
ORDER BY 
    total_despesas DESC
LIMIT 10;