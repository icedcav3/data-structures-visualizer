# Data Structures Visualizer

## Описание

Интерактивное приложение для визуализации базовых структур данных:
- **Стек (Stack)** — операции push, pop, peek
- **Очередь (Queue)** — операции enqueue, dequeue
- **Двоичное дерево поиска (BST)** — операции insert, delete, search

Приложение позволяет пошагово выполнять операции с визуализацией состояния структуры после каждой операции, ведёт лог операций с возможностью отмены.

## Требования

- Python 3.8+
- tkinter (обычно установлен с Python)
- pytest (для тестирования)

## Установка

```bash
clone https://github.com/icedcav3/data-structures-visualizer.git
cd data-structures-visualizer
pip install -r requirements.txt
```

## Запуск

### Локальный запуск
```bash
python src/main.py
```

### Через Docker
```bash
docker-compose up
```

### Запуск тестов
```bash
pytest
python scripts/run_tests.py
```

## Структура проекта

```
src/
├── core/              # Реализация структур данных
├── visualization/     # Визуализация на Canvas
├── gui/              # Графический интерфейс
├── controllers/      # Контроллеры (логика)
├── persistence/      # Логирование и конфигурация
└── utils/           # Утилиты
```

## Использование

1. Выберите структуру данных из выпадающего меню
2. Введите значение в текстовое поле
3. Нажмите кнопку операции (Push/Pop, Enqueue/Dequeue, Insert/Delete/Search)
4. Смотрите визуализацию и лог операций
5. Используйте кнопку Undo для отмены последней операции

## Лицензия

MIT License - см. файл LICENSE
