# Importa a biblioteca do Python que permite a comunicação do sistema com a placa de rede.
import socket

# Bloco try para tratamento de erros com excepts abaixo.
try:
    alvo = input("Qual IP deseja escanear: ")
    print(f"Iniciando scan no alvo: {alvo}...\n")

    for porta in range(1, 101):

# 1. Cria o 'objeto' socket (configurado para usar IPv4 e protocolo TCP)
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Define um tempo limite (timeout) de 0.5 segundos.
# Se o alvo demorar mais que isso para responder, cancelamos para o programa não travar.
        cliente.settimeout(0.5)

# 3. Tenta conectar. A função connect_ex retorna o número 0 se a conexão der certo (porta aberta)
        resultado_conexao = cliente.connect_ex((alvo, porta))

        if resultado_conexao == 0:
            print(f"A porta {porta} esta ABERTA!")

# 4. Fecha a conexão
        cliente.close()

    print("\nScan finalizado!")
# Tratamento de erros.
except KeyboardInterrupt:
    print(f"Scan cancelado pelo usuário.")
except socket.gaierror:
    print(f"Erro: Host ou IP inválidos.")