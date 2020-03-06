from django.http import HttpResponse
from django.shortcuts import render
from nodes.models import Node
from edges.models import Edge

def home(request):
    cluster1 = Edge.objects.filter(cluster = 1)
    cluster2 = Edge.objects.filter(cluster = 2)
    cluster3 = Edge.objects.filter(cluster = 3)
    cluster4 = Edge.objects.filter(cluster = 4)
    cluster5 = Edge.objects.filter(cluster = 5)
    cluster6 = Edge.objects.filter(cluster = 6)
    cluster7 = Edge.objects.filter(cluster = 7)
    cluster8 = Edge.objects.filter(cluster = 8)
    cluster9 = Edge.objects.filter(cluster = 9)
    cluster10 = Edge.objects.filter(cluster = 10)
    

    return render(request, 'home.html', {'cluster1' : cluster1, 'cluster2':cluster2, 'cluster3':cluster3,
                                        'cluster4':cluster4, 'cluster5':cluster5, 'cluster6':cluster6,
                                        'cluster7':cluster7, 'cluster8':cluster8, 'cluster9': cluster9, 'cluster10':cluster10})