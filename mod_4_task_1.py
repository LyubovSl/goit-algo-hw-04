from pathlib import Path

def total_salary(path):
    # Створення об'єкта Path для файлу
    file_path = Path(path)
    
    # Читання тексту з файлу
    try:
        with file_path.open("r", encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]
        
        # Обчислення загальної та середньої зарплати
        if not lines:
            return 0, 0  # Повертає 0, якщо файл порожній
        
        salaries = []
        for line in lines:
            try:
                name, salary = line.split(',')
                salaries.append(float(salary))
            except ValueError:
                print(f"Некоректний рядок у файлі: {line}")
        
        total = sum(salaries)
        average = total / len(salaries) if salaries else 0
        
        return total, average
        
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено!")
    except ValueError:
        print("Помилка в обробці даних. Перевірте формат файлу.")

# Виклик функції
total, average = total_salary("salary_list.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


