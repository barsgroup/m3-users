.. :changelog:


2.2.0
+++++
- Функция ``patterns`` из ``django.conf.urls.defaults`` заменена на
  одноименную из ``django.conf.urls``.
- Декоратор ``django.transaction.commit_on_success`` заменен на
  ``m3_django_compat.atomic``.
- Добавил поддержку кастомных моделей пользователя.