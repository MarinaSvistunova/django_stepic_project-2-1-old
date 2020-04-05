from django.contrib import admin
from django.urls import path


from vacancies.views import MainView, VacanciesView, JobsView, JobsCategoryView, CompanyJobView

urlpatterns = [
    path('', MainView.as_view(), name='main_view'),
    path('vacancies/', VacanciesView.as_view(), name='vacancies_view'),
    path('jobs/<int:id>/', JobsView.as_view(), name='jobs_view'),
    path('jobs/cat/<str:category>/', JobsCategoryView.as_view(), name='jobs_category_view'),
    path('companies/<int:id>/', CompanyJobView.as_view(), name='company_job_view'),
    path('admin/', admin.site.urls),
]
