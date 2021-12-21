menu = [{'title': 'Запись', 'url_name': 'addappointment'},
        {'title': 'Цены', 'url_name': 'pricelist'},
        {'title': 'Контакты', 'url_name': 'contacts'},
        {'title': 'Регистрация', 'url_name': 'register'},
        {'title': 'Войти', 'url_name': 'login'},
        {'title': 'Выйти', 'url_name': 'logout'}
        ]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()  # для главной страницы это условие реализовано отдельно в функции представления
        if not self.request.user.is_authenticated:
            user_menu.pop(5)
        else:
            user_menu.pop(3)
            user_menu.pop(3)

        context['menu'] = user_menu

        return context