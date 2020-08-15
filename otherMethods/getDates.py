from datetime import date, timedelta


def get_current_date():
    today = date.today()
    current_date = today.strftime("%Y-%m-%d")
    return current_date


def get_end_date():
    today = date.today()
    getdate = today + timedelta(weeks=1)
    end_date = getdate.strftime("%Y-%m-%d")
    return end_date
