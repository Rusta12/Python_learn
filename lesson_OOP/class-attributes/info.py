#	///////////////////////////////////////////////////////////////
#	Атрибуты класса................................................

#	Атрибуты класса бывают двух видов:

#	- атрибуты данных;
#	- атрибуты-методы.

#	Атрибуты данных обычно записываются сверху. Память для атрибутов 
#	выделяется в момент их первого присваивания — либо снаружи, либо 
#	внутри метода. Методы начинаются со служебного слова def.

#	Доступ к атрибутам выполняется по схеме obj.attrname.

	class Simple:
		'''Простой класс'''
		
		var = 87
		def f(x):
			return 'Hello world'

#	Здесь Simple.var и Simple.f — пользовательские атрибуты. Есть 
#	также стандартные атрибуты:

	print Simple.__doc__ 	# Простой класс

#	Целое число
	
	print Simple.var.__doc__ 	# int(x[, base]) -> integer

#	Создание экземпляра класса похоже на то, как будто мы делаем вызов 
#	функций:
	
	smpl = Simple()
	
#	Будет создан пустой объект smpl. Если мы хотим, чтобы при создании 
#	выполнялись какие-то действия, нужно определить конструктор, 
#	который будет вызываться автоматически:
	
	class Simple:
		def __init__(self):
			self.list = []
	
#	При создании объекта smpl будет создан пустой список list. 
#	Конструктору можно передать аргументы:

	class Simple:
		def __init__(self, count, str):
			self.list = []
			self.count = count
			self.str = str
 
	s = Simple(1,'22')
	s.count, s.str 		# 1 22

#	Атрибут данных можно сделать приватным (private) — т.е. недоступным 
#	снаружи — для этого слева нужно поставить два символа подчеркивания:

	class Simple:
		'''Простой класс с приватным атрибутом'''
	
		__private_attr = 10 
		def __init__(self, count, str):
			self.__private_attr = 20
			print self.__private_attr
 
	s = Simple(1,'22')
	print s.__private_attr

#	Последняя строка вызовет исключение — атрибут __private_attr годен 
#	только для внутреннего использования.

#	Методы необязательно определять внутри тела класса:

	def method_for_simple(self, x, y):
		return x + y

	class Simple:
		f = method_for_simple

	s = Simple()
	print s.f(1,2) 	# 3

#	Пустой класс можно использовать в качестве заготовки для структуры 
#	данных:

	class Customer:
		pass
		
	custom = Customer()
	custom.name = 'Вася'
	custom.salary = 100000