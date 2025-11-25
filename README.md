# 📌 Projeto-TOO – Sistema de Tarefas e Agendamentos  
### **Disciplina: Tecnologia Orientada a Objetos (TOO) – BCC | IFSUL**

Este projeto foi desenvolvido para a disciplina **Tecnologia Orientada a Objetos (TOO)** do curso de **Bacharelado em Ciência da Computação – IFSUL – Campus Passo Fundo**.  
Seu objetivo é demonstrar, na prática, a aplicação dos **princípios fundamentais de Programação Orientada a Objetos em Python**, incluindo:

- Abstração  
- Encapsulamento  
- Herança (simples e múltipla)  
- Polimorfismo  
- Classes abstratas  
- Uso de propriedades (`@property`)  
- Enumerações  
- Modularização  
- Padrões de criação (Factory Method)

O sistema implementado permite manipular diferentes tipos de **tarefas**, **agendamentos** e **compromissos**, simulando diversos cenários práticos dentro da POO.

---

# 📂 Estrutura do Projeto

Conforme a estrutura real do repositório:


---

# 🎯 Objetivos do Sistema

O projeto implementa um sistema de gerenciamento de tarefas, subdivididas em:

- **Tarefas pessoais**  
- **Tarefas profissionais**  
- **Tarefas escolares**  
- **Tarefas gamer**  
- **Agendamentos**  
- **Compromissos** (herança múltipla: Tarefa + Agendamento)

Os arquivos de teste demonstram o funcionamento de cada parte.

---

# 🧱 Principais Conceitos de POO Aplicados

### ✔️ 1. **Classe Abstrata**
A classe `Tarefa` é abstrata e define métodos obrigatórios:

- `exibir_dados()`
- `definir_termino()`

Isso garante que TODAS as subclasses implementem sua própria versão.

---

### ✔️ 2. **Herança**
- `TarefaEscolar`, `TarefaProfissional`, `TarefaGamer` e `TarefaPessoal` herdam de `Tarefa`.
- `Compromisso` herda **simultaneamente** de `Agendamento` e `Tarefa`.

---

### ✔️ 3. **Polimorfismo**
Cada subclasse implementa sua própria versão de:

- `exibir_dados()`
- `definir_termino()` (quando aplicável)

---

### ✔️ 4. **Encapsulamento**
Uso consistente de:

```python
@property
def atributo(self): ...

@atributo.setter
def atributo(self, valor): ...
```
---

### ✔️ 5. **Enumerações (Enum)**
Utilizado em:

- `StatusTarefa`
- `TipoTarefaPessoal` 
- `DificuldadeJogo`

Para garantir valores válidos e evitar strings soltas no código.

---

### ✔️ 6. **Factory Method**

`TarefaFactory.py` implementa um criador de tarefas baseado em:
```
TarefaFactory.criar_tarefa(tipo_tarefa="pessoal", ...)
```
Uma forma muito comum e importante de abstrair a criação de objetos.

--- 