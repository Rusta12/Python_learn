#	////////////////////////////////////////////////////////////////
#	Манипуляции с формой ...........................................

#	Как уже говорилось, у массива есть форма (shape), определяемая 
#	числом элементов вдоль каждой оси:

	a
	# array([[[  0,   1,   2],
	# 		[ 10,  12,  13]],

	# 	   [[100, 101, 102],
	# 		[110, 112, 113]]])

	a.shape 	# (2, 2, 3)

#	Форма массива может быть изменена с помощью различных команд:

	a.ravel()  # Делает массив плоским
	# array([  0,   1,   2,  10,  12,  13, 100, 101, 102, 110, 112, 113])

	a.shape = (6, 2)  # Изменение формы
	a
	# array([[  0,   1],
	# 	   [  2,  10],
	# 	   [ 12,  13],
	# 	   [100, 101],
	# 	   [102, 110],
	# 	   [112, 113]])

	a.transpose()  # Транспонирование
	# array([[  0,   2,  12, 100, 102, 112],
	# 	   [  1,  10,  13, 101, 110, 113]])

	a.reshape((3, 4))  # Изменение формы
	# array([[  0,   1,   2,  10],
	# 	   [ 12,  13, 100, 101],
	# 	   [102, 110, 112, 113]])

#	Порядок элементов в массиве в результате функции ravel() 
#	соответствует обычному "C-стилю", то есть, чем правее индекс, 
#	тем он "быстрее изменяется": за элементом a[0,0] следует a[0,1]. 
#	Если одна форма массива была изменена на другую, массив 
#	переформировывается также в "C-стиле". Функции ravel() и reshape() 
#	также могут работать (при использовании дополнительного аргумента)
#	в FORTRAN-стиле, в котором быстрее изменяется более левый индекс.

	a
	# array([[  0,   1],
	# 	   [  2,  10],
	# 	   [ 12,  13],
	# 	   [100, 101],
	# 	   [102, 110],
	# 	   [112, 113]])

	a.reshape((3, 4), order='F')
	# array([[  0, 100,   1, 101],
	# 	   [  2, 102,  10, 110],
	# 	   [ 12, 112,  13, 113]])

#	Метод reshape() возвращает ее аргумент с измененной формой, в то 
#	время как метод resize() изменяет сам массив:

	a.resize((2, 6))
	a
	# array([[  0,   1,   2,  10,  12,  13],
	# 	   [100, 101, 102, 110, 112, 113]])

#	Если при операции такой перестройки один из аргументов задается 
#	как -1, то он автоматически рассчитывается в соответствии с 
#	остальными заданными:

	a.reshape((3, -1))
	# array([[  0,   1,   2,  10],
	# 	   [ 12,  13, 100, 101],
	# 	   [102, 110, 112, 113]])