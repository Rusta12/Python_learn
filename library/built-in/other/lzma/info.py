lzma ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Этот модуль предоставляет классы и удобные функции для сжатия и 
# распаковки данных с использованием алгоритма сжатия LZMA. Также включен 
# файловый интерфейс, поддерживающий форматы .xz и .lzma, используемые 
# утилитой xz, а также необработанные сжатые потоки 

# документация на английском:
# https://docs.python.org/3/library/lzma.html 

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from lzma import *

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

open(filename, mode="rb", *, format=None, check=-1, preset=None, 
	filters=None, encoding=None, errors=None, newline=None)
# возвращает объект класса LZМAFile, представляющий созданный или от­крытый 
# архивный файл.
	format 
	# задает формат создаваемого или открываемого архивного файла. Здесь 
	# доступны следующие значения:
		lzma.FORМAT_AUTO
		# формат выбирается автоматически. Может быть задан только при открытии 
		# существующего файла, и в этом случае является значением по умолчанию
		lzma.FORМAT_XZ
		# новая разновидность формата (расширение файлов - .xz). Значение по 
		# умолчанию при создании архивного файла
		lzma.FORMAT_ALONE
		# старая разновидность формата (расширение файлов - .lzma)
		lzma.FORMAT_RAW
		# никакой формат не используется, и в файл записывается «сырой» набор 
		# данных
	check 
	# определяет тип проверки целостности архива - его имеет смысл задавать
	# лишь при создании архивного файла. Доступные значения:
		lzma.CHECK_NONE
		# проверка на целостность не проводится. Значение по умолчанию и 
		# единственное доступное значение для форматов 1zma.FORМAT_ALONE и 
		# lzma.FORМAT_RAW
		lzma.CHECK_CRC32
		# 32-разрядная циклическая контрольная сумма
		lzma.CHECK_CRC64
		# 64-разрядная циклическая контрольная сумма. Значение по умол­чанию 
		# для формата lzma.FORМAT_XZ
		lzma.CHECK_SHA256
		# хеширование по алгоритму SНА256
	preset 
	# указывает используемый при сжатии или распаковке набор параметров 
	# архиватора, фактически - степень сжатия. Доступны числовые значения от 
	# О (минималь­ное сжатие и высокая производительность) до 9 (максимальное 
	# сжатие и низкая производи­тельность). Этот параметр имеет смысл задавать 
	# лишь при создании архивного файла. Зна­чение по умолчанию - 
	# lzma.PRESET_DEFAULT, соответствующее числу 6.
	filters 
	# задает набор дополнительных фильтров, используемых при архивирова­нии и 
	# распаковке. Отметим, что для формата lzma.FORМAT_RAW фильтр требуется 
	# указать обязательно.




LZMAFile(filename=None, mode="r", *, format=None, check=-1, preset=None, 
	filters=None)
#
	peek(size=-1)
	#



LZMACompressor(format=FORMAT_XZ, check=-1, preset=None, filters=None)
# Для сжатия и данных по частям
	compress(data)
	# сжимает переданные в качестве параметра данные и возвращает результат 
	# сжатия как массив байтов типа bytes
	flush()
	# завершает процесс сжатия переданных ранее данных и возвращает 
	# результат их сжатия, оставшийся во внутренних буферах. Должен 
	# вызываться в любом случае по­сле окончания сжатия



LZMADecompressor(format=FORMAT_AUTO, memlimit=None, filters=None)
# Для распаковки данных сделаных с помощью LZMACompressor.
# Параметр memlimit устанавливает максимальный размер памяти в байтах, 
# который может быть использован архиватором. По умолчанию этот размер не
# ограничен. Отметим, что в случае задания параметра memlimit, если 
# архиватор не сможет уложиться в отведенный ему объем памяти, будет 
# возбуждено искmочение LZМAError, класс которого объявлен в модуле
# lzma.
	decompress(data, max_length=-1)
	# распаковывает переданные в качестве параметра сжатые дан­ные и 
	# возвращает результат распаковки
	eof
	# возвращает True, если в переданных сжатых данных присутствует 
	# сигнатура кон­ца архива, т.е., если данные закончились
	unused_data
	# возвращает «лишние» данные, присутствующие после сигнатуры конца
	# архива
	needs_input
	#



compress(data, format=FORMAT_XZ, check=-1, preset=None, filters=None)
#

decompress(data, format=FORMAT_AUTO, memlimit=None, filters=None)
#



is_check_supported(check)
#




# Filters :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Спецификатор цепочки фильтров представляет собой последовательность 
# словарей, где каждый словарь содержит идентификатор и параметры для 
# одного фильтра. Каждый словарь должен содержать ключ «id» и может 
# содержать дополнительные ключи для указания зависимых от фильтра 
# параметров. Допустимые идентификаторы фильтра:

# Фильтры сжатия:
FILTER_LZMA1 	# (для FORMAT_ALONE)
FILTER_LZMA2 	#(для FORMAT_XZ и FORMAT_RAW)

# Дельта-фильтр:
FILTER_DELTA

# Фильтры Branch-Call-Jump (BCJ):
FILTER_X86
FILTER_IA64
FILTER_ARM
FILTER_ARMTHUMB
FILTER_POWERPC
FILTER_SPARC

# Цепь фильтра может состоять из 4 фильтров и не может быть пустым. 
# Последний фильтр в цепочке должен быть фильтром сжатия, а любые другие 
# фильтры должны быть дельта-или BCJ-фильтрами.

# ::::::::::::::::::

# Фильтры сжатия поддерживают следующие параметры (указанные в качестве 
# дополнительных записей в словаре, представляющем фильтр):

preset
# Предустановка сжатия для использования в качестве источника значений 
# по умолчанию для опций, которые явно не указаны.

dict_size
# Размер словаря в байтах. Это должно быть между 4 KiB и 1,5 GiB 
# (включительно).

lc
# число литералов

lp
# Количество битов позиции. Сумма lc + lp должна быть не более 4.

pb
# Количество бит позиции; должно быть не более 4.

mode
# MODE_FAST или MODE_NORMAL

nice_len
# Что следует считать «nice length» для match. Это должно быть 273 или 
# меньше.
 
mf
# Какой подходящий finder использовать - MF_HC3, MF_HC4, MF_BT2, 
# MF_BT3 или MF_BT4.

depth
# Максимальная глубина поиска, используемая поиском соответствия. 0 
# (по умолчанию) означает автоматический выбор на основе других параметров 
# фильтра.





# exceptions ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

LZMAError
# Это исключение возникает при возникновении ошибки во время сжатия или 
# декомпрессии или при инициализации состояния компрессора/декомпрессора.