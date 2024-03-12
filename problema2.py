# Para testar o código no vscode, digite no terminal: pip install scipy
from scipy import integrate
import os

# Função para limpar a tela do terminal
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para calcular a taxa de gasto energético durante a corrida (em calorias por minuto)
def taxa_gasto_energia_corrida(velocidade):
    # Suponha que uma pessoa gasta 0.1 calorias por metro correndo
    # Convertendo a velocidade de km/h para m/min
    velocidade_m_min = velocidade * 1000 / 60  # 1 km/h = 1000 m/h = 1000/60 m/min
    return 0.1 * velocidade_m_min

# Função para calcular a taxa de gasto energético durante o ciclismo (em calorias por minuto)
def taxa_gasto_energia_ciclismo(velocidade):
    # Suponha que uma pessoa gasta 0.07 calorias por metro pedalando
    # Convertendo a velocidade de km/h para m/min
    velocidade_m_min = velocidade * 1000 / 60  # 1 km/h = 1000 m/h = 1000/60 m/min
    return 0.07 * velocidade_m_min

# Função para calcular a taxa de gasto energético durante a natação (em calorias por minuto)
def taxa_gasto_energia_natacao(velocidade):
    # Suponha que uma pessoa gasta 0.1 calorias por metro nadando
    # Convertendo a velocidade de km/h para m/min
    velocidade_m_min = velocidade * 1000 / 60  # 1 km/h = 1000 m/h = 1000/60 m/min
    return 0.1 * velocidade_m_min

# Função para calcular o total de energia gasta durante o exercício
def total_energia_gasta_exercicio(opcao, velocidade, tempo):
    if opcao == 1:
        # Definindo a função de taxa de gasto energético para integração
        def f_taxa_gasto_energia(t):
            return taxa_gasto_energia_corrida(velocidade)
    elif opcao == 2:
        # Definindo a função de taxa de gasto energético para integração
        def f_taxa_gasto_energia(t):
            return taxa_gasto_energia_ciclismo(velocidade)
    elif opcao == 3:
        # Definindo a função de taxa de gasto energético para integração
        def f_taxa_gasto_energia(t):
            return taxa_gasto_energia_natacao(velocidade)
    else:
        print("Opção inválida!")
        return None, None
    
    # Limites de integração para o tempo
    a = 0  # Tempo inicial
    b = tempo  # Tempo final
    
    # Calculando a integral definida
    total_energia = integrate.quad(f_taxa_gasto_energia, a, b)[0]
    
    return total_energia

# Loop principal
while True:
    limpar_tela()
    
    # Menu interativo
    print("Bem-vindo ao calculador de energia gasta durante o exercício!")
    print("Por favor, selecione o tipo de exercício:")
    print("1. Corrida")
    print("2. Ciclismo")
    print("3. Natação")
    print("4. Sair")

    # Solicita ao usuário a escolha do tipo de exercício
    opcao = int(input("Escolha o tipo de exercício (1/2/3/4): "))
    
    # Verifica se o usuário deseja sair
    if opcao == 4:
        break
    
    # Solicita ao usuário a velocidade média de exercício em quilômetros por hora (km/h)
    velocidade = float(input("Digite a velocidade média de exercício em km/h: "))

    # Solicita ao usuário o tempo de exercício em minutos
    tempo_exercicio = float(input("Digite o tempo de exercício em minutos: "))

    # Calcula o total de energia gasta com base no tipo de exercício escolhido
    total_energia = total_energia_gasta_exercicio(opcao, velocidade, tempo_exercicio)

    # Exibe o total de energia gasta
    if total_energia is not None:
        if opcao == 1:
            tipo_exercicio = "Corrida"
        elif opcao == 2:
            tipo_exercicio = "Ciclismo"
        elif opcao == 3:
            tipo_exercicio = "Natação"
        print(f"Total de energia gasta durante {tempo_exercicio} minutos de {tipo_exercicio}: {total_energia:.2f} calorias")
    
    # Espera o usuário pressionar Enter antes de continuar
    input("Pressione Enter para continuar...")
