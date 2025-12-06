from datetime import datetime, timedelta

STR_FORMATACAO = '%d/%m/%Y %H:%M:%S'
TEMPO_RESULTADO_EXAME = timedelta(days=2)

exame_realizado_em = datetime.now()

data_exame_str = exame_realizado_em.strftime(STR_FORMATACAO)
print(data_exame_str)

# print(TEMPO_RESULTADO_EXAME)

previsao_resultado = exame_realizado_em + TEMPO_RESULTADO_EXAME

# print(previsao_resultado)

previsão_de_entrega_str = previsao_resultado.strftime(STR_FORMATACAO)

print(previsão_de_entrega_str)