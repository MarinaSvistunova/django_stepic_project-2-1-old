""" Вакансии """

jobs = [

    {"title": "Разработчик на Python", "cat": "backend", "company": "staffingsmarter", "salary_from": "100000",
     "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Разработчик в проект на Django", "cat": "backend", "company": "swiftattack", "salary_from": "80000",
     "salary_to": "90000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Разработчик на Swift в аутсорс компанию", "cat": "backend", "company": "swiftattack",
     "salary_from": "120000", "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Мидл программист на Python", "cat": "backend", "company": "workiro", "salary_from": "80000",
     "salary_to": "90000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Питонист в стартап", "cat": "backend", "company": "primalassault", "salary_from": "120000",
     "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"}

]

# Company.objects.create( name=company['title'], location="Anythere", logo='https://place-hold.it/130x80', description="Something about company", employee_count=random.randint(1, 1000) )

# Specialty.objects.create(code=category['code'], title=category['title'], picture='https://place-hold.it/100x60' )

# for job in jobs:
#   specialty_id = Specialty.objects.filter(code=job['cat']).first().id
#   company_id = Company.objects.filter(name=job['company']).first().id
# Vacancy.objects.create( title=job['title'], specialty=specialty_id, company=company_id, description=job['desc'], salary_min=job['salary_from'], salary_max=job['salary_to'], publish_date=job['posted'] )
""" Компании """

companies = [

    {"title": "workiro"},
    {"title": "rebelrage"},
    {"title": "staffingsmarter"},
    {"title": "evilthreat h"},
    {"title": "wirey "},
    {"title": "swiftattack"},
    {"title": "troller"},
    {"title": "primalassault"}

]

""" Категории """

categories = [

    {"code": "frontend", "title": "Фронтенд"},
    {"code": "backend", "title": "Бэкенд"},
    {"code": "gamedev", "title": "Геймдев"},
    {"code": "devops", "title": "Девопс"},
    {"code": "design", "title": "Дизайн"},
    {"code": "products", "title": "Продукты"},
    {"code": "management", "title": "Менеджмент"},
    {"code": "testing", "title": "Тестирование"},
    {"code": "ios", "title": "Разработка под iOS"},
    {"code": "android", "title": "Разработка под Android"}

]
