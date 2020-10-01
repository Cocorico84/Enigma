from django.shortcuts import render


def enigma(request):
    return render(request, 'enigma2.html')
