from django.utils import timezone
from dateutil.relativedelta import relativedelta
from core.services import servicos_services, client_services, vehicles_services

today = timezone.now().date()

def month_limits():
    start_current_month = today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    start_next_month = (start_current_month + relativedelta(months=1))
    start_previous_month = (start_current_month - relativedelta(months=1))
    
    return start_current_month, start_next_month, start_previous_month

def get_next_prev_curr_month_relactive(month=0):
    ##-1 é para o mes passado, 0 para o mes atual e 1 para o proimo mes
    day = today.replace(day=1)
    start = day + relativedelta(months=month)
    end = start + relativedelta(months=1)
    start, end = [d.strftime("%Y-%m-%d %H:%M:%S") for d in (start, end)]
    return start, end

def kpis():
    delayed = servicos_services.show_delayed_services()
    delayed_count = len(delayed)

    next_to_due_date = servicos_services.get_next_due_service()
    active = len(servicos_services.get_active_services())

    curr_month = get_next_prev_curr_month_relactive(0)
    prev_month = get_next_prev_curr_month_relactive(-1)
    curr = servicos_services.get_month_service_count(curr_month[0], curr_month[1])
    prev = servicos_services.get_month_service_count(prev_month[0], prev_month[1])
    print(f"Current Month: {curr_month}, Previous Month: {prev_month}")

    return {
        "delayed_count": delayed_count,
        "next_to_due_date": next_to_due_date,
        "active_services": active,
        "current_month_services": curr,
        "previous_month_services": prev,
        "total_clients": client_services.count_clients(),
        "total_vehicles": vehicles_services.count_vehicles(),
    }