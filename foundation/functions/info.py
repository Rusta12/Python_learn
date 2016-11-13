# 	////////////////////////////////////////////////////////////
# 	Функции (function). ////////////////////////////////////////

#	Функция это блок организованного, многократно используемоего 
#	кода, который используется для выполнения конкретного задания. 

#	Создание функции............................................

#	- Блок функции начинается с ключевого слова def, после которого 
#	  следуют название функции и круглые скобки ().

#	- Любые аргументы, которые принимает функция должны находиться 
#	  внутри этих скобок.

#	- После скобок идет двоеточие ( : ) и с новой строки с отступом 
#	  начинается тело функции.

	def my_function(argument):
    	print argument

#	Вызов функции................................................

#	После создания функции, ее можно исполнять вызывая из другой 
#	функции или напрямую из оболочки Python. Для вызова функции 
#	следует ввести ее имя и добавить скобки.

	my_function("abracadabra")

#	Аргументы функции............................................

#	Вызывая функцию, мы можем передавать ей следующие типы аргументов:

#	- Обязательные аргументы (Required arguments)
#	- Аргументы-ключевые слова (Keyword argument)
#	- Аргументы по умолчанию (Default argument)
#	- Аргументы произвольной длины (Variable-length argumens)

#	Обязательные аргументы функции:..............................

#	Если при создании функции мы указали количество передаваемых ей 
#	аргументов и их порядок, то и вызывать ее мы должны с тем же 
#	количеством аргументов, заданных в нужном порядке.

	def bigger(a,b):
    	if a > b:
        	print a
    	else:
       		print b
 
	bigger(5,6)
  
#	Аргументы - ключевые слова:..................................

#	Аргументы - ключевые слова используются при вызове функции. 
#	Благодаря ключевым аргументам, вы можете задавать произвольный 
#	(то есть не такой каким он описан при создании функции) порядок 
#	аргументов.

	def person(name, age):
    	print name, "is", age, "years old"
 
#	Хотя в описании функции первым аргументом идет имя, мы можем 
#	вызвать функцию вот так
 
	person(age=23, name="John")


#	Аргументы, заданные по-умолчанию:.............................

#	Аргумент по умолчанию, это аргумент, значение для которого задано 
#	изначально, при создании функции.

	def space(planet_name, center="Star"):
    	print planet_name, "is orbiting a", center
 
#	Можно вызвать функцию space так:

	space("Mars")	# Mars is orbiting a Star
 
#	Можно вызвать функцию space иначе:

	space("Mars", "Black Hole") # В результате получим: 
								# Mars is orbiting a Black Hole

#	Аргументы произвольной длины:.................................

#	Иногда возникает ситуация, когда вы заранее не знаете, какое 
#	количество аргументов будет необходимо принять функции. В этом 
#	случае следует использовать аргументы произвольной длины. Они 
#	задаются произвольным именем переменной, перед которой ставится 
#	звездочка (*).

	def unknown(*args):
    	for argument in args:
        	print argument
 
	unknown("hello","world") # напечатает оба слова, каждое с новой строки
	unknown(1,2,3,4,5) # напечатает все числа, каждое с новой строки
	unknown() # ничего не выведет

# 	args - это кортеж из всех переданных аргументов функции, 
# 	и с переменной можно работать также, как и с кортежем.

#	Произвольное число именованных аргументов....................

# 	Функция может принимать и произвольное число именованных 
# 	аргументов, тогда перед именем ставится **

	def func(**kwargs):
		return kwargs

	func(a=1, b=2, c=3)		# {'a': 1, 'c': 3, 'b': 2}

# 	В переменной kwargs у нас хранится словарь.

#	Ключевое слово return.........................................

#	Выражение return прекращает выполнение функции и возвращает 
#	указанное после выражения значение. Выражение return без 
#	аргументов это то же самое, что и выражение return None. 
#	Соответственно, теперь становится возможным, например, 
#	присваивать результат выполнения функции какой либо переменной.

	def bigger(a,b):
    	if a > b:
        	return a 	# Если a больше чем b, то возвращаем a и 
        				# прекращаем выполнение функции

    	return b 	# Незачем использовать else. Если мы дошли до 
    				# этой строки, то b, точно не меньше чем a
 
#	присваиваем результат функции bigger переменной num

	num = bigger(23,42)

#	Область видимости.............................................

#	Некоторые переменные скрипта могут быть недоступны некоторым 
#	областям программы. Все зависит от того, где вы объявили эти 
#	переменные.

#	В Python две базовых области видимости переменных:

#	- Глобальные переменные
#	- Локальные переменные

#	Переменные объявленные внутри тела функции имеют локальную 
#	область видимости, те что объявлены вне какой-либо функции 
#	имеют глобальную область видимости.

#	Это означает, что доступ к локальным переменным имеют только 
#	те функции, в которых они были объявлены, в то время как доступ 
#	к глобальным переменным можно получить по всей программе в 
#	любой функции.


#	глобальная переменная age
	
	age = 44
 
	def info():
    	print age 	# Печатаем глобальную переменную age
 
	def local_info():
    	age = 22 	# создаем локальную переменную age 
    	print age
 
	info() # напечатает 44
	local_info() # напечатает 22

#	Важно помнить, что для того чтобы получить доступ к глобальной 
#	переменной, достаточно лишь указать ее имя. Однако, если перед 
#	нами стоит задача изменить глобальную переменную внутри 
#	функции - необходимо использовать ключевое слово global.


#	глобальная переменная age

	age = 13
 
#	функция изменяющая глобальную переменную

	def get_older():
		global age
   		age += 1
 
	print age 	# напечатает 13
	get_older() # увеличиваем age на 1
	print age 	# напечатает 14

#	Рекурсия......................................................

#	Рекурсией в программировании называется ситуация, в которой 
#	функция вызывает саму себя. Классическим примером рекурсии 
#	может послужить функция вычисления факториала числа.

#	Факториалом числа, например, 5 является произведение всех 
#	натуральных (целых) чисел от 1 до 5. То есть, 1 * 2 * 3 * 4 * 5

#	Рекурсивная функция вычисления факториала на языке Python будет 
#	выглядеть так:

	def fact(num):
    	if num == 0: 
        	return 1 # По договоренности факториал нуля равен единице
    	else:
        	return num * fact(num - 1) 	# возвращаем результат произведения 
        								# num и результата возвращенного 
        								# функцией fact(num - 1)

#	Однако следует помнить, что использование рекурсии часто может 
#	быть неоправданным. Дело в том, что в момент вызова функции в 
#	оперативной памяти компьютера резервируется определенное количество 
#	памяти, соответственно чем больше функций одновременно мы запускаем 
#	- тем больше памяти потребуется, что может привести к переполнению 
#	стека (stack overflow) и программа завершится аварийно, не так как 
#	предполагалось. Учитывая это, там где это возможно, вместо рекурсии 
#	лучше применять циклы.

#	Рецепт создания функции в Python..............................

#	Существует следующий алгоритм - рекомендация по созданию функции 
#	в Python. Например, мы создаем функцию вычисления площади 
#	прямоугольника.

#	Начинать следует с примеров того, что делает функция, и подобрать 
#	подходящее название. В нашем случае это будет выглядеть так:

# 	На данном этапе мы еще не указываем имена переменных

	def rectangle_area_finder( ):

    rectangle_area_finder(3, 5)	# 15
    rectangle_area_finder(17.2, 6)	# 103.2

#	Указать типы данных, которые принимает функция и тип данных, 
#	который она возвращает

#	функция принимает два числа, а возвращает одно
	def rectangle_area_finder( ):
    	'''(num, num) -> num'''
 
    rectangle_area_finder(3, 5)	# 15
    rectangle_area_finder(17.2, 6)	# 103.2

#	Подобрать подходящие названия для переменных

#	Поскольку это математическая функция нам вполне подойдут 
#	имена a и b

	def rectangle_area_finder(a, b):
    	'''(num, num) -> num'''
     
    rectangle_area_finder(3, 5)	# 15
    rectangle_area_finder(17.2, 6)	# 103.2

#	Написать краткое, но содержательное описание функции

	def rectangle_area_finder(a, b):
    	'''(num, num) -> num'''
 
    # Returns an area of a rectangle with given sides a and b.    
 
    rectangle_area_finder(3, 5)	# 15
    rectangle_area_finder(17.2, 6)	# 103.2

#	Написать собственно тело функции

	def rectangle_area_finder(a, b):
    	'''(num, num) -> num'''
 
    # Returns an area of a rectangle with given sides a and b.    
 
    rectangle_area_finder(3, 5) # 15
    rectangle_area_finder(17.2, 6) # 103.2

    return a * b

#	Функция готова! Осталось вызвать ее с указанными в примерах аргументами

#	При вызове команды help() с именем нашей функции в качестве аргумента 
#	мы получаем написанную нами документацию. Сопровождайте ваши функции 
#	качественной документацией и программисты, которые будут работать с 
#	вашим кодом после вас будут вам благодарны.

# 	Анонимные функции, инструкция lambda...............................

# 	Анонимные функции могут содержать лишь одно выражение, но и 
# 	выполняются они быстрее. Анонимные функции создаются с помощью 
# 	инструкции lambda. Их не обязательно присваивать переменной, 
# 	как c инструкцией def func()

	func = lambda x, y: x + y
	(lambda x, y: x + y)(1, 2)
	(lambda x, y: x + y)('a', 'b')

#	lambda функции, в отличие от обычной, не требуется инструкция 
# 	return, а в остальном, ведет себя точно так же.

	func = lambda *args: args