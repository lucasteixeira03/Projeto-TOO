from model.TarefaGamer import TarefaGamer
from model.DificuldadeJogo import DificuldadeJogo

print(" ### TAREFA GAMER ### ")
tg = TarefaGamer("Fazer 5 gols no Neuer", tipo="Desafio", jogo="FIFA 2025",
                 dificuldade=DificuldadeJogo.INSANO)
print(tg.exibir_dados())

tg.iniciarTarefa()
tg.concluir()
print("\nDepois de concluir:")
print(tg.exibir_dados())