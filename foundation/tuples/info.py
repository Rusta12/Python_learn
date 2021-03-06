# 	/////////////////////////////////////////////////////////////
# 	Кортежи (tuple). ////////////////////////////////////////////

# 	Кортеж, по сути - неизменяемый список.

#	Кортеж определяется так же, как и список, но элементы 
# 	перечисляются в круглых скобках вместо квадратных.

#	Как и в списках, элементы в кортежах имеют определенный порядок. 
#	Точно так же нумерация элементов начинается с нуля, то есть 
# 	первым элементом непустого кортежа всегда является t[0].

#	Как и для списков, отрицательные индексы позволяют вести отсчет 
#	элементов с конца кортежа.

#	К кортежам, как и к спискам можно применить операцию среза. 
#	Обратите внимание, что срез списка — новый список, а срез 
#	кортежа — новый кортеж.

# 	Защищенный от изменений.
# 	Меньший размер получить размер (tuple._sizeof_()); 

	a = (1, 2, 3, 4, 5, 6) # 72
	b = [1, 2, 3, 4, 5, 6] # 88

#	- возможность использовать кортежи в качестве ключей словаря;

	d = {(1, 1, 1) : 1} # {(1, 1, 1): 1}
	d = {[1, 1, 1] : 1} # TypeError

# Работа с кортежами. ///////////////////////////////////////////

	test = tuple() 	# создали кортеж с помощью встроенной функции
	test2 = () 		# создали кортеж с помощью литерала кортежа
	test3 = 's', 	# можно и так, но лучше не использовать
