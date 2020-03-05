from django.http import HttpResponse
from django.shortcuts import render
from nodes.models import Node
from edges.models import Edge

def home(request):
    clusters = []

    for i in range(0, 10):
        clusters.append(Edge.objects.filter(cluster=i))

    # return HttpResponse(clusters[0][0].from_edge)
    return render(request, 'home.html', {'clusters' : clusters})