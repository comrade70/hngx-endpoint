from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

# Create your views here.
def api(request):
    slack_name =request.GET.get("slack_name", "")
    track = request.GET.get("track", "")

    current_day = datetime.now().strftime("%A")
    utc_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    github_file_url = "https://github.com/comrade70/hngx-endpoint/blob/master/manage.py"
    github_repo_url = "https://github.com/comrade70/hngx-endpoint"

    #response to be served
    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return JsonResponse(response)
