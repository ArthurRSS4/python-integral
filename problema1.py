import importlib.util
import sys
import os  

# Função para instalar um pacote usando pip
def install_package(package):
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Verifica se a biblioteca scipy está instalada e a instala caso contrário
if importlib.util.find_spec("scipy") is None:
    print("Biblioteca scipy não encontrada. Instalando...")
    install_package("scipy")
    importlib.invalidate_caches()

import scipy.integrate as spi

# Calcula a velocidade média dado o tempo, velocidade inicial e velocidade final
def velocidade_media(tempo, velocidade_inicial, velocidade_final):
    return (velocidade_inicial + velocidade_final) / 2

# Calcula o gasto de energia durante a corrida dado o tempo, massa, velocidade inicial e final
def gasto_energia_corrida(tempo, massa, velocidade_inicial, velocidade_final):
    tempo_inicial = 0
    def potencia_instantanea(tempo):
        velocidade = velocidade_media(tempo, velocidade_inicial, velocidade_final)
        return 1.036 * massa * velocidade

    gasto_energia, _ = spi.quad(potencia_instantanea, tempo_inicial, tempo)
    return gasto_energia 

# Calcula o gasto de energia durante a natação
def gasto_energia_natacao(tempo, massa, velocidade_inicial, velocidade_final):
    tempo_inicial = 0
    distancia = velocidade_media(tempo, velocidade_inicial, velocidade_final) * (tempo - tempo_inicial)
    gasto_energia = 1.2 * massa * distancia
    return gasto_energia

# Calcula o gasto de energia durante o ciclismo
def gasto_energia_ciclismo(tempo, massa, velocidade_inicial, velocidade_final):
    tempo_inicial = 0
    distancia = velocidade_media(tempo, velocidade_inicial, velocidade_final) * (tempo- tempo_inicial)
    gasto_energia = 0.9 * massa * distancia
    return gasto_energia

# Calcula a taxa de gasto de energia durante a corrida dado a velocidade
def taxa_gasto_energia_corrida(velocidade):
    velocidade_m_min = velocidade * 1000 / 60
    return 0.1 * velocidade_m_min

# Calcula a taxa de gasto de energia durante a natação dado a velocidade
def taxa_gasto_energia_natacao(velocidade):
    velocidade_m_min = velocidade * 1000 / 60
    return 0.1 * velocidade_m_min

# Calcula a taxa de gasto de energia durante o ciclismo dado a velocidade
def taxa_gasto_energia_ciclismo(velocidade):
    velocidade_m_min = velocidade * 1000 / 60
    return 0.07 * velocidade_m_min

# Calcula o total de energia gasta durante um exercício dado a opção, velocidade, tempo, massa, velocidade inicial e final
def total_energia_gasta_exercicio(opcao, velocidade, tempo, massa, velocidade_inicial, velocidade_final):
    if opcao == 1:
        def f_taxa_gasto_energia(t):
            return taxa_gasto_energia_corrida(velocidade)
        gasto_energia_func = gasto_energia_corrida
    elif opcao == 2:
        def f_taxa_gasto_energia(t):
            return taxa_gasto_energia_ciclismo(velocidade)
        gasto_energia_func = gasto_energia_ciclismo
    elif opcao == 3:
        def f_taxa_gasto_energia(t):
            return taxa_gasto_energia_natacao(velocidade)
        gasto_energia_func = gasto_energia_natacao
    else:
        print("Opção inválida!")
        return None

    a = 0
    b = tempo

    total_energia = spi.quad(f_taxa_gasto_energia, a, b)[0]

    return total_energia

# Loop do menu principal
while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpar tela
    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("                       ---> MENU <---\n")
    print("[ 1 ] Calcular Gasto de Energia")
    print("[ 2 ] Análise do Efeito do Exercício na Perda de Peso")
    print("[ 3 ] Sair\n")
    escolha = int(input("-> "))

    # Opção 1: Calcular Gasto de Energia
    if escolha == 1:
        print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=\n")
        print("Escolha o tipo de exercício:")
        print("[ 1 ] Corrida")
        print("[ 2 ] Ciclismo")
        print("[ 3 ] Natação")
        opcao = int(input("-> "))
        tempo = float(input("Tempo de exercício (minutos): ")) / 60
        massa = float(input("Massa corporal (kg): "))
        velocidade_inicial = float(input("Velocidade inicial (km/h): "))
        velocidade_final = float(input("Velocidade final (km/h): "))

        # Calcula o gasto de energia com base na opção escolhida
        if opcao == 1:
            gasto = gasto_energia_corrida(tempo, massa, velocidade_inicial, velocidade_final)
        elif opcao == 2:
            gasto = gasto_energia_ciclismo(tempo, massa, velocidade_inicial, velocidade_final)
        elif opcao == 3:
            gasto = gasto_energia_natacao(tempo, massa, velocidade_inicial, velocidade_final)
        else:
            print("Opção inválida!")
            gasto = 0
            continue
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=\n")
        print("Resultado = {:.2f} kcal".format(gasto))
        input("Pressione Enter para continuar...")

    # Opção 2: Análise do Efeito do Exercício na Perda de Peso
    elif escolha == 2:
        print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=\n")
        print("Análise do Efeito do Exercício na Perda de Peso:")
        ingestao_calorica = float(input("Ingestão calórica diária (kcal): "))

        opcao = int(input("Escolha o tipo de exercício (1: Corrida, 2: Ciclismo, 3: Natação): "))
        tempo = float(input("Tempo de exercício por dia (minutos): ")) / 60
        massa = float(input("Massa corporal (kg): "))
        velocidade_inicial = float(input("Velocidade inicial (km/h): "))
        velocidade_final = float(input("Velocidade final (km/h): "))

        total_gasto = total_energia_gasta_exercicio(opcao, velocidade_final, tempo, massa, velocidade_inicial, velocidade_final)

        if total_gasto is not None:
            saldo_calorico = ingestao_calorica - total_gasto
            print("\nSaldo calórico diário:", saldo_calorico, "kcal")
            if saldo_calorico < 0:
                print("Parabéns! Você está queimando mais calorias do que está consumindo.")
            elif saldo_calorico > 0:
                print("Atenção! Você está consumindo mais calorias do que está queimando.")
            else:
                print("Seu saldo calórico está equilibrado.")
        input("Pressione Enter para continuar...")

    # Opção 3: Sair
    elif escolha == 3:
        print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=")
        print("\nSaindo...")
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpar tela
        print("Obrigado por usar o programa!")
        break
    else:
        print("Opção inválida!")