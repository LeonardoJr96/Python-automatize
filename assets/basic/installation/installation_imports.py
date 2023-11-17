from assets.biblioteca import *

def installation():
# Lista de pacotes a serem instalados
    packages_to_install = ["numpy", "pandas", "PyMySQL", "selenium", "seleniumbase", "pyautogui"]

    # Instalação dos pacotes
    for package in packages_to_install:
        subprocess.run(["pip", "install", package])
