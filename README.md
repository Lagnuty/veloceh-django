# Велоцех

Учебный сайт веломастерской. Контактные данные и цены приведены для примера.

## Запуск на Ubuntu

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py runserver
```

Откройте http://127.0.0.1:8000/. Все страницы зарегистрированы в `workshop/urls.py`. Шаблоны наследуют `base.html` и используют именованные ссылки через тег `url`.

