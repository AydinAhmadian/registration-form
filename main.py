# Tkinter وارد کردن ماژول
import tkinter as tk
from tkinter import ttk


# ساخت پنجره
Window = tk.Tk()


# باز شدن پنجره
print("You Start The Mahdad School Registration Form......")


# نام پنجره فرم ثبت نام آموزشگاه مهداد
Window.title("فرم ثبت نام آموزشگاه مهداد")


# سایز پنجره
# Window.geometry('600x600')


# محدودیت باز کردن پنجره
Window.resizable(0, 0)  # type: ignore


# توابع
# تابع فریم
def F(master, row, column):
    Frame = tk.Frame(master, bg="#f5f5f5")
    Frame.grid(row=row, column=column)
    return Frame


# تابع کادر
def LF(master, text, size, bd, row, column):
    LabelFrame = tk.LabelFrame(
        master,
        text=text,
        font=("B Nazanin", size, "bold"),
        fg="black",
        bd=bd,
        bg="#f5f5f5",
    )
    LabelFrame.grid(row=row, column=column)
    return LabelFrame


# get
def R():
    print(
        [
            EFNFL.get(),
            EFNF.get(),
            EBCN.get(),
            EI.get(),
            ENC.get(),
            EHA.get(),
            ET1.get(),
            ET2.get(),
            EM.get(),
            EW.get(),
            EQ.get(),
            EOC.get(),
        ]
    )


# تابع ورودی
def E(master, width, row, column):
    Entry = tk.Entry(master, font=("B Nazanin", 16), width=width)
    Entry.grid(row=row, column=column)
    return Entry


# تابع گزینه دایره ای
def RB(master, text, size, activebackground, variable, value, row, column):
    Radiobutton = tk.Radiobutton(
        master,
        text=text,
        font=("B Nazanin", size, "bold"),
        fg="#222222",
        activebackground=activebackground,
        variable=variable,
        value=value,
        bg="#f5f5f5",
    )
    Radiobutton.grid(row=row, column=column)
    return Radiobutton


# تابع کم و زیاد عدد ها
def S(master, from_, to, width, row, column):
    Spinbox = tk.Spinbox(
        master,
        from_=from_,
        to=to,
        font=("B Nazanin", 16, "bold"),
        width=width,
    )
    Spinbox.grid(row=row, column=column)
    return Spinbox


# تابع گزینه مربعی
def CB(master, text, font, size, bold, activebackground, row, column):
    Checkbutton = tk.Checkbutton(
        master,
        text=text,
        font=(font, size, bold),
        fg="#222222",
        bg="#f5f5f5",
        activebackground=activebackground,
    )
    Checkbutton.grid(row=row, column=column)
    return Checkbutton


# تابع برچسب
def L(master, text, font, size, bold, fg, bg, width, height, row, column):
    Label = tk.Label(
        master,
        text=text,
        font=(font, size, bold),
        fg=fg,
        bg=bg,
        width=width,
        height=height,
    )
    Label.grid(row=row, column=column)
    return Label


# تابع ویجت
def W(master, padx, pady):
    for Widget in master.winfo_children():
        Widget.grid_configure(padx=padx, pady=pady)
    return Widget


# ارزش تأهل پنجره
VMS = tk.StringVar()

# ارزش بله و خیر
VYAN = tk.StringVar()


# کادر اصلی
# کادر فرم ثبت نام
LFRF = tk.LabelFrame(
    Window,
    text="فرم ثبت نام",
    font=("B Nazanin", 36, "bold"),
    fg="black",
    bd=10,
    bg="#f5f5f5",
)
LFRF.pack(fill="both", expand=True)


# فریم ها
# فریم مشخصات کار آموز
FTP = F(LFRF, 0, 1)
# فریم مشخصات دوره
FCD = F(LFRF, 1, 1)
# فریم آی سی دی ال
FI = F(LFRF, 0, 0)
# فریم قانون
FL = F(LFRF, 1, 0)

# فریم متقاضی شرکت
FAFP = F(FI, 1, 0)


# کادر های پنجره
# کادر نام و نام خانوادگی
LFFNFL = LF(FTP, "نام و نام خانوادگی", 16, 2, 2, 3)
# کادر نام پدر
LFFNF = LF(FTP, "نام پدر", 16, 2, 2, 2)
# کادر شماره شناسنامه
LFBCN = LF(FTP, "شماره شناسنامه", 16, 2, 2, 1)
# کادر تاریخ تولد
LFDOB = LF(FTP, "تاریخ تولد", 16, 2, 2, 0)
# کادر صادره
LFI = LF(FTP, "صادره", 16, 2, 3, 3)
# کادر میزان تحصیلات
LFLOE = LF(FTP, "میزان تحصیلات", 16, 2, 3, 2)
# کادر کد ملی
LFNC = LF(FTP, "کد ملی", 16, 2, 3, 1)
# کادر وضعیت تأهل
LFMS = LF(FTP, "وضعیت تأهل", 16, 2, 3, 0)
# کادر آدرس منزل
LFHA = LF(FTP, "آدرس منزل", 16, 2, 4, 3)
# کادر تلفن اول
LFT1 = LF(FTP, "تلفن", 16, 2, 4, 2)
# کادر تلفن دوم
LFT2 = LF(FTP, "تلفن", 16, 2, 5, 2)
# کادر موبایل
LFM = LF(FTP, "موبایل", 16, 2, 4, 1)
# کادر محل کار
LFW = LF(FTP, "محل کار", 16, 2, 5, 3)

# کادر بله و خیر
LFYAN = LF(FCD, "", 0, 2, 1, 0)

# کادر ۸ مهارت آی سی دی ال
LF8IS = LF(FI, "(۸ مهارت) ICDL", 20, 4, 3, 0)
# کادر آی سی دی ال پیشرفته
LFIA = LF(FI, "ICDL Advanced", 20, 4, 4, 0)


# ورودی های پنجره
# ورودی نام و نام خانوادگی
EFNFL = E(LFFNFL, 16, 0, 0)

# ورودی نام پدر
EFNF = E(LFFNF, 16, 0, 0)

# ورودی شماره شناسنامه
EBCN = E(LFBCN, 16, 0, 0)

# ورودی صادره
EI = E(LFI, 16, 0, 0)

# ورودی کد ملی
ENC = E(LFNC, 16, 0, 0)

# ورودی آدرس منزل
EHA = E(LFHA, 16, 0, 0)

# ورودی تلفن اول
ET1 = E(LFT1, 16, 0, 0)

# ورودی تلفن دوم
ET2 = E(LFT2, 16, 0, 0)

# ورودی موبایل
EM = E(LFM, 16, 0, 0)

# ورودی محل کار
EW = E(LFW, 16, 0, 0)

# ورودی برچسب سوال
EQ = E(FCD, 20, 2, 0)

# ورودی برچسب سایر دوره ها
EOC = E(LFIA, 12, 6, 3)


# فیلد پنجره
# فیلد میزان تحصیلات
CLOE = ttk.Combobox(
    LFLOE,
    font=("B Nazanin", 16),
    value=[  # type: ignore
        "دیپلم",  # type: ignore
        "فوق دیپلم",
        "لیسانس",
        "فوق لیسانس",
        "دکترا",
        "فوق دکترا",
    ],
    width=16,
)
CLOE.grid(row=0, column=0)


# باکس کم و زیاد عدد های پنجره
# باکس کم و زیاد سال ها
SY = S(LFDOB, 1378, 1404, 6, 0, 0)
# باکس کم و زیاد ماه ها
SM = S(LFDOB, 1, 12, 3, 0, 1)
# باکس کم و زیاد روز ها
SD = S(LFDOB, 1, 31, 3, 0, 2)


# گزینه های دایره ای پنجره
# گزینه متأهل
RBM = RB(
    LFMS,
    "متأهل",
    14,
    "white",
    VMS,
    "Married",
    0,
    1,
)
# گزینه مجرد
RBS = RB(
    LFMS,
    "مجرد",
    14,
    "white",
    VMS,
    "Single",
    0,
    0,
)

# گزینه بله
RBY = RB(LFYAN, "بله", 16, "green", VYAN, "Yes", 0, 1)
# گزینه خیر
RBN = RB(LFYAN, "خیر", 16, "red", VYAN, "No", 0, 0)


# گزینه های مربعی پنجره
# گزینه خصوصی
CBP = CB(FAFP, "خصوصی", "B Nazanin", 12, "bold", "white", 0, 0)
# گزینه عمومی
CBP = CB(FAFP, "عمومی", "B Nazanin", 12, "bold", "white", 0, 1)

# گزینه مفاهیم پایه
CBBC = CB(LF8IS, "پایه مفاهیم", "Inter", 10, "", "white", 0, 7)
# گزینه ویندوز
CBW = CB(LF8IS, "Windows", "Inter", 10, "", "white", 0, 6)
# گزینه ورد
CBW = CB(LF8IS, "Word", "Inter", 10, "", "white", 0, 5)
# گزینه اکسل
CBE = CB(LF8IS, "Excel", "Inter", 10, "", "white", 0, 4)
# گزینه اکسس
CBA = CB(LF8IS, "Access", "Inter", 10, "", "white", 0, 3)
# گزینه پاورپوینت
CBP = CB(LF8IS, "Powerpoint", "Inter", 10, "", "white", 0, 2)
# گزینه اینترنت
CBI = CB(LF8IS, "Internet", "Inter", 10, "", "white", 0, 1)
# گزینه امنیت آی تی
CBIS = CB(LF8IS, "IT Security", "Inter", 10, "", "white", 0, 0)
# گزینه ورد پیشرفته
CBAW = CB(LFIA, "پیشرفته Word", "Inter", 10, "", "white", 0, 4)
# گزینه اکسل پیشرفته
CBAE = CB(LFIA, "پیشرفته Excel", "Inter", 10, "", "white", 0, 3)
# گزینه اکسس پیشرفته
CBAA = CB(LFIA, "پیشرفته Access", "Inter", 10, "", "white", 0, 2)
# گزینه پاورپوینت پیشرفته
CBAP = CB(LFIA, "پیشرفته Powerpoint", "Inter", 10, "", "white", 0, 1)
# گزینه ایی کیدس
CBEK = CB(LFIA, "E-kids", "Inter", 10, "", "white", 0, 0)
# گزینه اس پی اس اس
CBS = CB(LFIA, "spss", "Inter", 10, "", "white", 1, 4)
# گزینه اتوکد پیشرفته
CBAA = CB(LFIA, "پیشرفته اتوکد", "Inter", 10, "", "white", 1, 3)
# گزینه اتوکد مفدماتی
CBBA = CB(LFIA, "مقدماتی اتوکد", "Inter", 10, "", "white", 1, 2)
# گزینه مهارت های حرفه ای
CBPS = CB(LFIA, "ای حرفه های مهارت", "Inter", 10, "", "white", 1, 1)
# گزینه حسابداری نرم افزار رافع
CBRSA = CB(LFIA, "رافع افزار نرم حسابداری", "Inter", 10, "", "white", 1, 0)
# گزینه حسابداری نرم افزار هلو
CBHSA = CB(LFIA, "هلو افزار نرم حسابداری", "Inter", 10, "", "white", 2, 4)
# گزینه نت ورک پلاس
CBNP = CB(LFIA, "Network+", "Inter", 10, "", "white", 2, 3)
# گزینه تری دی مکس
CB3M = CB(LFIA, "3D MAX", "Inter", 10, "", "white", 2, 2)
# گزینه طراحی صفحات وب
CBWE = CB(
    LFIA,
    "Web Editing\nوب صفحات طراحی",
    "Inter",
    10,
    "",
    "white",
    2,
    1,
)
# گزینه فتوشاپ
CBP = CB(LFIA, "Photoshop", "Inter", 10, "", "white", 2, 0)
# گزینه ایی تبس
CBE = CB(LFIA, "Etabs", "Inter", 10, "", "white", 3, 4)
# گزینه پایتون
CBP = CB(LFIA, "پایتون", "Inter", 10, "", "white", 3, 3)
# گزینه اسکچاپ
CBS = CB(LFIA, "اسکچاپ", "Inter", 10, "", "white", 3, 2)
# گزینه برنامه نویسی اسکرچ
CBSP = CB(LFIA, "اسکرچ نویسی برنامه", "Inter", 10, "", "white", 3, 1)
# گزینه جی آی اس
CBG = CB(LFIA, "GIS", "Inter", 10, "", "white", 3, 0)
# گزینه سیف
CBS = CB(LFIA, "Safe", "Inter", 10, "", "white", 4, 2)

# گزینه قبول
CBA = CB(FL, "قبول", "B Nazanin", 16, "bold", "white", 4, 1)


# برچسب های پنجره
# برچسب مشخصات کار آموز
LTP = L(
    FTP,
    "مشخصات کارآموز",
    "B Nazanin",
    20,
    "bold",
    "#222222",
    "#f5f5f5",
    0,
    0,
    0,
    3,
)
# برچسب باکس خالی اول (اضافی)
LEB = L(
    FTP,
    "Empty Box",
    "Tahoma",
    10,
    "",
    "#222222",
    "#444444",
    0,
    0,
    4,
    0,
)
# برچسب باکس خالی دوم (اضافی)
LEB = L(
    FTP,
    "Empty Box",
    "Tahoma",
    10,
    "",
    "#222222",
    "#444444",
    0,
    0,
    5,
    0,
)
# برچسب باکس خالی سوم (اضافی)
LEB = L(
    FTP,
    "Empty Box",
    "Tahoma",
    10,
    "",
    "#222222",
    "#444444",
    0,
    0,
    5,
    1,
)
# برچسب مشخصات کار آموز خالی اول اضافی
LTPE = L(FTP, "", "", 0, "", "#222222", "#4CAF50", 14, 1, 0, 0)
# برچسب مشخصات کار آموز خالی دوم اضافی
LTPE = L(FTP, "", "", 0, "", "#222222", "#f5f5f5", 0, 3, 6, 0)

# برچسب سوال سایر دوره های کامپیوتر اول
LCCQ = L(
    FCD,
    "آیا تاکنون در دوره های آموزش کامپیوتر شرکت نموده اید ؟",
    "B Nazanin",
    16,
    "bold",
    "#222222",
    "#f5f5f5",
    0,
    0,
    1,
    1,
)
# برچسب سوال سایر دوره های کامپیوتر دوم
LCCQ = L(
    FCD,
    "اگر جواب مثبت است در کدام آموزشگاه و چه دوره اي ؟",
    "B Nazanin",
    16,
    "bold",
    "#222222",
    "#f5f5f5",
    0,
    0,
    2,
    1,
)

# برچسب متقاضی شرکت اول
LAFP = L(
    FI,
    "متقاضی شرکت در دوره بصورت",
    "B Nazanin",
    14,
    "bold",
    "#222222",
    "#f5f5f5",
    0,
    0,
    0,
    0,
)
# برچسب متقاضی شرکت دوم
LAFP = L(
    FI,
    "متقاضی شرکت در کدام یک از دوره های آموزشی زیر هستید ؟",
    "B Nazanin",
    16,
    "bold",
    "#222222",
    "#f5f5f5",
    0,
    0,
    2,
    0,
)

# برچسب ۱۰ دایره تو خالی اول
LOCC = L(
    LFIA,
    "•" * 10,
    "Tahoma",
    14,
    "bold",
    "#4CAF50",
    "#f5f5f5",
    0,
    0,
    5,
    0,
)
# برچسب ۱۰ دایره تو خالی دوم
LOCC = L(
    LFIA,
    "•" * 10,
    "Tahoma",
    14,
    "bold",
    "#4CAF50",
    "#f5f5f5",
    0,
    0,
    5,
    1,
)
# برچسب ۱۰ دایره تو خالی سوم
LOCC = L(
    LFIA,
    "•" * 10,
    "Tahoma",
    14,
    "bold",
    "#4CAF50",
    "#f5f5f5",
    0,
    0,
    5,
    2,
)
# برچسب ۱۰ دایره تو خالی چهارم
LOCC = L(
    LFIA,
    "•" * 10,
    "Tahoma",
    14,
    "bold",
    "#4CAF50",
    "#f5f5f5",
    0,
    0,
    5,
    3,
)
# برچسب ۱۰ دایره تو خالی پنجم
LOCC = L(
    LFIA,
    "•" * 10,
    "Tahoma",
    14,
    "bold",
    "#4CAF50",
    "#f5f5f5",
    0,
    0,
    5,
    4,
)
# برچسب سایر دوره ها
LOC = L(
    LFIA,
    "سایر دوره ها",
    "B Nazanin",
    16,
    "bold",
    "#222222",
    "#f5f5f5",
    0,
    0,
    6,
    4,
)
# برچسب آی سی دی ال پیشرفته خالی اضافی
LIAE = L(LFIA, "", "", 0, "", "#222222", "#f5f5f5", 0, 0, 8, 0)

# برچسب قانون خط اول
LL = L(
    FL,
    "پس از ثبت نام در صورتی که کار آموز به هر دلیل یا علت از تحصیل در آموزشگاه و شرکت در کلاس های آن",
    "Roya",
    12,
    "bold",
    "#222222",
    "#f5f5f5",
    0,
    0,
    1,
    1,
)
# برچسب قانون خط دوم
LL = L(
    FL,
    "منصرف و توانایی و امکان شرکت در کلاس ها را قبل و بعد از شروع دوره نداشته باشد",
    "Roya",
    12,
    "bold",
    "#222222",
    "#f5f5f5",
    0,
    0,
    2,
    1,
)
# برچسب قانون خط سوم
LL = L(
    FL,
    "هیچ وجهی از شهریه دریافتی توسط آموزشگاه به کار آموز مسترد نخواهد شد",
    "Roya",
    12,
    "bold",
    "#222222",
    "#f5f5f5",
    0,
    0,
    3,
    1,
)


# دکمه ثبت نام
B = tk.Button(
    FL,
    text="ثبت نام و نمایش اطلاعات",
    font=("B Nazanin", 16, "bold"),
    fg="white",
    bg="#4CAF50",
    activebackground="green",
    command=R,
)
B.grid(row=5, column=1)


# کانفیگ های جا به جایی ویجت های کادر ها و فریم ها
# کانفیگ جا به جایی ویجت های کادر فرم ثبت نام
W1 = W(LFRF, 16, 0)
# کانفیگ جا به جایی ویجت های فریم مشخصات دوره
W2 = W(FCD, 10, 12)
# کانفیگ جا به جایی ویجت های فریم متقاضی شرکت
W3 = W(FAFP, 32, 0)
# کانفیگ جا به جایی ویجت های فریم آی سی دی ال
W4 = W(FI, 0, 0)
# کانفیگ جا به جایی ویجت های کادر ۸ مهارت آی سی دی ال
W5 = W(LF8IS, 1, 0)


# اجرای پنجره
Window.mainloop()


# بسته شدن پنجره
print("You Close The Mahdad School Registration Form......")
