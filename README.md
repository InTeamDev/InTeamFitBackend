## Предварительные требования

Требования:
- Python 3.x
- Pip
- База данных PostgreSQL (или другая база данных по вашему выбору)

## Установка

Следуйте этим шагам, чтобы настроить проект на вашем локальном компьютере:

### Клонирование репозитория

```bash
git clone https://github.com/ZetoOfficial/star
cd your-repository
```

### Настройка виртуального окружения

```bash
python -m venv venv
source venv/bin/activate  # На Windows используйте `venv\Scripts\activate`
```

### Установка зависимостей

```bash
pip install -r requirements.txt
```

### Переменные окружения

Настройте необходимые переменные окружения в файле `settings.yaml`

### Запуск базы данных через Docker Compose

Если вы предпочитаете использовать Docker для запуска базы данных, убедитесь, что у вас установлен Docker и Docker Compose. Затем выполните следующую команду:

```bash
make up  # docker-compose -f docker-compose.yml up --build -d
```

## Настройка базы данных

Прежде чем начать работу с приложением, необходимо накатить миграции с помощью Alembic. Выполните следующие команды:

```bash
alembic upgrade head
```

Эти команды применят миграции к вашей базе данных, создавая необходимые таблицы и структуры.

## Запуск приложения

Запустите приложение локально с помощью следующей команды:

```bash
uvicorn app.service:app --host=localhost --port=8000
```

Приложение будет доступно по адресу `http://localhost:8000`.

## Тестирование [скоро]

Запустите набор тестов с помощью pytest:

```bash
pytest
```

## Документация API

После запуска приложения вы можете просмотреть документацию API и протестировать конечные точки по адресу `http://localhost:8000/docs`.
