Image :::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from PIL import Image as Im

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Im.open(file_name)
# возвращает значение в виде объекта типа Image
Im.new('RGBA', (100, 100), 'purple')
# создание нового объекта изображения
	alpha_composite(im, dest=(0, 0), source=(0, 0))
	# 

	crop((x1, y1, x2, y2))
	# обрезка области изображения
	
	copy()
	# возвращает новый объект Image с тем же изображением,
	# что и объект Image, для которого он был вызван
	
	paste(img_obj, (x, y))
	# помещает одно изображение поверх другого в точки верхнего
	# левого угла
	
	show()
	# показать изображение
	
	resize((x, y))
	# изменение размера изображения
	
	rotate(90, expand=True)
	# поварачивает изображение на 90 градусов против чесовой 
	# стрелки. Аргументом может быть целое или вещественное 
	# число. Аргумент expand приводит к увеличению размеров 
	# изображения таким образом, чтобы оно вписалось в 
	# ограничивающий прямоугольник нового повёрнутого изображения
	
	transpose(Image.FLIP_LEFT_RIGHT)
	# получить зеркальное отображение
		Image.FLIP_LEFT_RIGHT
		# изображение отражается по горизонтали
		Image.FLIP_TOP_BOTTOM
		# изображение отражается по вертикали
		Image.ROTATE_90
		Image.ROTATE_180
		Image.ROTATE_270
		# 
	getpixel((x, y))
	# получение цвета пикселя

	putpixel((x, y), ImageColor.getcolor('red', 'RGBA'))
	# установка цвета пикселя

	convert()
	#

	filter(ImageFilter.DETAIL)
	#

	load()
	#

	thumbnail((x, y))
	# создаёт превью в отличии от resize он сохраняет соотношение
	# сторон

	format
	# формат
	
	size
	# размеры
	mode
	# 
	filename
	# название изображения
	format_description
	# описание формата изображения
	save(file_name)
	# сохранение изменений файла

Im.alpha_composite(im1, im2)
# наложение im2 на im1 с сохранением alfa. Изображение должны
# быть одинаковыми.

Im.blend(im1, im2, alpha)
# создаёт новое изображение из im2 наложенного на im1. alfa
# задаёт прозрачность для im2.

Im.composite(image1, image2, mask)
# создаёт составное изображение путем смешивания изображений 
# с использованием маски. изображение mask может иметь режим 
# «1», «L» или «RGBA» и должено иметь тот же размер, что и два 
# других изображения.

Im.eval(image, *args)
# применяет функцию (которая должна принимать один аргумент) 
# к каждому пикселю в данном изображении. Если изображение 
# имеет более одной полосы, для каждой полосы применяется одна 
# и та же функция. image это входное изображение