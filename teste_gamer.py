from model.TarefaGamer import TarefaGamer
from datetime import datetime

a = TarefaGamer(
    nome_tarefa="Zerar Elden Ring",
    jogo="Elden Ring",
    nivel=50,
    descricao="Finalizar o último chefe",
    data_limite="25-10-2025"
)

print(a)
print(a.exibir_dados())