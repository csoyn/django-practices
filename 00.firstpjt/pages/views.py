from django.shortcuts import render

def index(request):
    # Template Namespace 문제!!
    # 1. index.html 이라는 이름의 탬플릿이 중복
    # 2. 탬플릿을 랜더할 때, templates 폴더를 모두 조사
    #  -> settings.py에 등록되어있는 앱 순서대로 조사

    # 해결방안
    #  -> app 별로 templates 하위 디렉토리를 추가해서
    #  탬플릿을 분리 관리한다!
    return render(request, 'pages/index.html')