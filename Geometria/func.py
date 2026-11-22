import subprocess
import platform

def limpar_terminal():
    comando = 'cls' if platform.system() == 'Windows' else 'clear'
    subprocess.run(comando, shell=True)