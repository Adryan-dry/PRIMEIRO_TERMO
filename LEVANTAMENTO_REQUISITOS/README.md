Crie um arquivo markdown para minhas aulas de Levantamento de Requisitos 
Preciso das seguintes informações
Conteúdo de aula
Funcionais e Não Funcionais 
Diagramas
Relatórios Técnicos
Brainstorm
Prototipagem
Entrevistas 

# 📋 Engenharia de Software: Levantamento e Engenharia de Requisitos

Este documento consolida o material de aula, técnicas de elicitação, padrões de documentação e metodologias para a descoberta de requisitos de software.

---

## 📅 1. Conteúdo de Aula

### Introdução à Engenharia de Requisitos
* **Definição:** Processo de descobrir, analisar, documentar e verificar os serviços e restrições do sistema.
* **Ciclo de Vida:** Elicitação -> Análise/Negociação -> Especificação -> Validação -> Gerenciamento.
* **Problemas Comuns:** Escopo mal definido, falhas de comunicação, mudanças constantes e requisitos implícitos.

### Técnicas de Elicitação Estudadas
1. Entrevistas (Estruturadas e Não Estruturadas).
2. Brainstorming e Workshops de JAD (Joint Application Design).
3. Etnografia e Observação Direta.
4. Análise de Documentos e Engenharia Reversa.

---

## 🔍 2. Requisitos Funcionais e Não Funcionais

### Requisitos Funcionais (RF)
*O que o sistema deve fazer. Declarações de funções, serviços ou comportamentos esperados.*
* **RF01:** O sistema deve permitir que o usuário crie uma conta usando e-mail e senha.
* **RF02:** O sistema deve emitir um relatório de vendas mensal em formato PDF.
* **RF03:** O sistema deve enviar uma notificação push quando o status do pedido mudar.

### Requisitos Não Funcionais (RNF)
*Como o sistema deve fazer. Propriedades de qualidade, restrições de desempenho, segurança ou conformidade.*
* **RNF01 (Desempenho):** A página inicial deve carregar em menos de 2 segundos sob carga normal.
* **RNF02 (Segurança):** Todas as senhas dos usuários devem ser criptografadas no banco de dados usando bcrypt.
* **RNF03 (Disponibilidade):** O sistema deve estar disponível 99,9% do tempo (24/7).

---

## 📊 3. Diagramas de Requisitos

### Modelagem Visual do Escopo
*Os diagramas ajudam a alinhar o entendimento entre a equipe técnica e os stakeholders.*

