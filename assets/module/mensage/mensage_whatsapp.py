from assets.biblioteca import *
from index_biblioteca import *


def whatsapp():
    # Leitura dos dados do CSV
    data = pd.read_csv("assets\\module\\usuario\\database\\database.csv", sep=",")
    data_dict = data.to_dict('list')

    # Dados de envio
    leads = data_dict['whatsapp']
    messages = data_dict['msg']
    combo = zip(leads, messages)

    for lead, message in combo:
        time.sleep(4)
        
        url = "https://web.whatsapp.com/send?phone=" + lead + "&text=" + message
        webbrowser.open_new_tab(url)
        
        time.sleep(10)
        pg.press("enter")
        pyautogui.press("enter")
        
        try:
            # Esperar até que o campo de mensagem esteja presente
            input_box_selector = '//div[@contenteditable="true"][@data-tab="1"]'
            WebDriverWait(url, 10).until(
                EC.presence_of_element_located((By.XPATH, input_box_selector))
            )
            
            # Se o elemento estiver presente, a página foi carregada
            print("Página carregada com sucesso!")

           
        except Exception as e:
            # Se ocorrer uma exceção, a página pode não ter sido carregada
            print(f"Erro ao carregar a página: {e}")

        soup = BeautifulSoup(requests.get(url).content, 'html.parser')
        selectable_text = soup.find('p', class_='selectable-text')
        print(f"Mensagem enviada para {lead} com sucesso!")
            
        if selectable_text:
                # Obter as coordenadas do elemento
                x, y = selectable_text.location['x'], selectable_text.location['y']

                # Mover o mouse até as coordenadas do elemento
                pyautogui.moveTo(x, y)

                # Pressionar Enter
                pyautogui.press("enter")

                print(f"Mensagem enviada para {lead} com sucesso!")

        else:
                print("Elemento de texto não encontrado.")

        # Encontrar o elemento span por texto
        button_element = soup.find('button')

        pg.press("enter")
        pyautogui.press("enter")
        
        time.sleep(5)
        
        pg.press("enter")   
        pyautogui.press("enter")
        
    # Mantenha a janela aberta para visualização (opcional)
    input("Pressione Enter para fechar o navegador...")