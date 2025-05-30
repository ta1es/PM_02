# PM_02

**Производственная практика по ПМ.02 «Осуществление интеграции программных модулей»**

##  Описание проекта

Данный репозиторий содержит материалы по практике, в рамках которой был реализован модуль приёма, валидации и хранения данных для информационной системы «Учёт заказов».

Проект разработан с использованием **FastAPI** и **PostgreSQL**. Основное внимание было уделено построению REST API, созданию и подключению базы данных, а также проверке корректности работы модулей на тестовых данных.

##  Содержимое репозитория

- `ТЗ ПМ02.docx` — техническое задание, оформленное по ГОСТ 34.602-2020, с описанием архитектуры модуля и базовой структурой БД.
- `main.py` — основной файл приложения FastAPI.
- `database.py` — подключение к базе данных PostgreSQL.
- `models.py` — описание таблиц с помощью SQLAlchemy.
- `schemas.py` — структура входных и выходных данных.
- `README.md` — краткое описание проекта.

##  Описание модуля

Была создана база данных `PM_02`, содержащая таблицы:
- `clients` — данные клиентов;
- `products` — каталог товаров;
- `orders` — информация о заказах.

Модуль поддерживает приём, проверку и запись информации в базу данных, а также обработку пользовательских запросов через API-интерфейс.

##  Функциональность

- Разработка структуры таблиц в PostgreSQL.
- Реализация REST API с методами получения, добавления и обновления данных.
- Интеграция компонентов с использованием FastAPI.
- Проверка корректности операций через Postman.
- Настройка стиля кода с помощью линтера `flake8`.

##  Ссылки

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [ГОСТ 34.602-2020 (ТЗ)](https://www.swrit.ru/doc/gost34/34.602-2020.pdf)

---

 *Автор репозитория: [ta1es](https://github.com/ta1es)*  
 *Дата последнего обновления: 15 апреля 2025*
