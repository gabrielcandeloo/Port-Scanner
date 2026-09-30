# 🔍 Scanner de Portas TCP (Port Scanner)

## 📖 Sobre o Projeto

Este projeto é um scanner de portas TCP desenvolvido em Python. A ferramenta foi construída do zero com o objetivo de auditar a segurança de redes, identificando portas abertas em um endereço IP alvo. É uma aplicação prática dos conceitos de infraestrutura de redes, comunicação via sockets e tratamento avançado de exceções em Cibersegurança.

## 🚀 Funcionalidades

* **Alvo Dinâmico:** Permite ao usuário inserir qualquer endereço IP ou hostname para análise.
* **Varredura Estratégica:** Analisa automaticamente as portas lógicas da 1 a 100.
* **Silêncio por Padrão (Security UX):** Filtra o ruído e exibe apenas as portas que estão abertas, otimizando a leitura do analista.
* **Blindagem contra Falhas:** Possui tratamento de exceções rigoroso para lidar com interrupções abruptas do usuário (`KeyboardInterrupt`) e resolução de DNS/IP inválida (`socket.gaierror`).

## 🛠️️ Tecnologias e Bibliotecas

* **Linguagem:** Python 3
* **Bibliotecas:** `socket` (nativa do Python)

## 🧠 Conceitos de Cibersegurança Aplicados

* **Comunicação TCP/IP:** Aplicação prática do *Three-Way Handshake* (SYN, SYN-ACK, ACK) na detecção de portas abertas.
* **Gestão de Timeouts:** Prevenção de congelamento da aplicação ao interagir com firewalls em modo furtivo (*drop mode*).
* **Desenvolvimento Seguro:** Código estruturado para evitar crashes inesperados (*Denial of Service* acidental na própria ferramenta) através do uso defensivo de `try/except`.

## 💻 Como Executar

1. Clone o repositório.
2. Certifique-se de ter o Python instalado.
3. Execute o arquivo no terminal:

⚠️ Aviso Ético: Esta ferramenta foi desenvolvida com propósitos educacionais para o estudo de Segurança da Informação. O uso deste software para escanear redes ou IPs sem a devida autorização explícita e por escrito do proprietário é ilegal e antiético. Utilize o IP 127.0.0.1 (localhost) para testes seguros na sua própria máquina.
```bash
python port_scanner.py
