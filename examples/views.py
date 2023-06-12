from django.shortcuts import render
from django.http import HttpResponse

# request = HttpRequest()
# response = HttpResponse()

#Функциональный обработчик(view),принимает request, отдает response
# def index(request):
#     return HttpResponse("Hello")

# def index(request):
#     my_list = [1,2,3,4]
#     return HttpResponse(my_list)

# def index(request):
#     text = "<h1>Hello<h1>"
#     return HttpResponse(text)

# def index(request):
#     body = f"""<body>
#     <img src = https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.newsweek.com%2Fhow-take-picture-supermoon-smartphone-moon-iphone-520810&psig=AOvVaw2FEniKQfeKrEr0OIXEJya2&ust=1686322299872000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCMDExJ_2s_8CFQAAAAAdAAAAABAE
#     <body>"""
#     return HttpResponse(body)

# def index(request):
#     if request.method == "GET":
#         print(request.get_host())
#     return HttpResponse("Hello",status=500)
