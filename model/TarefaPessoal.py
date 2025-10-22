from .Tarefa import Tarefa

class TarefaPessoal(Tarefa):
    def __init__(self, nome_tarefa, tipo, descricao=None, data_realizacao=None):
        super().__init__(nome_tarefa, descricao=descricao, data_realizacao=data_realizacao)
        self.tipo = tipo

    def __str__(self):
        return f"[Tarefa Pessoal] {super().__str__()}"

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        if not tipo or not str(tipo).strip():
            raise ValueError("Tipo é obrigatório (ex.: Saúde, Lazer, Doméstica...).")
        self.__tipo = str(tipo).strip().title()

    def exibir_dados(self):
        base = super().exibir_dados()
        return f"{base}\n Tipo: {self.tipo}"