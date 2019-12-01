import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def error_func(status, message):
    response = JsonResponse({'error': message})
    response.status_code = status
    return response


def check_func(a, b):
    try:
        int(a)
        int(b)
        return True
    except ValueError:
        return False


@csrf_exempt
def add_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            request_data = json.loads(request.body)
            A = request_data.get('A')
            B = request_data.get('B')

            if check_func(A, B):
                result = int(A) + int(B)
            else:
                return error_func(400, 'Value Error')

            data = {
                'answer': result
            }
            return JsonResponse(data)

        else:
            return error_func(400, 'No data provided!')
    else:
        return error_func(405, 'Method not allowed')


@csrf_exempt
def subtract_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            request_data = json.loads(request.body)
            A = request_data.get('A')
            B = request_data.get('B')

            if check_func(A, B):
                result = int(A) - int(B)
            else:
                return error_func(400, 'Value Error')

            data = {
                'answer': result
            }
            return JsonResponse(data)

        else:
            return error_func(400, 'No data provided!')
    else:
        return error_func(405, 'Method not allowed')


@csrf_exempt
def multiply_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            request_data = json.loads(request.body)
            A = request_data.get('A')
            B = request_data.get('B')

            if check_func(A, B):
                result = int(A) * int(B)
            else:
                return error_func(400, 'Value Error')

            data = {
                'answer': result
            }
            return JsonResponse(data)

        else:
            return error_func(400, 'No data provided!')
    else:
        return error_func(405, 'Method not allowed')


@csrf_exempt
def divide_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            request_data = json.loads(request.body)
            A = request_data.get('A')
            B = request_data.get('B')

            if B == 0:
                return error_func(400, 'Division by zero!')

            if check_func(A, B):
                result = int(A) / int(B)
            else:
                return error_func(400, 'Value Error')

            data = {
                'answer': result
            }
            return JsonResponse(data)

        else:
            return error_func(400, 'No data provided!')
    else:
        return error_func(405, 'Method not allowed')
