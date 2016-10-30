# 	///////////////////////////////////////////////////////////
# 	OOP .......................................................

#	Объектно-ориентированное программирование (ООП) — парадигма 
#	программирования, в которой основными концепциями являются 
#	понятия объектов и классов.

#	Терминология ООП:.........................................

#	- Класс (Class): Определенный программистом прототип 
#	  программируемого объекта с набором атрибутов (переменных 
#	  и методов), которые описывают данный объект. Доступ к 
#	  аттрибутам и методам осуществляется через точку.

#	- Переменная класса (Class variable): Переменная, доступная 
#	  для всех экземпляров данного класса. Определяется внутри 
#	  класса, но вне любых методов класса.

#	- Экземпляр класса (Instance): Отдельный объект-представитель 
#	  определенного класса.

#	- Переменная экземпляра класса (Instance variable): Переменная 
#	  определенная внутри медота класса, принадлежащая только к 
#	  этому классу.

# 	- Метод (Method): Особая функция, определенная внутри класса.

#	- Наследование (Inheritance): Передача аттрибутов и методов 
#	  родительского класса дочерним классам.

#	- Перегрузка функций (Function overloading): Изменение 
#	  работы метода, унаследованного дочерним классом от 
#	  родительского класса.

#	- Перегрузка операторов (Operator overloading): Определение 
#	  работы операторов с экземплярами данного класса.

#	...........................................................

#	В python всё является объектами - и строки, и списки, и 
#	словари, и всё остальное.

#	Но возможности ООП в python этим не ограничены. Программист 
#	может написать свой тип данных (класс), определить в нём 
#	свои методы.

#	Это не является обязательным - мы можем пользоваться только 
#	встроенными объектами. Однако ООП полезно при долгосрочной 
#	разработке программы несколькими людьми, так как упрощает 
#	понимание кода.

#	Попробуем определить собственный класс:

	class A:
		pass

#	Теперь мы можем создать несколько экземпляров этого класса:

	a = A()
	b = A()
	a.arg = 1  		# у экземпляра a появился атрибут arg, равный 1
	b.arg = 2  		# а у экземпляра b - атрибут arg, равный 2
	print(a.arg) 	# 1

#	Классу возможно задать собственные методы:

	class A:

		def g(self):
		# self - обязательный аргумент, содержащий в себе экземпляр
		# класса, передающийся при вызове метода, поэтому этот 
		# аргумент должен присутствовать во всех методах класса.

			return 'hello world'

	a = A()
	a.g() 		#'hello world'

#	И напоследок еще один пример:

	class B:

		arg = 'Python'
		# Все экземпляры этого класса будут иметь атрибут arg,
		# равный "Python" Но впоследствии мы его можем изменить

		def g(self):
			return self.arg

	b = B()
	b.g() 		# 'Python'
	B.g(b) 		# 'Python'
	b.arg = 'spam'
	b.g() 		# 'spam'

#	Конструктор и деструктор....................................

#	Специальные методы вызываются при создании экземпляра класса 
#	(конструктор) и при удалении класса (деструктор). В языке 
#	Python реализовано автоматическое управление памятью, 
#	поэтому деструктор требуется достаточно редко, для ресурсов, 
#	требующих явного освобождения.

#	Следующий класс имеет конструктор и деструктор:

	class Line:
    	def __init__(self, p1, p2):
        	self.line = (p1, p2)

    	def __del__(self):
        	print "Удаляется линия %s - %s" % self.line

	l = Line((0.0, 1.0), (0.0, 2.0))
	del l #	Удаляется линия (0.0, 1.0) - (0.0, 2.0)

#	В момент вызова деструктора (например, по завершении программы) 
#	среда исполнения может быть уже достаточно «истощённой»[что?], 
#	поэтому в деструкторе следует делать только самое необходимое. 
#	Кроме того, не обработанные в деструкторе исключения игнорируются.

#	Время жизни объекта ........................................

#	Обычно время жизни объекта, определённого в программе на Python, 
#	не выходит за рамки времени выполнения процесса этой программы.

#	Для преодоления этого ограничения объект можно сохранить, а 
#	после — восстановить. Как правило, при записи объекта 
#	производится его сериализация, а при чтении — десериализация.

	import shelve
	s = shelve.open("somefile.db")
	s['myobject'] = [1, 2, 3, 4, 'свечка']
	s.close()

	import shelve
	s = shelve.open("somefile.db")
	print s['myobject']
	# [1, 2, 3, 4, '\xd1\x81\xd0\xb2\xd0\xb5\xd1\x87\xd0\xba\xd0\xb0']

