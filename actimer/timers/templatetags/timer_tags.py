from django import template

register = template.Library()


@register.inclusion_tag('timers/inc/buttons.html')
def addButtonsHtml(timer_status):
    '''Creates a template for timer control buttons depending on its state.'''

    return {'timer_stats': timer_status}