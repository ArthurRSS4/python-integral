import importlib.util
import sys

# instalar biblioteca caso não a tenha baixada via pip
def install_package(package):
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
  
# verificar se a biblioteca foi instalada
if importlib.util.find_spec("scipy") is None:
    print("Biblioteca scipy não encontrada. Instalando...")
    install_package("scipy")
    importlib.invalidate_caches()  # Atualiza o cache de módulos importados

import scipy.integrate as spi

# Definir a velocidade media para o calculo
def velocidade_media(tempo, velocidade_inicial, velocidade_final):
    return (velocidade_inicial + velocidade_final) / 2

def gasto_energia_corrida(tempo_inicial, tempo_final, massa, velocidade_inicial, velocidade_final):
    # Define a potência instantânea
    def potencia_instantanea(tempo):
        velocidade = velocidade_media(tempo, velocidade_inicial, velocidade_final)
        return 1.036 * massa * velocidade

    #integrar potência instantânea ao longo do tempo fornecido
    gasto_energia, _ = spi.quad(potencia_instantanea, tempo_inicial, tempo_final)
    return gasto_energia