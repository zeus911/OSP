from django.shortcuts import render, HttpResponseRedirect
# import ldap


def check_user(func):
    def check(request):
        if not request.session.get('username'):
            return HttpResponseRedirect('/login/')
        return func(request)

    return check


def index(request):
    return render(request, "index.html")


def login(request):
    if request.session.get('username'):
        return HttpResponseRedirect('/')

    if request.POST:
        a = ldap.open('10.10.11.210')
        user = request.POST.get('user')
        password = request.POST.get('password')
        username = 'SZ1CARD1\\' + user

        try:
            a.simple_bind_s(username, password)
            status = 0
            request.session['username'] = user
            request.session.set_expiry(0)
            return HttpResponseRedirect('/')
        except:
            status = 1
            return render(request, 'login.html', {'status': status})

    return render(request, 'login.html')


def logout(request):
    if not request.session.get('username'):
        return HttpResponseRedirect('/login/')

    del request.session['username']
    return HttpResponseRedirect('/login/')
