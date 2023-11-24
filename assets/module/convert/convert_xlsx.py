from assets.biblioteca import *

def txt_to_xlsx(txt_directory, xlsx_directory):
  directory = '[alocad directory]'

  arrives = os.listdir(directory)
  print(f'[alocad new text]')
  for arrives in arrives:
    print(arrives)
    txt_files = glob.glob(txt_directory + '/*.txt')

  for txt_file in txt_files:

      with open(txt_file, "r") as file:
          lines = file.readlines()

      df = pd.DataFrame(lines, columns=['Text'])
      df = df['Text'].str.split(expand=True)
      file_name = txt_file.split('/')[-1].split('.')[0]
      xlsx_file = xlsx_directory + '/' + file_name + '.xlsx'
      df.to_csv(xlsx_file, index=False)
      
      for file in os.listdir(xlsx_directory):
        if file.endswith('.csv'):
            caminho_file = os.path.join(xlsx_directory, file)
            shutil.copy(caminho_file, '/Downloads/')