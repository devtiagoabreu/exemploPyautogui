import pyautogui
from time import sleep

# coordenada mouse noteTiago
#  usuário: 971,540
#  senha: 954,573
#  entrar: 851,613


# 1 - clicar e digitar meu usuário;
pyautogui.click(971,540,duration=2)
pyautogui.write('tiago')
# 2 - clicar e digitas minha senha;
pyautogui.click(954,573,duration=2)
pyautogui.write('123')
# 3 - clicar em "Entrar";
pyautogui.click(851,613,duration=2)
# 4 - extrair cada produto do aquivo txt
#   1 - clicar e digitar produto;
#   2 - clicar e digitar quantidade;
#   3 - clicar e digitar preço;
#   4 - clicar em registrar;
