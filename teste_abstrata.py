from model.Tarefa import Tarefa

# ESTE ARQUIVO SERVE APENAS PARA MOSTRAR QUE TAREFA É ABSTRATA:
# Ao tentar instanciar, deve ocorrer TypeError.

t1 = Tarefa("Aula TOO", "teste")
print(t1.exibir_dados())
t1.concluir()
print(t1.exibir_dados())