import os
import shutil
from concurrent.futures import ThreadPoolExecutor

def process_folder(folder_path):
    # Отримуємо список файлів у папці
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    # Сортуємо файли за розширеннями
    extensions = set(os.path.splitext(f)[1] for f in files)
    for ext in extensions:
        ext_folder = os.path.join(folder_path, ext.lstrip('.'))
        os.makedirs(ext_folder, exist_ok=True)
        for f in files:
            if os.path.splitext(f)[1] == ext:
                shutil.move(os.path.join(folder_path, f), os.path.join(ext_folder, f))
    
    print(f"Сортування завершено для папки {folder_path}")

def main():
    target_folder = "/home/yurs/Документи/Go_IT_Project_poetry/My_project/trash" # Шлях до цільової папки
    
    # Отримуємо список підпапок
    subfolders = [os.path.join(target_folder, d) for d in os.listdir(target_folder) if os.path.isdir(os.path.join(target_folder, d))]
    
    # Виконуємо обробку кожної підпапки в окремому потоці
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(process_folder, subfolders)

if __name__ == "__main__":
    main()
