# Инструкция по развертыванию

## Локальная установка

### Требования
- Python 3.8 или выше
- pip (обычно идет с Python)

### Установка

1. **Клонировать репозиторий**
```bash
git clone https://github.com/icedcav3/data-structures-visualizer.git
cd data-structures-visualizer
```

2. **Установить зависимости**
```bash
pip install -r requirements.txt
```

3. **Запустить приложение**
```bash
python src/main.py
```

Основное окно приложения откроется автоматически.

## Docker

### Требования
- Docker
- Docker Compose

### Установка

1. **Убедитесь, что Docker запущен**

2. **Запустите контейнер**
```bash
docker-compose up
```

Примечание: Для отображения GUI в контейнере может потребоваться дополнительная конфигурация X11 на Linux/Mac.

## Запуск тестов

```bash
# Быстрый запуск тестов
pytest

# Запуск с отчетом о покрытии
pytest --cov=src --cov-report=html

# Использование скрипта
python scripts/run_tests.py
```

## Скрипты запуска

### Linux/Mac
```bash
bash scripts/run.sh
```

### Windows
```cmd
scripts\run.bat
```

## Структура проекта

```
src/
├── core/              # Реализация структур данных
├── visualization/     # Модули отрисовки
├── gui/              # Графический интерфейс
├── controllers/      # Контроллеры логики
├── persistence/      # Логирование и конфигурация
└── utils/            # Утилиты

tests/
├── unit/             # Модульные тесты
├── integration/      # Интеграционные тесты
└── fixtures/         # Тестовые данные

scripts/
├── run.sh/run.bat    # Скрипты запуска
└── run_tests.py      # Скрипт для тестов
```

## Файлы конфигурации

- `requirements.txt` - зависимости Python
- `pytest.ini` - конфигурация pytest
- `Dockerfile` - для Docker
- `docker-compose.yml` - для Docker Compose
- `.gitignore` - исключаемые файлы
- `.dockerignore` - исключаемые файлы для Docker

## Возможные проблемы

### "No module named 'tkinter'"

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install python3-tk
```

**macOS:**
```bash
brew install python-tk
```

**Windows:**
Обычно встроен в Python. Переустановите Python и убедитесь, что выбрана опция "tcl/tk and IDLE".

### Проблемы с отображением GUI

Убедитесь, что у вас есть графический сервер (X11 на Linux, нативный GUI на Windows/macOS).

## Дополнительно

Для получения дополнительной информации см. [README.md](../../README.md) и [API документацию](API.md).
