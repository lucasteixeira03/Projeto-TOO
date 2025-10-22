from datetime import datetime
from .Tarefa import Tarefa

class TarefaProfissional(Tarefa):
    def __init__(self, nome_tarefa, projeto, data_entrega, descricao = None, data_realizacao = None):
        super().__init__(nome_tarefa, descricao, data_realizacao)
        self.projeto = projeto
        self.data_entrega = data_entrega


    def __str__(self):
        return f"[Tarefa Profissional] {super().__str__()}"

    @property
    def projeto(self):
        return self.__projeto
    
    def projeto(self, projeto):
        if not projeto or not str(projeto).strip():
            raise ValueError("Projeto é obrigatório em TarefaProfissional.")
        self.__projeto = str(projeto).strip().title()

    @property
    def data_entrega(self):
        return self.__data_entrega
    
    @data_entrega.setter
    def data_entrega(self, data):
        self.__data_entrega = None 
        if data is not None:
            try:
                self.__data_entrega = datetime.strptime(data, "%d-%m-%Y")
            except ValueError as e:
                print(f"Data em formato inválido: {e}")

    def exibir_dados(self):
        base = super().exibir_dados()
        data_entrega = self.data_entrega.strftime("%d-%m-%Y") if self.data_entrega else "Sem data definida"
        projeto = self.projeto if self.projeto else "Sem projeto definido"
        return f"{base}\n Projeto: {projeto}\n Data Entrega: {data_entrega}"