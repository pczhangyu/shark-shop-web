from django.core.serializers import json


def application(environ, start_response):
    classmates = ['mate1', 'mate2', 'mate3']
    print len(classmates)
    classmates.append('mate4')
    classmates.insert(0, 'mate0')
    start_response('200 OK', [('Content-Type', 'application/json')])
    return classmates