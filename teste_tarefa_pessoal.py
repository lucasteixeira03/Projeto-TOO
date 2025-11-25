from model.TarefaPessoal import TarefaPessoal
from model.TipoTarefaPessoal import TipoTarefaPessoal

t = TarefaPessoal("Limpar casa, lavar roupa e cozinhar", tipo=TipoTarefaPessoal.FAMILIA,
                  descricao="Tarefas de casa para o final de semana")
print(t)
t.concluir()
print(t.exibir_dados())