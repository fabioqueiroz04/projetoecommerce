from django.shortcuts import render

def paginaProjeto(request):

    contexto = {
        "nome": "Projeto de e-commerce"
    }

    return render(request, "homeprojetos.html", contexto)


def primeirapaginaluchesy(request):
    return render(request, "luchesy.html")
