import pyautogui
from time import sleep
import webbrowser
from random import choice
lista_comentarios = ['Wooooow!!', 'Amazing! :)', 'Cool!', 'Great post <3']
while True:
    usuario = 'pagina_legal19'
    senha = 'senha' # essa não é a senha de verdade
    webbrowser.open('https://www.instagram.com/')
    sleep(2)
    botao_entrar = pyautogui.locateCenterOnScreen('botao_entrar.png')
    if botao_entrar is not None:
        # Dá um click mais ou menos no centro da tela, para habilitar
        pyautogui.click(663, 409)
        pyautogui.tripleClick(859, 278, duration=0.5)
        pyautogui.typewrite(usuario)
        sleep(1)
        pyautogui.tripleClick(859, 318, duration=0.5)
        pyautogui.typewrite(senha)
        sleep(1)
        pyautogui.click(botao_entrar, duration=0.5)
        sleep(2.5)
        agora_nao = (809, 514)
        pyautogui.doubleClick(agora_nao, duration=0.5)
        sleep(3)
    pesquisar = pyautogui.locateCenterOnScreen('pesquisar.png')
    if pesquisar is not None:
        pyautogui.click(pesquisar)
        sleep(0.5)
        conta_a_pesquisar = pyautogui.prompt('Qual conta pesquisar? ')
        pyautogui.typewrite(conta_a_pesquisar)
        sleep(1.5)
        pyautogui.press(['down', 'enter'])
        sleep(2.5)
        pyautogui.click(607,633, duration=1)
        sleep(2.5)
        botao_curtir = pyautogui.locateCenterOnScreen('botao_curtir.png')
        if botao_curtir is not None:
            pyautogui.click(botao_curtir, duration=1.5)
            sleep(0.5)
            pyautogui.click(botao_curtir[0] + 40, duration=1.5)
            sleep(0.5)
            pyautogui.typewrite(choice(lista_comentarios))
            sleep(1)
            pyautogui.press('enter')
        else:
            pyautogui.alert('Você já curtiu essa publicação!!')
        sleep(5)
        pyautogui.hotkey('alt', 'f4')
        sleep(86400)
    else:
        pyautogui.alert('Algo deu errado. É possível que os dados de login estejam incorretos.')
        break
