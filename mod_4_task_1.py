from pathlib import Path

def total_salary(path):
    # Створення об'єкта Path для файлу
    file_path = Path(path)
    
    # Читання тексту з файлу
    try:
        with file_path.open("r", encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]
        
        # Обчислення загальної та середньої зарплати
        total = sum(int(item.split(',')[1]) for item in lines)
        average = total / len(lines)
        
        print(f"Загальна сума заробітної плати: {total}")
        print(f"Середня заробітна плата: {average}")
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено!")
    except ValueError:
        print("Помилка в обробці даних. Перевірте формат файлу.")

# Виклик функції
file_path = "salary_list.txt"
total_salary(file_path)

