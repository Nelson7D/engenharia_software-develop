from django.urls import include, path

from . import views

management_patterns = (
    [
        path("", views.index, name="index"),
        path("sign-in/", views.sign_in, name="sign_in"),
        path("logout-user/", views.logout_user, name="logout_user"),
        path("cadastro-produto.html", views.cadastro_produto, name='cadastro_produto'),
        path("dashboard.html", views.dashboard, name='dashboard'),
        path("tabela-sem-dados.html", views.tabela_sem_dados, name='tabela_sem_dados'),
        path("pesquisa-produtos.html", views.pesquisa_produtos, name='pesquisa_produtos'),
        path('login.html', views.login_page, name='login'),
        path('cadastro.html', views.cadastro_page, name='cadastro'),
        path('pagina-vazia.html', views.pagina_vazia, name='pagina_vazia'),
        path('esqueceu-a-senha.html', views.esqueceu_a_senha, name='esqueceu_a_senha'),
        path('cadastro-funcionario.html', views.cadastro_funcionario, name='cadastro_funcionario'),
        path('403.html', views.error_403, name='403'),
        path('404.html', views.error_404, name='404'),
        path('500.html', views.error_500, name='500'),


        # path("event-detail/", views.event_detail, name="event_detail"),
        # path("contact-us/<str:pack>/", views.contact_us, name="contact_us"),
        # path("send-email/<str:pack>/", views.send_email, name="send_email"),
        # path("privacity/", views.privacity, name="privacity"),
        # path("terms/", views.terms, name="terms"),
        # path("sent/", views.sent, name="sent"),
    ],
    "management"
)

urlpatterns = [
    path("", include(management_patterns)),
]