menu = [{'title': 'Запись', 'url_name': 'addappointment'},
          {'title': 'Цены', 'url_name': 'pricelist'},
          {'title': 'Контакты', 'url_name': 'contacts'},
          {'title': 'Войти', 'url_name': 'login'},
          ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context