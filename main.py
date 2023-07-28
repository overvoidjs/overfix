from autocorrect import Speller
import keyboard
import pyperclip
import os
from dotenv import load_dotenv

load_dotenv()

lang = os.getenv("OVERFIX_LANG")
action = os.getenv("OVERFIX_ACTION")

if lang == None:
    lang = "ru"
if action == None:
    action = "alt"

spell = Speller()
spell = Speller('ru')

def getAndCorrect():
    buffer = pyperclip.paste()
    buffer = spell(buffer)
    pyperclip.copy(buffer)

keyboard.add_hotkey('alt', getAndCorrect)

print("OverFix запущен")
print("Нажмите ALT для форматирования из буфера")
print("Нажмите ALT+ESC для остановки")
keyboard.wait('alt+esc')
print("OverFix остановлен")