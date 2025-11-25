from .Agendamento import Agendamento
from .Tarefa import Tarefa
from datetime import datetime

class Compromisso(Agendamento, Tarefa):
    def __init__(self, titulo, descricao=None, data_hora_ini=None, data_hora_fim=None, local=None):
        # Inicializa a parte da Tarefa
        Tarefa.__init__(self, nome_tarefa=titulo, descricao=descricao, data_realizacao=data_hora_ini)
            
        # Inicializa a parte do Agendamento
        Agendamento.__init__(
            self, 
            data_inicio=data_hora_ini, 
            data_final=data_hora_fim, 
            atividades=descricao or "", 
            nome=titulo, 
            local=local
        )

    # 🔹 Implementação do método abstrato de Tarefa
    def definir_termino(self, data_hora_fim: datetime | None = None):
        """
        Define a data/hora de término do compromisso.
        - Se nada for passado, usa o momento atual.
        - Isso é compatível com Tarefa.concluir(), que chama definir_termino() sem argumentos.
        """
        if data_hora_fim is None:
            data_hora_fim = datetime.now()
        self.data_final = data_hora_fim

    def exibir_dados(self):
        """Combina exibir_dados da Tarefa com informações do Agendamento."""
        dados_tarefa = Tarefa.exibir_dados(self)

        inicio = ""
        fim = ""
        if self.data_inicio:
            inicio = self.data_inicio.strftime('%d-%m-%Y %H:%M') if isinstance(self.data_inicio, datetime) else str(self.data_inicio)
        if self.data_final:
            fim = self.data_final.strftime('%d-%m-%Y %H:%M') if isinstance(self.data_final, datetime) else str(self.data_final)

        dados_agendamento = (
            f"Local: {self.local}\n" if self.local else "" +
            (f"Início: {inicio}\n" if inicio else "") +
            (f"Término: {fim}\n" if fim else "")
        )

        return f"--- Compromisso ---\n{dados_tarefa}\n{dados_agendamento}"

    def __str__(self):
        return f"Compromisso: {self.nome} em {self.local if self.local else 'local indefinido'}"
