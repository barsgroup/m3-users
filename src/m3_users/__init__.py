#coding:utf-8
u"""
m3_users
========

Приложение, с помощью которого можно управлять разрешениями пользователя на выполнение определенных
операций

Подключение к проекту

    .. code-block:: py

        # ===========
        # settings.py
        # ===========

        INSTALLED_APPS = (
            ...
            'm3_users',
            ...
        )

        # ===========
        # app_meta.py
        # ===========

        from m3_users.roles import RolesWindowAction
        from m3_ext.ui import app_ui

        admin_group = app_ui.DesktopLaunchGroup(name=u'Администрирование')

        admin_group.subitems.append(
            app_ui.DesktopLauncher(name=u'Роли пользователей',
                                   url=RolesWindowAction.absolute_url())
        )

        app_ui.DesktopLoader.add(app_ui.get_metarole(app_ui.GENERIC_USER),
                                app_ui.DesktopLoader.START_MENU,
                                admin_group)

|pict1|

.. |pict1| image:: _static/m3_users.png
"""

from app_meta import GENERIC_USER, ADMIN, SUPER_ADMIN