<!-- Crie um arquivo markdown para minhas aulas de Arquitetura de redes IoT -->
Preciso das seguintes informações
Conteúdo de aula
Funcionais e Não Funcionais 
Diagramas
Relatórios Técnicos
Brainstorm
Prototipagem
Entrevistas  -->

# 🌐 Arquitetura de Redes IoT: Notas de Aula e Projetos

Este documento serve como repositório central para os conteúdos, metodologias e documentações técnicas das aulas de Arquitetura de Redes IoT.

---

## 📅 1. Conteúdo de Aula

### Introdução à IoT
* **Conceito:** Interconexão digital de objetos cotidianos com a internet.
* **Camadas da Arquitetura:** Percepção (sensores), Rede (gateways), Processamento (nuvem) e Aplicação.
* **Protocolos Comuns:** MQTT, CoAP, HTTP, LoRaWAN, Zigbee.

### Principais Tópicos Estudados
1. Topologias de rede (Estrela, Malha, Ponto a Ponto).
2. Gerenciamento de energia em dispositivos restritos.
3. Segurança física e lógica em redes de sensores.

---

## 📋 2. Requisitos do Sistema IoT

### Requisitos Funcionais (RF)
*O que o sistema IoT deve fazer na prática.*
* **RF01:** O sensor deve coletar dados de temperatura a cada 5 segundos.
* **RF02:** O gateway deve enviar alertas via MQTT se a umidade passar de 80%.
* **RF03:** O painel web deve exibir gráficos em tempo real dos dispositivos ativos.

### Requisitos Não Funcionais (RNF)
*Como o sistema deve se comportar (qualidade e restrições).*
* **RNF01:** A bateria do nó sensor deve durar pelo menos 2 anos.
* **RNF02:** A latência máxima no envio de comandos críticos deve ser menor que 200ms.
* **RNF03:** Os dados transmitidos via rádio devem usar criptografia AES-128.

---

## 📊 3. Diagramas de Arquitetura

### Visão Geral do Fluxo
