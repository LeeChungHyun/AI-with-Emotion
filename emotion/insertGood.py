import pyautogui
import pyperclip
import time
import sys
import pandas as pd

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
df = pd.read_excel('feeling.xlsx', sheet_name='Sheet1')
words = df[df["감정범주"].isin(["기쁨","흥미"])].sort_values(by='감정정도M', ascending=False)[:50][["단어"]].drop_duplicates().values.flatten()


def click(x, y):
    time.sleep(0.5)
    pyautogui.moveTo(x, y) #마우스의 현재 위치를 옮겨주는 절대적인 값
    pyautogui.click(clicks=1)
    time.sleep(0.5)
    

for i in range(len(words)):
    click(449,959) #특정 커서의 위치다(find.py에서 찾을 수 있음)
    click(702,574)
    pyperclip.copy(words[i]) #엑셀의 데이터 복사
    pyautogui.hotkey("ctrl", "v") #엑셀의 데이터 복붙
    click(1086,694)

