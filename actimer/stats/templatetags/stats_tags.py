from django import template

register = template.Library()


@register.filter(name='month_title')
def getMonthTitle(month_num: int) -> str:
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return months[month_num]