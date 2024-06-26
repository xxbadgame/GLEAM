from django.shortcuts import render, get_object_or_404
from marketplace.models import Mission, Waitlist, ApplyMission
from accounts.models import CustomUser
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from openai import OpenAI
from django.http import JsonResponse
from .AssistantAI.Assistant import *
import os
import uuid


def index(request):
    return render(request, 'marketplace/index.html')

def missions(request):
    missions = Mission.objects.all()
    return render(request, 'marketplace/missions.html', {'missions' : missions})

def missions_company(request):
    return render(request, 'marketplace/missionsCompany.html')

def missions_freelance(request):
    return  render(request, 'marketplace/missionsFreelance.html')

def mission_detail(request, slug):
    mission_detail = get_object_or_404(Mission, slug=slug)
    return render(request, 'marketplace/missionDetail.html', {'mission_detail' : mission_detail})

def creation_mission(request):
    thread = create_thread()
    request.session['thread_id'] = thread.id
    return render(request, 'marketplace/creationMission.html')

def waitlist(request):
    user = request.user
    waitlist, _ = Waitlist.objects.get_or_create(user=user)
    return render(request, 'marketplace/waitlist.html', {'applies': waitlist.applies.all()})

def delete_waitlist(request):
    if waitlist := request.user.waitlist:
        waitlist.delete()
    return redirect('waitlist')

def apply(request, slug):
    user = request.user
    mission = get_object_or_404(Mission, slug=slug)
    waitlist = get_object_or_404(Waitlist,user=user)
    apply_mission , _ = ApplyMission.objects.get_or_create(user=user,mission=mission)
    
    waitlist.applies.add(apply_mission)
    waitlist.save()
    
    return redirect(reverse("mission_detail", kwargs={"slug": slug}))


def delete_apply(request, slug):
    user = request.user
    waitlist = get_object_or_404(Waitlist, user=user)
    mission = get_object_or_404(Mission, slug=slug)
    apply_mission = get_object_or_404(ApplyMission, user=user, mission=mission)
    waitlist.applies.remove(apply_mission)
    apply_mission.delete()
    
    return redirect('waitlist')

    
# Création d'un assistant 
# Prompting / Knowledge / Action
    
def BotCreationProjet(request):
    
    thread_id = request.session.get('thread_id', None)
    ASSISTANT_ID = os.environ.get('OPENAI_ASS_CDC_KEY')
    
    if request.method == "POST":
        message = request.POST.get('message')
        
        assistant = retrieve_assistant(ASSISTANT_ID)
        Add_message(message=message, thread_id=thread_id)
        
        responseHTML = run_assistant(assistant=assistant, thread_id=thread_id)
        print(responseHTML)
        return HttpResponse(responseHTML)
    
    return render(request, 'marketplace/creationMission.html')


def creation_tasks(request):
    thread_id = request.session.get('thread_id', None)
    ASSISTANT_ID = os.environ.get('OPENAI_ASS_TASKS_KEY')
    
    

def save_cdc_and_tasks(request):
    if request.method == "POST":
        titre = request.POST.get('titre')
        unique_id = str(uuid.uuid4())[:8]
        slug = f"{titre.lower()}-{unique_id}"
        description = request.POST.get('description')
        company_name = request.POST.get('company_id')
        company_user = get_object_or_404(CustomUser, username=company_name)
        budget = request.POST.get('budget')
        deadline = request.POST.get('deadline')
        thread_id = request.session.get('thread_id', None)
        mission = Mission(title=titre,
                          slug=slug,
                          description=description,
                          company_id=company_user, 
                          budget=budget,
                          deadline=deadline,
                          thread_id=thread_id
                          )
        mission.save()
        

    return HttpResponse("Mission Envoyé")