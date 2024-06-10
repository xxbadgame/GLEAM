from django.contrib import admin
from django.urls import path
from marketplace.views import *
from accounts.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    
    # Accounts
    path('admin/', admin.site.urls),
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    
    # Marketplace
    path('mission_detail/<str:slug>/', mission_detail, name='mission_detail'),
    path('missions_company/', missions_company , name='missions_company'),
    path('missions_freelance/', missions_freelance , name='missions_freelance'),
    path('missions/', missions, name='missions'),
    path('creation_mission/', creation_mission, name='creation_mission'),
    path('BotCreationProjet/', BotCreationProjet, name='BotCreationProjet'),
    path('save_cdc_and_tasks/', save_cdc_and_tasks, name='save_cdc_and_tasks'),
    path('mission_detail/<str:slug>/apply', apply, name='apply'),
    path('mission_detail/<str:slug>/delete_apply', delete_apply, name='delete_apply'),
    path('waitlist/', waitlist, name='waitlist'),
    path('waitlist/delete_waitlist', delete_waitlist, name='delete_waitlist')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
