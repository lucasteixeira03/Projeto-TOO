from model.TarefaPessoal import TarefaPessoal
from model.TipoTarefaPessoal import TipoTarefaPessoal
print("\n### TAREFA PESSOAL ###")
tp = TarefaPessoal("Jogar Counter-Strike", tipo=TipoTarefaPessoal.LAZER,
                   descricao="Desestressar")
print(tp.exibir_dados())

tp.iniciarTarefa()
tp.concluir()
print("\nDepois de concluir:")
print(tp.exibir_dados())
