from django.db import models


class Specialty( models.Model ):
    code = models.CharField( max_length=30 )
    title = models.CharField( max_length=100 )
    picture = models.URLField()


class Company( models.Model ):
    name = models.CharField( max_length=100 )
    location = models.CharField( max_length=100 )
    logo = models.URLField()
    description = models.CharField( max_length=300 )
    employee_count = models.IntegerField()

    class Meta:
        verbose_name = 'компания'
        verbose_name_plural = 'компании'


class Vacancy( models.Model ):
    title = models.CharField( max_length=100, verbose_name='название вакансии' )
    specialty = models.ForeignKey( Specialty, on_delete=models.CASCADE, related_name='speciality_vacancy' )
    company = models.ForeignKey( Company, on_delete=models.CASCADE, related_name='company_vacancy' )
    description = models.CharField( max_length=300, verbose_name='описание вакансии' )
    salary_min = models.IntegerField( verbose_name='зарплата от' )
    salary_max = models.IntegerField( verbose_name='зарплата до' )
    publish_date = models.DateField( verbose_name='дата публикации' )

    # skills вынесены в класс Skills

    class Meta:
        verbose_name = 'вакансия'
        verbose_name_plural = 'вакансии'

    def __str__(self) -> str:
        return f'{self.title} ({self.specialty})'


class Skill( models.Model ):
    vacancy = models.ForeignKey( Vacancy, on_delete=models.CASCADE, related_name='my_skills' )
    skill = models.TextField()

    class Meta:
        verbose_name = 'навык'
        verbose_name_plural = 'навыки'
