# Webparsing

Этот проект представляет собой парсер товаров с сайта [saucedemo.com](https://www.saucedemo.com), написанный на Python с использованием Selenium. Скрипт выполняет авторизацию, открывает карточки товаров, извлекает названия и сохраняет их в базу данных SQLite.

## Возможности

- Вход на сайт через Selenium
- Переход по товарам и сбор названий
- Сохранение названий в SQLite-базу
- Вывод всех товаров в консоль

## Установка

1. Установите зависимости:
   ```bash
   pip install selenium
   ```

2. Скачайте ChromeDriver с [chromedriver.chromium.org](https://chromedriver.chromium.org/) и убедитесь, что он доступен в `PATH`.

3. (Опционально) Укажите путь к профилю Chrome в `main.py`, если нужно сохранять сессии:
   ```python
   options.add_argument("--user-data-dir=C:/temp/selenium-profile")
   ```

## Запуск

```bash
python main.py
```
