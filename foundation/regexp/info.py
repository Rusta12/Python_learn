# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Regular expresion


re.match('ex', 'example')
# проверяет, начинается ли источник с шаблона

re.compile('ex')
# для более сложных проверок нужно скомпилировать шаблон, 
# чтобы ускорить поиск

re.search()
# возвращает первое совпадение, если таковое имеется

re.findall()
# возвращает список всех непересекающихся совпадений, 
# если таковые имеются

re.split()
# разбивает источник на совпадения с шаблоном и возвращает 
# список всех фрагментов строки

re.sub()
# принимает аргумент для замены и заменяет все части источника, 
# совпа­вшие с шаблоном, на значение этого аргумента


re.findall('ex1|ex2', souce)
# поиск во всём тексте строки ex1 или ex2

re.findall('^ex1', source)
# поиск строки ex1 в начале текста

re.findall('ex2$', source)
# поиск строки ex2 в конце текста
