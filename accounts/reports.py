from django.db.models import Count, Sum
from django.utils import timezone
from datetime import timedelta
import csv
from django.http import HttpResponse
from .models import Member


def generate_monthly_report(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="monthly_report.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Month', 'New Members', 'Expired Members', 'Active Members'])
    
    # آمار ماهانه
    current_date = timezone.now()
    for i in range(12):
        month_start = current_date - timedelta(days=30*i)
        month_end = month_start - timedelta(days=30)
        
        new_members = Member.objects.filter(
            start_date__range=[month_end, month_start]
        ).count()
        
        expired_members = Member.objects.filter(
            end_date__range=[month_end, month_start]
        ).count()
        
        active_members = Member.objects.filter(
            start_date__lte=month_start,
            end_date__gte=month_start
        ).count()
        
        writer.writerow([
            month_start.strftime("%Y-%m"),
            new_members,
            expired_members,
            active_members
        ])
    
    return response
