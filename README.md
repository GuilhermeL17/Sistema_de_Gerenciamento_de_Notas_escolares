# Descrição do Projeto: Sistema de Gerenciamento de Notas Escolares
Este projeto tem como objetivo desenvolver um Sistema de Gerenciamento de Notas Escolares eficiente, que utilize algoritmos de ordenação e busca para otimizar o acesso e a análise das informações acadêmicas dos alunos. O sistema será capaz de armazenar, organizar e consultar as notas de alunos de maneira dinâmica, permitindo uma visualização clara do desempenho individual e coletivo em diferentes disciplinas.

A aplicação possibilitará que professores e administradores escolares realizem consultas rápidas por nome de aluno, disciplina ou faixa de notas. Além disso, os dados poderão ser ordenados de forma personalizada (por nome, nota ou disciplina), facilitando a construção de rankings, o acompanhamento do progresso acadêmico e a identificação de padrões de desempenho.

A combinação entre algoritmos de ordenação (como Bubble Sort, Merge Sort ou Quick Sort) e algoritmos de busca (como busca sequencial ou busca binária) proporcionará maior eficiência nas operações do sistema, reduzindo o tempo necessário para localizar e organizar informações. Por exemplo, ao ordenar previamente os alunos por nome, a busca binária poderá ser aplicada, acelerando significativamente a localização de registros.


## Módulos:
- **dados.py**: Armazena e cadastra alunos.
- **ordenacao.py**: Contém funções para ordenar por nome, disciplina ou nota.
- **busca.py**: Realiza buscas por nome, disciplina e faixa de nota.
- **interface.py**: Menu de interação com o usuário.
- **main.py**: Arquivo principal de execução.
