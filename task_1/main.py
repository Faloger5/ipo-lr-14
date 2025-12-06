# Доброва Анна

import sys  # Импортируем модуль sys для работы с путями
import os   # Импортируем модуль os для работы с файловой системой

# Добавляем путь к папке classes, чтобы можно было импортировать классы
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classes.image_handler import ImageHandler  # Импортируем класс ImageHandler
from classes.image_processor import ImageProcessor  # Импортируем класс ImageProcessor

def main():  # Главная функция программы
    path = input("Введите путь к изображению: ")  # Запрашиваем путь у пользователя
    handler = ImageHandler(path)  # Создаём объект класса ImageHandler

    img = handler.load_image()  # Загружаем изображение

    rotated = handler.rotate_45()  # Поворачиваем изображение на 45°

    output_jpg = "output.jpg"  # Имя файла для сохранения
    handler.image = rotated  # Обновляем текущее изображение
    handler.save_as_jpg(output_jpg)  # Сохраняем как JPG

    processor = ImageProcessor(rotated)  # Создаём объект ImageProcessor

    sharpened = processor.apply_sharpen()  # Применяем фильтр SHARPEN

    final_img = processor.add_border()  # Добавляем рамку

    final_img.save("final_result.jpg")  # Сохраняем итоговое изображение
    print("Финальное изображение сохранено: final_result.jpg")  # Сообщаем пользователю

if __name__ == "__main__":  # Проверяем, запущен ли файл напрямую
    main()  # Запускаем программу

