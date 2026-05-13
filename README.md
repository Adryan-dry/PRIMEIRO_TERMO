# PRIMEIRO_TERMO
Material de Aula 1°Termo - LOPAL - SOP -ARI - LER


## LOPAL 
Lógica de programação Python


### SOP 
# 🎓 Repositório de Disciplinas: Engenharia de Software, Infraestrutura e Sistemas

Este repositório centraliza os planos de aula, materiais de apoio, roteiros de laboratório e frameworks de documentação técnica para quatro disciplinas fundamentais dos cursos de Tecnologia e Engenharia.

---

## 📚 Sumário das Disciplinas

1. [🌐 Arquitetura de Redes IoT](#-1-arquitetura-de-redes-iot)
2. [📋 Engenharia e Levantamento de Requisitos](#-2-engenharia-e-levantamento-de-requisitos)
3. [💻 Lógica de Programação e Algoritmos](#-3-lógica-de-programação-e-algoritmos)
4. [🐧 Sistemas Operacionais (com Práticas em Python)](#-4-sistemas-operacionais-com-práticas-em-python)

---

## 🌐 1. Arquitetura de Redes IoT

Foco no design de soluções conectadas, topologias de comunicação e integração hardware-software de baixo consumo.

* **Conteúdo Programático:** Camadas da arquitetura IoT (Percepção, Rede, Nuvem), protocolos (MQTT, CoAP, LoRaWAN, Zigbee) e gerenciamento energético.
* **Engenharia de Requisitos:**
  * *Funcionais:* Frequência de coleta de sensores e regras de acionamento de atuadores.
  * *Não Funcionais:* Restrições de autonomia de bateria (anos) e latência de rede em milissegundos.
* **Modelagem Visual:** Diagramas de blocos de hardware, fluxos de mensagens sequenciais e topologias de redes mesh/estrela.
* **Abordagem Prática:**
  * *Brainstorming:* Ideação voltada para Cidades Inteligentes e Indústria 4.0.
  * *Prototipagem:* Uso do microcontrolador ESP32, simulador Wokwi e IDE Arduino/PlatformIO.
  * *Validação:* Entrevistas de campo com foco em restrições geográficas, climáticas e infraestrutura local.

---

## 📋 2. Engenharia e Levantamento de Requisitos

Metodologias e técnicas para elicitar, analisar, documentar e validar as necessidades de stakeholders em projetos de software.

* **Conteúdo Programático:** Ciclo de vida dos requisitos (Elicitação à Validação) e mitigação de problemas de comunicação no escopo do projeto.
* **Engenharia de Requisitos:**
  * *Funcionais:* Comportamentos explícitos, geração de relatórios e fluxos de navegação do usuário.
  * *Não Funcionais:* Métricas quantificáveis de desempenho (tempo de resposta), segurança (hashing) e disponibilidade (SLA).
* **Modelagem Visual:** Diagramas de Casos de Uso (UML), Diagramas de Atividades para fluxos de negócio e Mapas Mentais.
* **Abordagem Prática:**
  * *Brainstorming:* Condução de sessões sem julgamento e aplicação da **Matriz MoSCoW** para priorização.
  * *Prototipagem:* Criação de wireframes de baixa fidelidade no papel e interfaces navegáveis de alta fidelidade no Figma.
  * *Validação:* Roteiros de entrevistas estruturadas contendo perguntas abertas de contexto e fechadas para limites técnicos.

---

## 💻 3. Lógica de Programação e Algoritmos

Base do pensamento computacional, estruturação lógica e resolução de problemas através de código estruturado.

* **Conteúdo Programático:** Tipos de dados, operadores lógicos/aritméticos, estruturas condicionais (`if/else`) e laços de repetição (`while/for`).
* **Engenharia de Requisitos:**
  * *Funcionais:* Entradas de dados via teclado, cálculos matemáticos esperados e saídas formatadas em console.
  * *Não Funcionais:* Restrição de linguagens específicas (C/Python) e padronização estética (indentação e comentários).
* **Modelagem Visual:** Construção de fluxogramas padronizados (elipses, losangos e retângulos) para representação algorítmica.
* **Abordagem Prática:**
  * *Brainstorming:* Técnicas de decomposição de grandes problemas matemáticos/comerciais em subrotinas simples.
  * *Prototipagem:* Desenvolvimento inicial em ambiente visual e amigável através do Portugol (Visualg) e Scratch.
  * *Validação:* Entrevistas simuladas para mapear regras de negócio do cliente e validação rigorosa via Teste de Mesa.

---

## 🐧 4. Sistemas Operacionais (com Práticas em Python)

Estudo do núcleo dos sistemas operacionais, gerenciamento de recursos de hardware e automação via scripts de infraestrutura.

* **Conteúdo Programático:** Gerenciamento de processos e memória (virtual, paginação), sistemas de arquivos, concorrência, concorrência e deadlocks.
* **Engenharia de Requisitos:**
  * *Funcionais:* Captura de logs do sistema, manipulação de arquivos em disco e interrupção de tarefas travadas.
  * *Não Funcionais:* Isolamento de memória no Kernel Space, portabilidade multi-plataforma e consumo mínimo de CPU.
* **Modelagem Visual:** Diagramas de Transição de Estados de um Processo e mapeamento de alocação de memória (Stack vs Heap).
* **Abordagem Prática:**
  * *Brainstorming:* Discussão de arquitetura de exclusão mútua e tratamento preventivo de condições de corrida.
  * *Prototipagem em Python:* Monitoramento de recursos de hardware com o módulo `psutil` e simulação de concorrência real através de `threading` e `Locks`.
  * *Validação:* Entrevistas voltadas ao ecossistema DevOps e SysAdmin para identificar gargalos operacionais e tarefas candidatas à automação.

---

## 📁 Estrutura de Pastas Sugerida para o Repositório

```text
├── 📁 iot-architecture/
│   ├── README.md (Conteúdo específico de IoT)
│   └── 📁 labs/ (Modelos Wokwi e códigos ESP32)
├── 📁 requirements-engineering/
│   ├── README.md (Teoria de Elicitação)
│   └── 📁 templates/ (Modelos de SRS IEEE 830 e roteiros de entrevista)
├── 📁 programming-logic/
│   ├── README.md (Exercícios de Algoritmos)
│   └── 📁 examples/ (Códigos em Portugol e C)
└── 📁 operating-systems/
    ├── README.md (Teoria de SO)
    └── 📁 python-scripts/ (Exemplos de psutil e threading)
```
