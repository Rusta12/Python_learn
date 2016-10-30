#	////////////////////////////////////////////////////////////
# 	методы работы со словарём //////////////////////////////////

	dict.clear()
	# очищает словарь.

	dict.copy()
	# возвращает копию словаря.

	dict.items()
	# возвращает пары (ключ, значение).

	dict.keys()
	# возвращает ключи в словаре.
	
	dict.popitem()	
	# удаляет и возвращает пару (ключ, значение). Если словарь 
	# пуст, бросает исключение KeyError. Помните, что словари 
	# неупорядочены.

	dict.values()
	# возвращает значения в словаре.

	dict.update([other])	
	# обновляет словарь, добавляя пары (ключ, значение) из other. 
	# Существующие ключи перезаписываются. Возвращает None 
	# (не новый словарь!).

	classmethod dict.fromkeys(seq[, value])	
	# создает словарь с ключами из seq и значением value 
	# (по умолчанию None).

	dict.get(key[, default])	
	# возвращает значение ключа, но если его нет, не бросает 
	# исключение, а возвращает default (по умолчанию None).

	dict.pop(key[, default])	
	# удаляет ключ и возвращает значение. Если ключа нет, 
	# возвращает default (по умолчанию бросает исключение).

	dict.setdefault(key[, default])	
	# возвращает значение ключа, но если его нет, не бросает 
	# исключение, а создает ключ с значением default 
	# (по умолчанию None).