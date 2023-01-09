import pyautogui
from time import sleep

# coordenada mouse noteTiago
# atalho descktop: 54,655
# atalho cadastro: 271,480
# fechar janela: 1418,53
#  usuário: 971,540
#  senha: 954,573
#  entrar: 851,613
#  produto: 594,526
#  quantidade: 597,557
#  preco: 597,590
#  registrar: 497,787

# 0 - iniciando sistema
pyautogui.doubleClick(54,655,duration=0.5)
pyautogui.doubleClick(271,480,duration=2)
pyautogui.doubleClick(1418,53,duration=0.5)
# 1 - clicar e digitar meu usuário;
pyautogui.click(971,540,duration=1)
pyautogui.write('jhonatan')
# 2 - clicar e digitas minha senha;
pyautogui.click(954,573,duration=0.5)
pyautogui.write('123456')
# 3 - clicar em "Entrar";
pyautogui.click(851,613,duration=0.5)
# 4 - extrair cada produto do aquivo txt
with open('files/produtos.txt','r') as arquivo:
  for linha in arquivo:
    produto = linha.split(',')[0]
    quantidade = linha.split(',')[1]
    preco = linha.split(',')[2]
    #   1 - clicar e digitar produto;
    pyautogui.click(594,526,duration=0.5)
    pyautogui.write(produto)
    #   2 - clicar e digitar quantidade;
    pyautogui.click(597,557,duration=0.5)
    pyautogui.write(quantidade)
    #   3 - clicar e digitar preço;
    pyautogui.click(597,590,duration=0.5)
    pyautogui.write(preco)
    #   4 - clicar em registrar;
    pyautogui.click(497,787,duration=0.5)
sleep(1)