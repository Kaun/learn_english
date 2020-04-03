import random
from data import teachers
from flask import Flask, render_template, request
# import json
#
# data = [{"name": "Alexey", "phone": "55049"}, {"name": "Alexandr", "phone": "65555"}]
#
# with open("data.json", "r") as f:
#     # json.dump(data,f)
#     # content = f.read()
#     content_json = json.load(f)
#
#
# new_line = input().split(' ')
# new_dict = {"name": new_line[0], "phone": new_line[1]}
# json.dumps(content_json.append(new_dict))
# print(content_json)
#
#
# with open("data_1.json", "w") as f:
#     json.dump(content_json, f)



# import json
#
# new_line = input().split(" ")
#
# with open("data.json", "a") as f:
#     json.dump(new_line, f)

#
# @app.route('/pay', methods =['POST'])
# def pay():
#     t = request.form.get
#     return f"Карта: {t('card_number')}\nВладелец: {t('card_name')}\nДействует до: {t('card_expires')}\nКод безопасности: {t('card_cvv2')}"


# mail = "fffffw,ru"
# print("@" not in mail)
#
# app = Flask(__name__)
#
# @app.route('/signin', methods='POST')
# def registration():
#     form = '''
#     <form class="auth-form" action="/signin" method="POST">
#     <div> Имя <input type="text" name="u_name" />  </div>
#     <div> Фамилия <input type="text" name="u_surname" /> </div>
#     <div> Почта <input type="email" name="u_mail" /> </div>
#     <div> Пароль <input type="password" name="u_pass" /> </div>
#     <div> Еще раз <input type="password" name="u_pass_again" /> </div>
#     <div> <input type="submit" value="Зарегистрироваться" />  </div>
#     </form>
# '''
#     req = request.form.get
#     if req('u_mail').find("@")<0:
#         print(req('u_mail').find("@"))
#         if req('u_pass')!=req('u_pass_again') or req('u_pass')=='' :
#             return form
#     else :
#         return f"Пользователь {req('u_name')} {req('u_surname')} с почтой {req('u_mail')} зарегистрирован"
#
#
# form = '''
#     <form class="auth-form" action="/signin" method="POST">
#     <div> Имя <input type="text" name="u_name" />  </div>
#     <div> Фамилия <input type="text" name="u_surname" /> </div>
#     <div> Почта <input type="text" name="u_mail" /> </div>
#     <div> Пароль <input type="password" name="u_pass" /> </div>
#     <div> Еще раз <input type="password" name="u_pass_again" /> </div>
#     <div> <input type="submit" value="Зарегистрироваться" />  </div>
#     </form>
# '''
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return form
#
# @app.route('/signin', methods=["POST"])
# def search():
#     req = request.form.get
#     if req('u_pass') != req('u_pass_again') or req('u_pass') == '' or not ("@" in req('u_mail')):
#         return form
#     else:
#
#         return f"Пользователь {req('u_name')} {req('u_surname')} с почтой {req('u_mail')} зарегистрирован"
#
#
# if __name__ == '__main__':
#     app.run()
teachers_random = []
for i in range(0, 6):
    teacher = random.choice(teachers)
    teachers_random.append(teacher)
    # print(t["id"])
    # random_profile = random.choice[teachers]
#     teacher_random.append(random_profile)
print(teachers_random)

t = random.sample(teachers, 6)
print(t)