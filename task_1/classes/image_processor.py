from PIL import ImageFilter, ImageOps  # Импортируем фильтры и операции для обработки изображений

class ImageProcessor:  # Определяем класс ImageProcessor для обработки изображений
    def __init__(self, image):  # Конструктор принимает объект изображения
        self.image = image  # Сохраняем изображение в атрибуте объекта

    def apply_sharpen(self):  # Метод для применения фильтра повышения резкости
        sharpened = self.image.filter(ImageFilter.SHARPEN)  # Применяем фильтр SHARPEN
        print("Фильтр SHARPEN применён")  # Сообщаем о применении фильтра
        return sharpened  # Возвращаем обработанное изображение

    def add_border(self, border_size=15, color="black"):  # Метод для добавления рамки
        bordered = ImageOps.expand(self.image, border=border_size, fill=color)  # Добавляем рамку указанного размера и цвета
        print(f"Добавлена рамка шириной {border_size}px")  # Сообщаем о добавлении рамки
        return bordered  # Возвращаем изображение с рамкой

