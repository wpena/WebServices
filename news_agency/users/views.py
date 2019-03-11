from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from news.models import Author, Story, User
import re
import datetime

@csrf_exempt
def user_login(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username, password)
        user = authenticate(username=username, password=password)
        if (user is not None):
            if (user.is_active):
                login(request, user)
                if (user.is_authenticated):
                    return HttpResponse('Logged in', status=200)
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Username or Password is incorrect', status=401)
    if (request.method != 'POST'):
        return HttpResponse ('invalid request', status=400)


@login_required
@csrf_exempt
def user_logout(request):
    logout(request)
    return HttpResponse('Successfully logged out. Au Revoir!', status=200)


@login_required
@csrf_exempt
def poststory(request):
    if (request.method == 'POST'):
        data = request.GET.dict()
       
        headline = data.get("headline")
        story_cat = data.get("story_cat")
        story_region = data.get("story_region")
        story_details = data.get("story_details")
        current_user_id = request.user.id
        
        author = Author.objects.get(user__id=current_user_id)
        Story.objects.create(
            headline=headline,
            story_cat=story_cat,
            story_region=story_region,
            story_details=story_details,
            author=author.user
            )
        return HttpResponse('Story Created', status=201)
    else:
        return HttpResponse('Unable to respond to request', status=404)

@csrf_exempt
def getstories(request):
    if (request.method == 'GET'):
        data = request.GET.dict()
        
        story_cat = data.get("story_cat")
        story_region = data.get("story_region")
        story_date = data.get("story_date")
        
        # story_date = re.search(r'(\d\d)\.(\d\d)\.(\d{4})', story_date)
        # day, month, year = story_date.groups()
        # new_date = datetime.datetime(int(year), int(month), int(day))
        
        stories = Story.objects.filter(
            story_cat__iexact=story_cat,
            story_region__iexact=story_region,
            #story_date__gte=new_date
        )
            
        stories_dict = []
        for story in stories:
            stories_dict.append({
                "key": story.key,
                "headline": story.headline,
                "category": story.story_cat,
                "region": story.story_region,
                "author": story.author.username,
                "date": story.story_date,
                "details": story.story_details,
                }
                )
            return JsonResponse(stories_dict, safe=False)
        else:
            return HttpResponse(status=404 + 'No stories found')

@login_required
@csrf_exempt
def deletestory(request):
    if (request.method == 'POST'):
        data = request.GET.dict()
        Story.objects.get(pk=data["story_key"]).delete()
        return HttpResponse("Story Deleted", status=201)
    else:
        return HttpResponse('Service Unavailable', status_code=503)
