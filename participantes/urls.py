from django.urls import path
from participantes import views


app_name = 'participantes'

urlpatterns = [
    path("lista/", views.RunnersView.as_view(), name='lista-participantes'),
    path('umparticipante/', views.RunnerView.as_view(), name='um-participante'),
    path('umparticipante/<id_arg>/', views.RunnerView.as_view(), name='consulta-participante'),
]