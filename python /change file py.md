تبدیل فایل Py به EXE

بعضی اوقات لازم هست که فایل پایتونی‌مون رو تبدیل به یک فایل EXE کنیم تا راحت بتونیم اجراش کنیم. برای این کار ابزارهای زیادی هست، ولی یکی از راحت‌ترین و بی‌دردسرترین روش‌ها استفاده از cx_Freeze هست. حالا بریم ببینیم چطوری میشه ازش استفاده کرد.

خب طبیعی هست که اول باید ابزار رو نصب کنیم. توی ترمینال این دستور رو می‌زنیم:
pip install cx_Freeze
بعد از نصب، باید یه فایل بسازیم به اسم setup.py که قراره تنظیمات تبدیل پروژه رو توش بنویسیم. اگه برنامه‌مون ساده‌ست این کد کفایت می‌کنه:
from cx_Freeze import setup, Executable

setup(
    name="اسم برنامه",
    version="ورژن برنامه",
    description="یک توضیح درباره برنامه",
    executables=[Executable("main.py")]
)
ولی اگه برنامه‌مون از کتابخونه‌های گرافیکی استفاده می‌کنه، اون وقت فایل setup.py باید یک ذره فرق داشته باشه:
from cx_Freeze import setup, Executable
import sys

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="اسم برنامه",
    version="ورژن",
    description="توضیحات",
    executables=[Executable("main.py", base=base)]
)
نکته مهم: فایلی که می‌خواهید تبدیلش کنید باید اسمش main.py باشه. البته می‌تونید اسم دیگه هم بدید، ولی اون موقع باید توی قسمت Executable اسم دقیق فایل رو بنویسید.
حالا ترمینال رو باز کنید، وارد مسیر اون فایل شید و این دستور رو بزنید:
python setup.py build
یه پوشه به اسم build ساخته می‌شه که داخل‌ش نسخه‌ی EXE برنامه‌ هست😉


یک روش ساده‌تر هم هست که دیگه نیاز به فایل setup نداره.
که دستورش این هست:
cxfreeze --script hello.py --target-dir dist
اینجوری مستقیم فایل EXE ساخته می‌شه و نیاز به فایل setup.py نیست.
البته توی صفحه رسمی‌ش سوییچ‌های دیگه هم گذاشته شده که می‌تونید ازشون استفاده کنید:
https://cx-freeze.readthedocs.io/en/stable/script.html


💎 Channel:
https://t.me/programming_languages390
