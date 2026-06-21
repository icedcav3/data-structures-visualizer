# Data Structures Visualizer - Документация API

## Основные модули

### core/

#### Stack (Стек)
```python
from src.core.stack import Stack

stack = Stack()
stack.push(5)        # Добавить элемент
value = stack.pop()  # Извлечь элемент
top = stack.peek()   # Посмотреть верхний элемент
empty = stack.is_empty()  # Проверить пустоту
size = stack.size()  # Получить размер
```

#### Queue (Очередь)
```python
from src.core.queue import Queue

queue = Queue()
queue.enqueue(5)     # Добавить в конец
value = queue.dequeue()  # Извлечь с начала
front = queue.front()    # Получить первый элемент
empty = queue.is_empty() # Проверить пустоту
size = queue.size()      # Получить размер
```

#### Binary Search Tree (Двоичное дерево поиска)
```python
from src.core.bst import BinarySearchTree

bst = BinarySearchTree()
bst.insert(5)           # Вставить элемент
found = bst.search(5)   # Поиск элемента
bst.delete(5)           # Удалить элемент
inorder = bst.inorder_traversal()  # Обход в порядке
```

### visualization/

#### StackDrawer
```python
from src.visualization.stack_drawer import StackDrawer

drawer = StackDrawer(canvas)
drawer.draw(stack)  # Отрисовать стек
```

#### QueueDrawer
```python
from src.visualization.queue_drawer import QueueDrawer

drawer = QueueDrawer(canvas)
drawer.draw(queue)  # Отрисовать очередь
```

#### BSTDrawer
```python
from src.visualization.bst_drawer import BSTDrawer

drawer = BSTDrawer(canvas)
drawer.draw(bst)  # Отрисовать дерево
```

### controllers/

#### StackController
```python
from src.controllers.stack_controller import StackController

controller = StackController()
result = controller.perform_operation('push', 5)
result = controller.perform_operation('pop')
result = controller.undo()  # Отменить операцию
```

#### QueueController
```python
from src.controllers.queue_controller import QueueController

controller = QueueController()
result = controller.perform_operation('enqueue', 5)
result = controller.perform_operation('dequeue')
result = controller.undo()
```

#### BSTController
```python
from src.controllers.bst_controller import BSTController

controller = BSTController()
result = controller.perform_operation('insert', 5)
result = controller.perform_operation('search', 5)
result = controller.perform_operation('delete', 5)
result = controller.undo()
```

### persistence/

#### OperationLogger
```python
from src.persistence.logger import OperationLogger

logger = OperationLogger()
logger.log_operation('push', 5, 'success')
operations = logger.get_operations()
logger.clear_log()
```

#### Config
```python
from src.persistence.config import Config

config = Config()
value = config.get('animation_speed', 500)
config.set('animation_speed', 1000)
```

## GUI

### VisualizerApp
Главное окно приложения с интеграцией всех компонентов:
```python
from src.gui.app import VisualizerApp

app = VisualizerApp()
app.run()
```

### ControlPanel
Панель управления для выбора структуры и ввода значений.

### CanvasFrame
Область отрисовки визуализации.

### OperationLog
Журнал выполненных операций.

### StatusBar
Строка состояния для сообщений и ошибок.

## Утилиты

```python
from src.utils.helpers import format_time, validate_input, sanitize_value

formatted = format_time(3661)  # "1h 1m 1s"
is_valid, value, error = validate_input('5', 'int')  # True, 5, None
safe = sanitize_value("very long string")  # Обрезать до 50 символов
```
