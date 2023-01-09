import pyautogui
from time import sleep

# coordenada mouse noteTiago
# 0 - iniciando sistema
pyautogui.doubleClick(54,655,duration=0.5)
pyautogui.doubleClick(238,530,duration=0.5)
pyautogui.click(943,671,duration=2)
sleep(3)
# 1 - efetuar login;
# 2 - extraindo dados do arquivo de usuarios;
with open('files/autoConf.txt','r') as arquivo:
  for linha in arquivo:
    usuario = linha.split(',')[0]
    senha = linha.split(',')[1]
    # 1 -clicar e digitar usuario;
    pyautogui.click(746,465,duration=1)
    pyautogui.write(usuario)
    # 2 - clicar e digitar minha senha;
    pyautogui.doubleClick(1007,467,duration=1) 
    # 3 - clicar em "Acessar";
    pyautogui.click(861,533,duration=0.5)
    # 4 - mensagem de senha não digitada
    pyautogui.click(1186,202,duration=2)
    # 5 - clicar e digitar minha senha;
    pyautogui.doubleClick(1007,467,duration=1) 
    pyautogui.write(senha)
    # 6 - clicar em "Acessar";
    pyautogui.click(861,533,duration=0.5)
# 3 - acessando system view
sleep(4)
pyautogui.click(505,244,duration=0.5)
# 4 - abrindo relatorio de contas a receber
sleep(4)
pyautogui.click(448,420,duration=1)
# 5 - clicando no relatorio padrao e visualizar
pyautogui.click(805,500,duration=1)
# 6 - clicando em exportar em csv, gerando arquivo e fechando relatório
pyautogui.click(37,180,duration=1)
pyautogui.click(961,621,duration=1)
pyautogui.click(1905,143,duration=1)
sleep(15)
# 7 - acessando a lista de processos agendados
pyautogui.click(1655,152,duration=1)
# 8 - efetuar download do arquivo
pyautogui.click(664,641,duration=1)

