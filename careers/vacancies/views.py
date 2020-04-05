from django.shortcuts import render
from django.views import View

from .models import Vacancy, Specialty, Company, Skill


class MainView( View ):
    def get(self, request):
        context = {}

        specialties = Specialty.objects.all()

        context['specialties'] = {}

        for specialty in specialties:
            jobs_count = Vacancy.objects.filter( specialty=Specialty.objects.get( code=specialty.code ).id ).count()
            context['specialties'][specialty.code] = {'title': specialty.title, 'img': specialty.picture,
                                                      'count': jobs_count}

        # companies name logo vacancies

        companies = Company.objects.all()

        context['companies'] = {}

        for company in companies:
            jobs_count = Vacancy.objects.filter( company=company.id ).count()
            context['companies'][company.id] = {'name': company.name, 'img': company.logo, 'count': jobs_count}

        return render(
            request, 'vacancies/index.html', context
        )


# class Skill( models.Model ):
#     vacancy = models.ForeignKey( Vacancy, on_delete=models.CASCADE, related_name='my_skills' )
#     skill = models.TextField()
#

# class Vacancy( models.Model ):
#     title = models.CharField( max_length=100, verbose_name='название вакансии' )
#     specialty = models.ForeignKey( Specialty, on_delete=models.CASCADE, related_name='speciality_vacancy' )
#     company = models.ForeignKey( Company, on_delete=models.CASCADE, related_name='company_vacancy' )
#     description = models.CharField( max_length=300, verbose_name='описание вакансии' )
#     salary_min = models.IntegerField( verbose_name='зарплата от' )
#     salary_max = models.IntegerField( verbose_name='зарплата до' )
#     publish_date = models.DateField( verbose_name='дата публикации' )

class VacanciesView( View ):
    def get(self, request):
        context = {}

        vacancies = Vacancy.objects.all()

        context['count'] = vacancies.count()

        context['vacancies'] = {}
        for vacancy in vacancies:
            skills = []
            for each_skill in Skill.objects.filter( vacancy=vacancy.id ):
                skills += [each_skill.skill]
            context['vacancies'][vacancy.id] = {'title': vacancy.title,
                                                'specialty': vacancy.specialty.title,
                                                'logo': vacancy.company.logo,
                                                'skills': skills,
                                                'salary_min': vacancy.salary_min,
                                                'salary_max': vacancy.salary_max,
                                                'date': vacancy.publish_date}

        return render(
            request, 'vacancies/vacancies_list.html', context
        )


class JobsView( View ):
    def get(self, request, id):
        context = {}

        vacancy = Vacancy.objects.filter( id=id ).first()
        # company = Company.objects.filter( id=vacancy.company ).first()

        context['vacancy'] = vacancy

        skills = []
        for each_skill in Skill.objects.filter( vacancy=id ):
            skills += [each_skill.skill]

        context['skills'] = skills

        return render(
            request, 'vacancies/vacancy.html', context
        )


class JobsCategoryView( View ):
    def get(self, request, category):
        context = {}

        specialty = Specialty.objects.get( code=category )
        vacancies = Vacancy.objects.filter( specialty=specialty.id )
        context['title'] = specialty.title
        context['count'] = vacancies.count()

        context['vacancies'] = {}
        for vacancy in vacancies:
            skills = []
            for each_skill in Skill.objects.filter( vacancy=vacancy.id ):
                skills += [each_skill.skill]
            context['vacancies'][vacancy.id] = {'title': vacancy.title,
                                                'specialty': vacancy.specialty.title,
                                                'logo': vacancy.company.logo,
                                                'skills': skills,
                                                'salary_min': vacancy.salary_min,
                                                'salary_max': vacancy.salary_max,
                                                'date': vacancy.publish_date}

        return render(
            request, 'vacancies/list.html', context
        )


class CompanyJobView( View ):
    def get(self, request, id):
        context = {}

        company = Company.objects.filter( id=id ).first()

        context['company'] = company
        vacancies = Vacancy.objects.filter( company=id )
        context['count'] = vacancies.count()
        context['vacancies'] = {}
        for vacancy in vacancies:
            skills = []
            for each_skill in Skill.objects.filter( vacancy=vacancy.id ):
                skills += [each_skill.skill]
            context['vacancies'][vacancy.id] = {'title': vacancy.title,
                                                'specialty': vacancy.specialty.title,
                                                'logo': vacancy.company.logo,
                                                'skills': skills,
                                                'salary_min': vacancy.salary_min,
                                                'salary_max': vacancy.salary_max,
                                                'date': vacancy.publish_date}

        return render(
            request, 'vacancies/company.html', context
        )
