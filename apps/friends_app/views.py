from django.shortcuts import render, redirect
from ..login_app.models import User
from models import Friend
def index(request):
        # print request.session['user_id']
    if "email" not in request.session.keys():
        return redirect('/')
    else:
        friends = []
        friendids = [request.session['user_id']]
        for count in range(0, len(User.objects.get(id = request.session['user_id']).friends.all())):
            friends.append(User.objects.get(id = Friend.objects.filter(user = request.session['user_id'])[count].id))
        print friends
        for count in range(0, len(User.objects.get(id = request.session['user_id']).friends.all())):
            friendids.append(Friend.objects.filter(user = request.session['user_id'])[count].id)
        print friendids
        notfriends = []
        stillnot = {}
        for person in User.objects.all():
            for ids in friendids:
                if person.id == ids:
                    stillnot[person.id]= False
                    print stillnot
        for person in User.objects.all():
            if stillnot.has_key(person.id):
                pass
            else:
                notfriends.append(person) #WHY THE FUCK DOESN'T THIS WORK
        # print notfriends
        context = {
            'friendids': friends,
            'otherUsers': notfriends,
        }
        return render(request, 'friends_app/index.html', context) #end

def show(request, userid):
    if "email" not in request.session.keys():
        return redirect('/')
    else:
        context = {
            'user': User.objects.get(id=userid)
        }
        return render(request, 'friends_app/show.html', context)

def add(request, userid):
    if "email" not in request.session.keys():
        return redirect('/')
    else:
        c = Friend(id = userid)
        c.save()
        c.user.add(User.objects.get(id = request.session['user_id']))
        return redirect('/friends')

def remove(request, userid):
        if "email" not in request.session.keys():
            return redirect('/')
        else:
            for user in Friend.objects.filter(user = request.session['user_id']):
                a = User.objects.get(id = userid)
                a.remove(user)
            return redirect ('/friends')
