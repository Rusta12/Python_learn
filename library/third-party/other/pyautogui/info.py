PyAutoGUI :::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Кросс-платформенная автоматизация графического интерфейса для 
# людей. Способен посылать сигналы виртуальных нажатий клавиш и 
# щелчков мышью операционным системам Windows, Linux, OSX. 

# документация на английском:
# https://pyautogui.readthedocs.io/en/latest/

# установка:
pip install python-xlib pyautogui

# для скниншотов (только в Linux)
sudo apt install scrot

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import pyautogui as pg

# constants :::::::::::::::::::::::::::::::::::::::::::::::::::::::

pg.MINIMUM_DURATION
# устанавливает время задержки для перемещение мыши

pg.PAUSE
# устанавливаю паузу после каждого вызова функции в секундах

pg.FAILSAFE = True 
# активирует средство безопасного выхода из программы

pg.KEYBOARD_KEYS
# получение списка клавиш



# general :::::::::::::::::::::::::::::::::::::::::::::::::::::::::

pg.size()
# возвращает кортеж из двух целых чисел, представляющих ширину и 
# высоту экрана в пикселях

pg.position()
# возвращает кортеж из двух целых чисел, представляющих координаты
# текущей позиции указателя

pg.onScreen(x, y)
# возвращает True если x и y находятся в пределах экрана

pg.pixelMatchesColor(x, y, 'RGBA', tolerance=10)
# возвращает значение True, если цвет пикселя с заданными экранными
# координатами x и y совпадают с заданным цветом
# tolerance задаёт насколько каждый цвет может не совподать



# screenshot ::::::::::::::::::::::::::::::::::::::::::::::::::::::

pg.screenshot('ex.png', region=(x,y, width, height))
# делает снимок экрана. Необзательный аргумент файл, если требуется
# задать имя. region необязательный аргумент, область захвата
	getpixel((x, y))
	# получить цвет RGB пикселя на скриншоте

pg.locateOnScreen('file_name.png', grayscale=False)
# возвратит координаты местонахождения этого изображения на экране
# кортеж из четырёх целых чисел возвращаемый функцией, предоставляет
# x-координату левого края, y-координату верхнего края, а также 
# ширину и высоту изображения в первой из позиций на экране, в 
# которой оно обнаруженно. Обратите внимание на то, что для того
# чтобы изображение на экране было успешно распознано, оно должно
# в точности совпадать с представленным изображением. Если оно
# отличается хотябы одним пикселем, то функция вернёт None.
	grayscale
	# если True увеличивает поиск на 30%, но потенциально вызывая 
	# ложноположительные совпадения.

pg.locateCenterOnScreen(image, grayscale=False)
# Возвращает (x, y) координаты центра первого найденного экземпляра 
# изображения на экране. Возвращает None, если не найден на экране.

pg.locateAllOnScreen('file_name.png', grayscale=False)
# находит координаты изображения во всех частях экрана. Она 
# возвращает объект Generator 

pg.locate(needleImage, haystackImage, grayscale=False)
# Возвращает (x, y, width, height) координату первого найденного 
# экземпляра needleImage в haystackImage. Возвращает None, если не 
# найден на экране.

pg.locateAll(needleImage, haystackImage, grayscale=False)
# Возвращает генератор, который дает (x, y, width, height) кортежи, 
# для которых needleImage находится в haystackImage.

pg.center((x, y, width, height))
# возвращает центер переданных координат 



# мышь ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

pg.moveTo(x, y, duration)
# немедленно перемещает указатель в указанную позицию на экране
# x и y координаты. Необязательный именнованный аргумент duration
# в виде целого или вещественного числа задаёт (в секундах) 
# длительность перемещения указателя в конечную точку. Если его не
# указывать, то duration присваивается значение 0, что приводит к
# мгнавенному перемещению указателя.

pg.moveTo(x, y, duration, pg.easeInQuad)     # start slow, end fast
pg.moveTo(x, y, duration, pg.easeOutQuad)    # start fast, end slow
pg.moveTo(x, y, duration, pg.easeInOutQuad)  # start and end fast, slow in middle
pg.moveTo(x, y, duration, pg.easeInBounce)   # bounce at the end
pg.moveTo(x, y, duration, pg.easeInElastic)  # rubber band at the end

pg.moveRel(x, y, duration)
# перемещает указатель мыши относительно его текущей позиции
# x,y перемещение указателя вправо по горизонтали и вниз по 
# вертикали, отрицатильные значения задают обратный направления

pg.click(x, y, clicks=3, interval=0.24, button)
# отправить компьютеру виртуальный щелчок мышью, по умолчанию
# предпологается что это щелчок левой кнопкой мыши, в месте 
# текущего указателя мыши. Необязательные аргументы x и y указывают
# где вызвать щелчок. 
# Необязательный именнованный аргумент button указывает какой 
# кнопкой происходит нажатие, могут быть следующие значения
# left, right, middle

pg.mouseDown(x, y, button)
# соответствует лишь нажатие кнопки

pg.mouseUp(x, y, button)
# соответствует лишь отжатие кнопки

pg.doubleClick(x, y)
# выполняет двойной щелчок левой кнопки мыши

pg.rightClick(x, y)
# выполняет нажатие правой кнопки мыши

pg.middleClick(x, y)
# выполняет нажатие средней кнопки мыши

pg.dragTo(x, y, duration)
# перетаскивает нажатый указатель мыши в новое место

pg.dargRel(x, y, duration)
# перетаскивает нажатый указатель мыши в местоположение 
# относительно текущего.

pg.scroll(200, x=moveToX, y=moveToY)
# принимает целочисленный аргумент, определяющий количество единиц 
# прокрутки в направлении вверх или вниз. Прокрутка осуществляется 
# в текущей позиции курсора. Положительное значение означает 
# прокртку вверх, отрицательное вниз.
# x и y необязательные аргументы которые устанавлмвают курсор мыши
# перед скролом в заданную область.

pg.hscroll(200)
# горизонтальный скрол. Положительное вправо, отрицательное
# влево



# клавиатура ::::::::::::::::::::::::::::::::::::::::::::::::::::::

pg.typewrite(message, interval=0.25)
# посылает компьютеру виртуальные компьютерные нажатия. 
# Необязательный аргумент интервал задаёт задержку между символами
# в качестве message может выступать либо слово, либо список 
# названий клавиш, пример: 'left', 'right', полный список можно
# увидеть командой pg.KEYBOARD_KEYS

pg.keyDown()
# посылает виртуальное нажатие клавиш

pg.keyUp()
# посылает виртуальное отжатие клавиш

pg.press(['enter', 'enter'])
# посылает нажатие клавиши 'enter'

pg.hotkey('ctrl', 'c')
# принимает несколько строковых аргументов, обозначающих клавиши, 
# выполняет виртуальное нажатие клавиш в указанном парядке, а затем
# отпускает их в обратном порядке


# список клавиш
['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']



# оконные сообщения :::::::::::::::::::::::::::::::::::::::::::::::

alert(text='', title='', button='OK')
# Отображает простое окно с текстом и одну кнопку OK. Возвращает 
# текст нажатой кнопки.

confirm(text='', title='', buttons=['OK', 'Cancel'])
# Отображает окно сообщения с кнопками «ОК» и «Отмена». Номер и 
# текст кнопок можно настроить. Возвращает текст нажатой кнопки.

prompt(text='', title='' , default='')
# Отображает окно сообщения с текстовым вводом и кнопки «ОК» и 
# «Отмена». Возвращает введенный текст или None, если нажата 
# кнопка «Отмена».

password(text='', title='', default='', mask='*')
# Отображает окно сообщения с текстовым вводом и кнопки «ОК» и 
# «Отмена». Типизированные символы отображаются как *. Возвращает 
# введенный текст или None, если нажата кнопка «Отмена».



# 