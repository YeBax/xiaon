import datetime
from language.frame import Frame

__author__ = "Yebax"

if __name__ == '__main__':
    # import setting
    user_id = 123
    t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    f = Frame(user_id, t)

    while True:
        s = input("请输入内容：")
        r = f.receive_talk(s, t)

        print(r)


