
from django.shortcuts import render, redirect

def mbo_authed(func):
    def decorated(request, *args, **kwargs):
      userid = 0
      is_logged_in = False
      if 'userid' in request.session:
        userid = request.session['userid']
      if userid != 0 and userid != None:
        is_logged_in = True
      print('USERID FROM DECORATOR: ', userid)
      if is_logged_in:
        return func(request, *args, **kwargs)
      else:
        return redirect('/web/login')
    return decorated


    