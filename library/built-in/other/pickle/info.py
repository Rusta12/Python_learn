pickle ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Этот модуль преобразует объект в последовательность байтов, которая может 
# быть записана в файл, а потом прочитана из файла. Модуль может работать 
# с большинством разновидностей обычных объектов Python, включая:
	
	# None
	
	# Числа и строки
	
	# Кортежи, списки и словари, содержащие объекты только тех типов, 
	# которые поддерживаются модулем pickle
	
	# Экземпляры пользовательских классов, объявленных в модуле на верхнем 
	# уровне

# документация на английском:
# https://docs.python.org/3/library/pickle.html

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from pickle import *

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

dump(obj, file, protocol=None, *, fix_imports=True)
# производит сериализа­цию объекта и записывает данные в указанный файл. В 
# параметре file указывается файловый объект, открытый на запись в бинарном 
# режиме.

load(file[, fix_imports-True][, encoding-"ASCII"][, errors-"strict"])
# читает данные из файла и преобразует их в объект. В параметре file 
# указы­вается файловый объект, открытый на чтение в бинарном режиме.


Pickler(file [, protocol][, fix_imports-True])
# Создает объект, который записывает данные в файловый объект, используя 
# указанный протокол сериализации.
	dump(x)
	# Записывает объект в файл.


Unpickler(file[, fix_imports-True][, encoding-'ASCII'][, errors-'strict'])
# Создает объект, который читает данные из файлового объекта.
	load()
	# загружает данные из файла и возвращает новый объект.


HIGHEST_PROTOCOL
# Атрибут, хранит идентификатор современного протокола


dumps(object [, protocol][, fix_imports-True])
# производит сериализацию объ­екта и возвращает последовательность байтов 
# специального формата. Формат зависит от указанного протокола - числа от 
# 0 до 4 в порядке от более старых к более новым и со­вершенным. По 
# умолчанию используется протокол 4.

loads(string, [, fix_imports-True][, encoding-'ASCII'][, errors-'strict'])
# преобразует последовательность байтов специального формата в объект.



# exceptions :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

PicklingError
# случились проблемы с сериализацией объекта

UnpicklingError
# случились проблемы с десериализацией объекта