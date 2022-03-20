from html.entities import name2codepoint
from tracemalloc import stop
import pyautogui, pyperclip
import keyboard
from time import sleep
from convert_contacts import create_users_for_find, list_search
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

def clear_space():
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')
    pyautogui.press("backspace")

# @benchmark
def main():
    country = pyautogui.prompt('Введите название страны')
    stop_word = pyautogui.prompt('Введите слова для исключения из поиска')
    text_message = pyautogui.prompt('Введите ваше сообщение')

    create_users_for_find(country, stop_word)
    point = pyautogui.locateCenterOnScreen('data/search.PNG')
    pyautogui.doubleClick(point)
    sleep(1)
    
    count = 0
    for name in list_search:
    
        keyboard.write(name)
        sleep(3)
        pyautogui.press('enter')
        sleep(0.5)
        pyautogui.press('enter')

        sleep(1)
        keyboard.write(text_message)
        # pyautogui.press('enter')
        pyautogui.leftClick(pyautogui.locateCenterOnScreen('data/clear.PNG'))
        sleep(0.5)
        pyautogui.doubleClick(point)
        sleep(0.5)
        clear_space()
        count += 1
    pyautogui.confirm(f"Отправка писем завершена, отправленно {count} писем!")
    




# if __name__ == '__main__':
#     main()

main()