markdown
# User Repository Project

## Установка и запуск

1. Установите PostgreSQL и создайте базу данных с именем `user_repo`

2. Клонируйте проект и перейдите в папку:
```
git clone <url-репозитория>
cd UserRepo
```

3. Создайте и активируйте виртуальное окружение:
```
python -m venv venv
venv\Scripts\activate
```

4. Установите зависимости:
```
pip install -r requirements.txt
```

5. Настройте подключение к БД в файле database.py:
```
DATABASE_URL = "postgresql://ваш_логин:ваш_пароль@localhost:5432/user_repo"
```

6. Запустите тесты:
```
python -m unittest tests/test_user_repository.py
```

7. Описание проекта
```
models/ - модели данных SQLAlchemy

repositories/ - классы для работы с базой данных

tests/ - интеграционные тесты

database.py - настройка подключения к PostgreSQL
```
`Проект реализует CRUD-операции для модели пользователя с интеграционными тестами.`