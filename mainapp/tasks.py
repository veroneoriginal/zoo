import time

def save_report(queryset):
    time.sleep(10)
    with open('food.txt', 'w', encoding='utf-8') as f:
        for food in queryset.all():
            f.write(f'{food.name}\n')
