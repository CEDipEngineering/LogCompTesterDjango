from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def _convert_to_datetime(datestring: str) -> datetime:
    '''
    Returns a datetime object, information accessible through . operator.

    Example:

    # Print month in datestring
    k = _convert_to_datetime("2022-10-16T10:20:51Z")
    print(k.month)
    >>> 10

    '''
    k = datetime.strptime(datestring, '%Y-%m-%dT%H:%M:%SZ')
    return k

def _compute_semester_id(datestring: str) -> str:
    '''
    Computes a string's semester. Dates before July ( < 31/06/xxxx) will be assigned to first semester.
    Returns a string with the year, period, the semester.
    
    Example:

    # Print semester of certain datestring
    s = _compute_semester_id(2022-10-16T10:20:51Z)
    print(s)
    >>> 2022.2

    '''
    date = _convert_to_datetime(datestring)
    year = str(date.year)
    if date.month > 6:
        return year + ".2"
    return year + ".1"

@csrf_exempt
def upload(request):
    body = json.loads(str(request.body, encoding='utf-8'))
    
    # Debug dump req to file
    with open('./req.json', 'w') as f:
        json.dump(body, f)
    
    # Parse request.
    try:
        if body['ref_type'] == 'tag':
            version_id = body['ref'] # v2.1.0
        else:
            raise KeyError("Push was not tag, branch creations don't trigger testing.")
        repository_id = body['repository']['html_url'] # https://github.com/CEDipEngineering/github-actions-test-client
        user_id = body['repository']['owner']['login'] # CEDipEngineering, github username
        # push_time = _convert_to_datetime(body['repository']['pushed_at']) # Used to infer if delivery is before due date.
        # semester_id = _compute_semester_id(body['repository']['pushed_at']) # 2022.2
        print(
            {
                "version_id" : version_id,
                "repository_id" : repository_id,
                "user_id" : user_id,
                # "push_time" : push_time,
                # "semester_id" : semester_id,
            }
        )
    except KeyError as e:
        print('='*30+"\n\n ERROR \n\n")
        print(e)
        print("="*30 + "\n\n")
    
    return HttpResponse({
        "Status": "Ok"
    })