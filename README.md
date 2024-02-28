# rishat_test_task

**Все зависимости находятся в requirements.txt, пример необходимых переменных окружений в .env_sample**
**Для запуска проекта:**
- `git clone https://github.com/AliaksandrSihai/rishat_test_task.git`
-  Создать файл .env(скопировать из .env_sample необходимые переменные)
- Зарегистрироваться на https://stripe.com/ и добавить полученный api_secret key в .env(STRIPE_SECRET_KEY)
- Для последующей успешной обработки платежей с помощью webhook перейти на  https://stripe.com/docs/stripe-cli#install и установить stripe-cli для вашей ОС, после успешной установки сохранить полученный webhook signing secret в .env file(STRIPE_WEBHOOK_KEY= ваш webhook signing secret)

  - <br>**Разворачивание без Docker:**
    - `python -m venv venv && source venv/bin/activate && pip install -r requirements.txt`
    - Выполнить в отдельном терминале `stripe listen --forward-to http://127.0.0.1:8000/stripe_webhooks` или же ваш url + port
    - `python manage.py migrate `
    - для создания супер пользователя перейти в users/management/commands/csu.py и изменить необходимые данные(email, password) и выполнить `python manage.py csu`
    - ` python manage.py runserver`
  
    <br>**Разворачивание с помощью Doker:**
    - Для создания супер пользователя перейти в users/management/commands/csu.py и изменить необходимые данные(email, password) и выполнить `docker-compose exec rishat_test_task python manage.py csu`
    - Выполнить в отдельном терминале `docker-compose exec rishat_test_task` и находясь внутри контейнера выполнить  `stripe listen --forward-to http://0.0.0.0:8000/stripe_webhooks` или же ваш url + port

- Перейти в админ-панель(email/password ваши данные в файле users/management/commands/csu.py ) и создать необходимые товары   

## Стек:
- **Django**
- **Django REST framework**
- **PostgreSQL**
- **Stripe**
- **Docker**
## Документация:
- **Drf-yasg**

## О проекте:
  Реализован онлайн магазин товаров. Анонимные пользователи не могут совершать покупок, но могут просматривать товары. Оплата производится с помощью Stripe.






