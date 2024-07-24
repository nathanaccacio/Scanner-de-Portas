import os
import threading
import colorama
from colorama import Fore
import socket
from datetime import datetime

# Inicializa o colorama
colorama.init()

os.system('cls')  # Limpa o console (somente no Windows)

target = input("Digite o endereço IP ou nome do domínio do alvo: ")  # Solicita ao usuário o alvo

os.system('cls')  # Limpa o console novamente
print('-'*41)
print('Scanning: ' + target)
print('Time Started: ' + str(datetime.now()))
print('-'*41)

ports = []  # Lista para armazenar as portas abertas
threads = []  # Lista para armazenar as threads

def scan(port):
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria um socket TCP/IP
    socket.setdefaulttimeout(1)  # Define um timeout de 1 segundo para a conexão
    try:
        connection.connect((target, port))  # Tenta conectar ao alvo na porta especificada
        connection.close()  # Fecha a conexão se bem-sucedida
        print(f'{Fore.WHITE}Port {Fore.RED}[{port}]{Fore.WHITE} está aberta')  # Imprime que a porta está aberta
        ports.append(port)  # Adiciona a porta aberta à lista
    except Exception:
        pass  # Ignora exceções (a conexão falhou, porta fechada ou inacessível)

# Cria e inicia threads para escanear portas
for port in range(1, 65500):
    thread = threading.Thread(target=scan, kwargs={'port': port})
    threads.append(thread)
    thread.start()

# Aguarda o término de todas as threads
for thread in threads:
    thread.join()

# Verifica e imprime o resultado do escaneamento
if not ports:
    print(f'{Fore.RED}Nenhuma porta aberta foi encontrada.')
else:
    print(f'Portas abertas: {ports}')

# Finaliza o colorama
colorama.deinit()
