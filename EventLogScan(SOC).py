import csv

# Путь к исходному файлу журнала событий
input_log_file_path = 'event_log.csv'
# Путь к новому файлу для сохранения отфильтрованных событий
output_log_file_path = 'filtered_event_log.csv'

# ID событий, которые нас интересуют
event_ids_to_check = {4624, 4625, 4634, 4688, 4697, 4720, 4740, 4769, 4776, 5140}

# Список для хранения отфильтрованных событий
filtered_events = []

# Открываем исходный файл журнала и считываем его
with open(input_log_file_path, mode='r', encoding='utf-8') as log_file:
    csv_reader = csv.DictReader(log_file)
    
    # Получаем названия колонок из исходного файла
    fieldnames = csv_reader.fieldnames
    
    # Проходим по каждой строке в файле
    for row in csv_reader:
        # Проверяем, если ID события входит в интересующий нас список
        event_id = int(row['EventID'])
        if event_id in event_ids_to_check:
            # Добавляем событие в список отфильтрованных событий
            filtered_events.append(row)

# Сохраняем отфильтрованные события в новый файл
with open(output_log_file_path, mode='w', encoding='utf-8', newline='') as output_file:
    csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    # Записываем заголовок (названия колонок) в новый файл
    csv_writer.writeheader()
    # Записываем все отфильтрованные события
    csv_writer.writerows(filtered_events)

print(f"Отфильтрованные события сохранены в файл: {output_log_file_path}")
