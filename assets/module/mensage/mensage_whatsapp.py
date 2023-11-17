from assets.biblioteca import *
from index_biblioteca import *


def whatsapp():
    #import csv
    data = pd.read_csv("assets\\module\\usuario\\database\\database.csv",sep=",")
    data_dict = data.to_dict('list')

    #envio

    data_dict = data.to_dict('list')

    leads = data_dict['whatsapp']
    messages = data_dict['msg']
    combo = zip(leads, messages)
    first = True

    for lead, message in combo:
        time.sleep(4)
        web.open("https://web.whatsapp.com/send?phone="+lead+"&text="+message)
        
        if first:
            time.sleep(6)
            first = False
            
        width, height = pg.size()
        pg.click(width/2,height/2)
        time.sleep(6)
        pg.press('enter')
        time.sleep(6)
        pg.press('Enter')
        time.sleep(6)
        pg.press('enter')
    pg.press("ctrl", "w")

