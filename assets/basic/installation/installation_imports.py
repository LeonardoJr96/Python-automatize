from assets.biblioteca import *

def installation():
# List for install
    packages_to_install = ["numpy", "pandas", "PyMySQL", "selenium", "seleniumbase", "pyautogui", "pdf2image pillow"]

    # Instalação dos packets
    for package in packages_to_install:
        subprocess.run(["pip", "install", package])
