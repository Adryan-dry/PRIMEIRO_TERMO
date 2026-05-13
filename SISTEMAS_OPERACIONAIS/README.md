Crie um arquivo markdown para minhas aulas de Sistemas Operacionais
Preciso das seguintes informações
Conteúdo de aula
Funcionais e Não Funcionais 
Diagramas
Relatórios Técnicos
Brainstorm
Prototipagem
Entrevistas 

# 🐧 Sistemas Operacionais: Notas de Aula e Laboratórios com Python

Este documento centraliza o conteúdo programático, especificações de projetos, diagramas e práticas de programação voltadas ao entendimento do núcleo de um Sistema Operacional (SO).

---

## 📅 1. Conteúdo de Aula

### Conceitos Fundamentais de SO
* **Definição:** Software que gerencia o hardware do computador e fornece serviços para os aplicativos.
* **Gerenciamento de Processos:** Estados de um processo (Pronto, Executando, Bloqueado), escalonamento e troca de contexto.
* **Gerenciamento de Memória:** Memória virtual, paginação, segmentação e algoritmos de substituição de páginas (FIFO, LRU).
* **Sistemas de Arquivos:** Estrutura de diretórios, permissões de acesso (POSIX) e alocação de espaço.
* **Concorrência:** Threads, condições de corrida, exclusão mútua, semáforos e *deadlocks*.

---

## 📋 2. Requisitos de Subsistemas (Funcionais e Não Funcionais)

*Análise de requisitos aplicada ao desenvolvimento de componentes de um SO ou scripts de automação.*

### Requisitos Funcionais (RF)
*O que o utilitário ou subsistema do SO deve executar.*
* **RF01:** O script deve listar todos os processos ativos no sistema operacional.
* **RF02:** O sistema de arquivos deve permitir a criação, leitura e exclusão de arquivos de texto.
* **RF03:** O escalonador deve interromper processos que estourem o tempo de *quantum* alocado.

### Requisitos Não Funcionais (RNF)
*Restrições de desempenho, segurança e arquitetura do SO.*
* **RNF01 (Desempenho):** A troca de contexto entre threads não deve consumir mais que 5% da CPU.
* **RNF02 (Segurança):** O sistema deve isolar o espaço de memória de cada processo (*Memory Protection*).
* **RNF03 (Portabilidade):** O protótipo em Python deve rodar de forma idêntica em ambientes Linux e Windows.

---

## 📊 3. Diagramas de Arquitetura do SO

### Diagrama de Transição de Estados de um Processo
