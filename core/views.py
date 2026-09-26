import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from core.services.recommender import get_recommendations


@csrf_exempt
def recommend(request):
    if request.method != "POST":
        return JsonResponse(
            {"error": "Only POST requests are allowed."},
            status=405
        )

    try:
        data = json.loads(request.body)
        marks = data.get("marks", {})

        result = get_recommendations(marks)

        return JsonResponse(result)

    except json.JSONDecodeError:
        return JsonResponse(
            {"error": "Invalid JSON."},
            status=400
        )

    except Exception as e:
        return JsonResponse(
            {"error": str(e)},
            status=500
        )