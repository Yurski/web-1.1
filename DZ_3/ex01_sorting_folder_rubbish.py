import os
from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict
import shutil

def sort_files_by_extension(directory):
    # Створюємо словник для збереження файлів за їх розширенням
    file_extensions = defaultdict(list)

    # Перебираємо файли в директорії
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Отримуємо розширення файлу
            _, extension = os.path.splitext(file)
            # Додаємо файл до списку файлів з цим розширенням
            file_extensions[extension].append(file_path)

    # Переносимо файли у відповідні папки за їх розширенням
    with ThreadPoolExecutor() as executor:
        for extension, files in file_extensions.items():
            # Створюємо папку для розширення, якщо вона ще не існує
            extension_dir = os.path.join(directory, extension[1:])  # Видаляємо крапку з початку розширення
            os.makedirs(extension_dir, exist_ok=True)
            # Переносимо файли у відповідну папку
            executor.map(shutil.move, files, [extension_dir] * len(files))

if __name__ == "__main__":
    directory = "/home/yurs/Документи/trash"  # Шлях до папки "Хлам"
    sort_files_by_extension(directory)
