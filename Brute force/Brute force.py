import itertools
import string
import time

# Senha-alvo (apenas para demonstração)
senha_correta = "abc12"

# Define o conjunto de caracteres a serem usados
caracteres = string.ascii_lowercase + string.digits  # a-z, 0-9
tamanho_maximo = 5  # Tamanho máximo da senha a ser testada

# Função para gerar combinações e testar
def brute_force():
    tentativas = 0
    start_time = time.time()

    # Testa combinações de diferentes tamanhos
    for tamanho in range(1, tamanho_maximo + 1):
        # Gera todas as combinações possíveis
        for combinacao in itertools.product(caracteres, repeat=tamanho):
            tentativa = ''.join(combinacao)
            tentativas += 1
            print(f"Tentando: {tentativa}")

            # Verifica se a senha está correta
            if tentativa == senha_correta:
                end_time = time.time()
                print(f"Senha encontrada: {tentativa}")
                print(f"Tentativas: {tentativas}")
                print(f"Tempo: {end_time - start_time:.2f} segundos")
                return
    print("Senha não encontrada.")

# Executa o brute force
brute_force()