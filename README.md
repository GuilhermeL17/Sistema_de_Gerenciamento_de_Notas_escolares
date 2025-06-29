### **Integrantes**
Guilherme Lacerda Ricardo - RGM:38878577

Davi Sobral Cavalcante Lacerda - RGM:38708761

Cauã Eduardo Silva de Carvalho Mendes - RGM: 36923303

Maira Priscila Faustino Dias Chaves - RGM: 38721503

Jéssica Soares Dias - RGM: 37885715


---

## **Briefing do Projeto: Sistema de Gerenciamento de Notas Escolares**

---

### **Objetivo Geral**

Desenvolver um sistema simples em Python que permita o **cadastro, organização, busca e análise de notas escolares** de alunos, visando facilitar o trabalho de professores e administradores no acompanhamento do desempenho acadêmico.

---

### **Escopo do Projeto**

**Inclui:**

* Cadastro de alunos com nome, disciplina e nota.
* Visualização e listagem de todos os cadastros.
* Ordenação dos dados por nome, disciplina e nota (crescente e decrescente).
* Busca por nome do aluno, disciplina e faixa de notas.
* Interface de linha de comando (CLI) para interação com o usuário.
* Estrutura modular dividida em 5 arquivos para facilitar o trabalho em equipe.
* Testes básicos de validação das principais funcionalidades.

---

### **Funcionalidades Esperadas**

1. **Cadastro de Alunos**

   * Inserção de nome, disciplina e nota.
   * Armazenamento em estrutura de dados (lista de dicionários).

2. **Listagem de Dados**

   * Exibição de todos os alunos cadastrados.

3. **Ordenação**

   * Por nome (ordem alfabética).
   * Por disciplina.
   * Por nota (crescente e decrescente).

4. **Busca**

   * Busca por nome exato do aluno.
   * Busca por disciplina.
   * Busca por intervalo de notas (ex: alunos com notas entre 7 e 10).

5. **Interface com o Usuário**

   * Menu interativo no terminal com as opções acima.

6. **Testes**

   * Validação de ordenações e buscas com exemplos simples.

---

### **Necessidades Técnicas**

* Linguagem: **Python**
* Organização modular em arquivos:
* `dados.py`, `ordenacao.py`, `busca.py`, `interface.py`, `main.py`
* Boa prática de código: nomes claros, comentários, modularização
* Integração entre as partes desenvolvidas por diferentes membros da equipe


---

### **Restrições**

* O sistema deve ser executável sem necessidade de bibliotecas externas.
* Cada integrante foi responsável por um módulo específico.
* O tempo de execução deve ser rápido mesmo com até centenas de registros (uso de ordenação eficiente quando necessário).


