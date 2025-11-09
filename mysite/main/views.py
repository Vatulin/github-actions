from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
import os

def home(request):
    return render(request, 'main/home.html')

def health_check(request):
    """Простой health-check"""
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return JsonResponse({"status": "ok", "database": "connected"})
    except:
        return JsonResponse({"status": "error", "database": "disconnected"}, status=500)

def volume_info(request):
    """Информация о томах"""
    info = {
        "bind_volumes": {
            "app_code": {
                "host_path": "./app_code",
                "container_path": "/app",
                "files_count": len(os.listdir('/app')) if os.path.exists('/app') else 0
            }
        },
        "named_volumes": {
            "static_volume": {
                "path": "/app/static",
                "exists": os.path.exists('/app/static')
            },
            "media_volume": {
                "path": "/app/media", 
                "exists": os.path.exists('/app/media')
            },
            "postgres_data": {
                "description": "PostgreSQL data storage"
            }
        }
    }
    return JsonResponse(info)