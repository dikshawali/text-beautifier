from django.http import HttpResponse
from django.shortcuts import render

def index_fun(request):
    # return HttpResponse("<h1>Choose from the below links!</h1><br><a href='#'></a><br><a href='/newlinerem'>New line Removal</a><br><a href='/spacerem'>Space Removal</a><br><a href='/capfirst'>Capitalize First</a><br><a href='/rempunc'>Remove Punctuation</a><br><a href='/charcount'>Character Count</a>")
    # params={'name':'Diksha Wali'}
    # ta_text=request.GET.get('ta_text_html', 'default')
    # print(ta_text)
    return render(request, 'index.html')

def about_fun(request):
    return HttpResponse('This is information about our website.Enjoy!')

def fileread(request):
    with open('myfirstsite/randomfile.txt') as f:
        lines=f.readlines()
    return HttpResponse(f'{lines[0]}')

def analyzer(request):
    tatext=request.GET.get('tatexthtml')
    rpdj=request.GET.get('rp')
    ucdj=request.GET.get('uc')
    nlrdj=request.GET.get('nlr')
    t1dj=request.GET.get('t1')
    t2dj=request.GET.get('t2')
    lenstrdj=request.GET.get('lenstr')

    if(rpdj == 'on'):
        for x in '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~''':
            tatext=tatext.replace(x, '')

    if(ucdj == 'on'):
        # print('came here!! I swear!!')
        tatext=tatext.upper()

    if(nlrdj=='on'):
        tatext=' '.join(tatext.splitlines())
        print("after newline removal: ", tatext)
    # replacing:
    tatext=tatext.replace(t1dj, t2dj)

    if(lenstrdj=='on'):
        tatext=len(tatext)
        # print(tatext)

    tatext_dict={'text': tatext}
    return render(request, 'analyzer.html', tatext_dict)










    