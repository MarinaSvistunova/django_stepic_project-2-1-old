def variable_to_context(request):
    return {
        'menu_titles': {
            'Главная': '',
            'Вакансии': 'vacancies/',
            'О проекте': ''
        },
        'searches': ['Python', 'Flask', 'Django', 'Парсинг', 'ML']
    }
