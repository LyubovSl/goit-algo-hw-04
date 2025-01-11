from pathlib import Path

def get_cats_info(path):
     # Створення об'єкта Path для файлу
    file_path = Path(path)
    
    # Читання тексту з файлу
    try:
        with file_path.open("r", encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]

        # Створення списку словників
        cats_list = []
        for entry in lines:
            # Розділення рядка за комою
            cat_id, name, age = entry.split(',')
            # Додавання до списку словника
            cats_list.append({
                "id": cat_id,
                "name": name,
                "age": int(age)
            })
        return cats_list
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено!")
    except ValueError:
        print("Помилка в обробці даних. Перевірте формат файлу.")

file_path =  "cats_list.txt"
cats_info = get_cats_info(file_path)  
print(cats_info)     