from django.http import HttpResponse
from django.shortcuts import render
from nodes.models import Node

def home(request):
    for i in range(1, 4040):
        node = Node()
        node.node_id = i
        node.save()

    return render(request, 'home.html')