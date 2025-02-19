import pyautogui
import time
import pandas as pd

caminho = r"//depo0903/gpa$/PAC/Daniel Menezes/Python/PACOTE/PLUS.xlsx"
ler = pd.read_excel(caminho)
tabela = pd.DataFrame(ler)
print(tabela)

x = 0
y = 1
PLU = tabela.iloc[x, y]
print (PLU)
pyautogui.hotkey("win")
time.sleep(2)
pyautogui.write("OPERA")
time.sleep(3)
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("manhattan")
time.sleep(2)
pyautogui.hotkey("down")
pyautogui.hotkey("down")
pyautogui.hotkey("down")
pyautogui.hotkey("down")
pyautogui.hotkey("down")
pyautogui.hotkey("down")
pyautogui.hotkey("down")
pyautogui.hotkey("down")
pyautogui.hotkey("down")
time.sleep(3)
pyautogui.press("enter")
time.sleep(3)
pyautogui.leftClick(58, 83)
time.sleep(2)
pyautogui.write("itens")
time.sleep(2)
pyautogui.hotkey("down")
pyautogui.hotkey("down")
pyautogui.hotkey("down")
pyautogui.press("enter")
time.sleep(2)
pyautogui.leftClick(944, 133)




while True and x < len (tabela):
    
    PLU = tabela.iloc[x, y]


    time.sleep(1)
    pyautogui.doubleClick(275, 191)
    time.sleep(1)
    pyautogui.hotkey("backspace")
    time.sleep(1)
    pyautogui.write(str(PLU))
    time.sleep(1)
    pyautogui.leftClick(1099, 195)
    time.sleep(1)
    pyautogui.leftClick(74, 297)
    time.sleep(1)
    pyautogui.leftClick(73, 701)
    time.sleep(2)
    pyautogui.leftClick(433, 227)
    time.sleep(2)
    pyautogui.leftClick(75, 696)
    time.sleep(2)
    pyautogui.leftClick(637, 301)
    time.sleep(2)
    pyautogui.leftClick(651, 348)
    time.sleep(1)
    pyautogui.leftClick(1238, 692)
    time.sleep(3)
    pyautogui.leftClick(62, 144)
    x = x + 1
    time.sleep(2)
    print("DEV: DANIEL MENEZES")
    
