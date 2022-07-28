# api final
### Функционал

* Подписка на пользователей
* Просмотр, создание, удаление и модификация постов
* Просмотр и создание групп
* Просмотр, создание, удаление и модификация комментариев
* Фильтрация по полям

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Savin-AS94/api_final_yatube.git
```

```
cd kittygram_plus
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
