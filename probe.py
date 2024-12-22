# import sqlite3
#
# # Подключаемся к базе данных
# conn = sqlite3.connect('db.sqlite3')
# print(conn)
# # cursor = conn.cursor()
# # print(cursor)
#
# c = conn.cursor()
#
# c.execute("SELECT name FROM sqlite_master WHERE type='table';")
# tables = c.fetchall()
# print(tables)
# #
# # # Выполняем запрос
# # cursor.execute("SELECT SUM(dislikes) FROM Advertisement")
# #
# # # Получаем результат
# # result = cursor.fetchone()[0]
# #
# # print(f"Сумма: {result}")
#
# # Закрываем соединение
# conn.close()
#
# # from django.db.models import Sum
# # from urban_project.board.models import Advertisement
# # # import os
# # # import sys
# # # import django
# # #
# # # sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# # # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoProject.settings')
# # # django.setup()
# # result = Advertisement.objects.aggregate(total_dislikes=Sum('dislikes'))
# # total_dislikes = result['total_dislikes']
# # print(f"Сумма dislikes: {total_dislikes}")