from configparser import SectionProxy
import pyautogui as p
import time
from datetime import datetime
from random import randint


day = 20
start_hour = '00'
start_min = '02'
end_hour = '08'
end_min = '00'

messages = [
    'hey u HBD :)',
    'happy birthday day to you.',
    'tavalodet andaze eshge man be to mobarak bashe',
    'tavalodet mobarak',
    'HBD to you',
    'zadrozed ro behet tabric migam',
    'tavalod tavalod tvalodet moooooobarak',
    'happy birthday my programer',
    'barname nevise man tavalodet ro tabrik migam',
    'refigh tavalodet mobarak',
    'hhhhhhhhhhhhhhhhhhhhhhaaaaaaaaaaaaaaaapppppppppppppy birthday to us :)',
    ':)',
    ':D',
]
key = 'enter'
delay_between_messages = 1

script_start_time = datetime.now()
time.sleep(5)
while 1:
    now = datetime.now()
    start_time = now.replace(
        hour=int(start_hour),
        minute=int(start_min),
        second=0,
        microsecond=0
    )
    end_time = now.replace(
        hour=int(end_hour),
        minute=int(end_min),
        second=0,
        microsecond=0
    )

    secLater = int((start_time - datetime.now()).total_seconds())
    if((secLater > 0)):
        print('it will start in ', secLater, 'second later')
        continue
    today = now.strftime("%d")
    if(int(day) == int(today) and now > start_time and now < end_time):
        p.typewrite(messages[randint(0, len(messages) - 1)])
        p.press(key)
        print('i\'m doing my work.')
        # time.sleep(delay_between_messages)

    if(today != day and now > end_time):
        print('Done.')
        time.sleep(1)
        print('Doone.')
        time.sleep(1)
        print('Dooone.')
        time.sleep(1)
        print('Doooone.')
        time.sleep(1)
        print('i didn\'t have any things to do.')
        time.sleep(2)
        print('i think i have to kill my self. yeah it\'s better.')
        time.sleep(2)
        print('don\'t forget live in moment and make love.')
        time.sleep(2)
        print('bye.')
        time.sleep(2)
        print('BBBBBBBBBooooooooom ...')
        time.sleep(4)
        print('Aaaaaaaa i think i forget to say a tip. wait.')
        time.sleep(2)
        print('make love with your computer not with girl :)')
        time.sleep(2)
        print('Bye.')
        time.sleep(2)
        exit()


# now = datetime.now()
# current_time = now.strftime("%d - %H")
# print("Current Time =", current_time)
# print(now.replace(hour=8, minute=0, second=0, microsecond=0) > now)

# # time.sleep(5)
# # for i in range(10):
# #     p.typewrite('salam khobi ?')
# #     p.press('enter')
