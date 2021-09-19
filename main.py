from tkinter import *
from tkinter import messagebox
from tkinter.tix import Tk
import sys
import pygame
from PIL.ImageTk import PhotoImage
from pygame import mixer

tk = Tk()
w, h = tk.winfo_screenwidth(), tk.winfo_screenheight()
tk.geometry("1400x800")
# tk.wm_state('zoomed')
our_image = PhotoImage(file='img/map.png')
our_label = Label(tk)
our_label.image = our_image
our_label['image'] = our_label.image
our_label.place(x=50, y=0)


def destroy():  # Досрочный Game Over
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        sys.exit()


b1 = Button(tk, text="Start", command=tk.destroy, fg='Navy', font=("Georgia", 16, "bold"))
b1.place(x=1030, y=500, width=70, height=40)
b1["bg"] = "SpringGreen"

b2 = Button(tk, text="Quit", command=destroy, fg='RoyalBlue', font=("Georgia", 16, "bold"))
b2.place(x=1030, y=600, width=70, height=40)
b2["bg"] = "Navy"
tk.mainloop()

pygame.init()
# create the GAME screen
screen = pygame.display.set_mode((1370, 700))
pygame.display.set_caption('супермаркет "АТБ"')

# mixer.music.load("ozhidanijai.mp3")
# mixer.music.play(-1)


# ATB
width = 1365
height = 700
floor = pygame.image.load('img/floor.png')
floorImg = pygame.transform.scale(floor, (width, height))

img_size = 120
# gerl
FPS = 100
fpsClock = pygame.time.Clock()
ball1Img = pygame.image.load('img/gerl.png')
x1 = y1 = 200  # координаты
x3 = y3 = 100
xv1 = yv1 = xv2 = yv2 = xv3 = yv3 = 0.5  # скорость
check = parity = False

ball1Img = pygame.transform.scale(ball1Img, (img_size, img_size))
ball1Img.set_colorkey((255, 255, 255))
# Player
playerImg = pygame.image.load('img/player.png')
playerX = 30
playerY = 700
playerImg = pygame.transform.scale(playerImg, (img_size, img_size))
playerImg.set_colorkey((255, 255, 255))
playerX_change = 0
playerY_change = 0  # Стартовые точки

# Security_man
SmanImg = pygame.image.load('img/Sman.png').convert()
SmanX = 1100
SmanY = 500  # Стартовые точки
SmanX_change = 0
SmanY_change = 1
# Change Img (no white fon)
SmanImg.set_colorkey((255, 255, 255))
SmanImg = pygame.transform.scale(SmanImg, (img_size, img_size))

manImg = pygame.image.load('img/man.png').convert()
manX = 100
manY = 300  # Стартовые точки
manX_change = 2
manY_change = 0
# Change Img (no white fon)
manImg.set_colorkey((255, 255, 255))
manImg = pygame.transform.scale(manImg, (img_size, img_size))
# All products:
meatIng = pygame.image.load('img/мяясо.jpg').convert()
meatX = 50
meatY = 350
img_sizeM = 50
meatIng.set_colorkey((255, 255, 255))
meatIng = pygame.transform.scale(meatIng, (img_sizeM, img_sizeM))

vegetablesImg = pygame.image.load('img/v.jpg')
vegetX = 250
vegetY = 50
img_sizeV = 50

eggsImg = pygame.image.load('img/egg.png')
eggsX = 550
eggsY = 50

bordImg = pygame.image.load('img/price.png')
bordX = 530
bordY = 450

cashboxImg = pygame.image.load('img/cashb — копия.png')
cashbX = 800
cashbY = 270

products = {'хлеб': 15, 'молоко': 20, 'яйца': 30.50, 'сахар': 22.50, 'колбаса': 60, 'масло': 27, 'мясо': 90,
            'капуста': 10, 'лук': 12, 'рыба': 80,
            'гречка': 40, 'рис': 24.60, 'майонез': 28.90}
# Summ =============0000000=========0000000000========0000000=====0000
root1 = Tk()
root1.geometry('900x400+200+100')
root1['bg'] = 'white'

money = 0


def yes():
    global money
    money = float(entry_1.get())
    win = Tk()
    win.geometry('300x250+530+180')
    lbl0 = Label(win, text='У Вас с собой:', font=("Cambria", 20), fg="blue")
    lbl0.place(x=60, y=10)
    lbl = Label(win, text=[money], font=("Cambria", 40), fg="blue")
    lbl.place(x=100, y=60)
    lbl1 = Label(win, text='Грв.', font=("Cambria", 30), fg="blue")
    lbl1.place(x=100, y=150)
    root1.destroy()
    win.after(1000, lambda: win.destroy())
    win.mainloop()
    print(money)


main_text = Label(root1, text="Сегодня мы идем в супермаркет за продуктами!",
                  fg='blue', bg='white',
                  font=("Cambria", 28))
main_text2 = Label(root1, text='''Достаточное количество товаров сделают поход
 в супермаркет "АТБ" быстрым, удобным и комфортным.''',
                   bg='white', font=("Cambria", 18))
label = Label(root1, text="Сколько денег берем?",
              bg='white', font=("Cambria", 16))
entry_1 = Entry(root1, font=("Ubuntu", 25), justify='center', bg='LightCyan')
text = Label(root1, text='Введите число:', font='Cambria', bg='LightCyan')
btn = Button(root1, text="Применить", command=yes, bg="DodgerBlue", font='Cambria')
main_text.place(x=40, y=30)
main_text2.place(x=100, y=90)
label.place(x=255, y=180)
text.place(x=255, y=220)
entry_1.place(x=260, y=250)
entry_1.focus_set()
btn.place(x=700, y=310)

root1.mainloop()
root1.quit()


# Sound "Vinnik"
# mixer.music.load("music.mp3")
# mixer.music.play(-1)


# Crafting items
def player(x, y):
    screen.blit(playerImg, (x, y))


def Sman(x, y):
    screen.blit(SmanImg, (x, y))


def man(x, y):
    screen.blit(manImg, (x, y))


def meat(x, y):
    screen.blit(meatIng, (x, y))


def veget(x, y):
    screen.blit(vegetablesImg, (x, y))


def eggs(x, y):
    screen.blit(eggsImg, (x, y))


def bord(x, y):
    screen.blit(bordImg, (x, y))


def cashbox(x, y):
    screen.blit(cashboxImg, (x, y))


def store_products():
    root7 = Tk()
    root7.geometry('830x300+300+230')
    story = Label(root7, text='''В магазине сегодня распродажа!                    

    масло   -  54 грн           мясо    - 110 грн          капуста - 13 грн
    сахар   -  24.80 грн        рыба    - 80 грн           лук     - 12 грн
    молоко  -  26 грн           колбаса - 60 грн           хлеб    - 15 грн

    яйца    -  32.50 грн        рис     - 24.60 грн
    майонез -  28.90 грн        гречка  - 38.40 грн
                                                                                                    ''',
                  font=('Arial', 20), fg='blue')
    story.pack()
    root7.after(4000, lambda: root7.destroy())
    root7.mainloop()


def no_product():
    root4 = Tk()
    root4.geometry('700x100+300+250')
    root4.title('Нет продукта')
    root4['bg'] = 'PapayaWhip'
    text2 = Label(root4, text='Извините, такого продукта в нашем магазине нет!',
                  bg='PapayaWhip', fg='Red', font=('Comfortaa', 16))
    text2.place(x=30, y=20)

    root4.after(1000, lambda: root4.destroy())
    root4.mainloop()


cart = ''
money_start = money


def prod():
    spisok = '''    хлеб, яйца, масло.'''

    hh = '''Вы можете сделать следующее:        Введите цифру      1 или ведите цифру   2    или введите цифру  3   
   НАПИШИТЕ, ЧТО БУДЕТЕ БРАТЬ!!'''

    def prod():
        root2 = Tk()
        root2.geometry('400x170+450+250')
        root2.title('Продукты в АТБ')

        def prodi():
            global user_input
            user_input = (entry_1.get())
            root2.destroy()

        def how_much():
            window = Tk()
            window.geometry('300x250+530+180')
            lbl0 = Label(window, text='У Вас примерно:', font=("Cambria", 22), fg="blue")
            lbl0.place(x=60, y=10)
            lbl = Label(window, text=[money], font=("Cambria", 40), fg="blue")
            lbl.place(x=100, y=60)
            lbl1 = Label(window, text='Грв.', font=("Cambria", 20), fg="blue")
            lbl1.place(x=100, y=150)
            window.after(2000, lambda: window.destroy())
            window.mainloop()

        def end():
            pass

        label = Label(root2, text="Какой продукт берём?", fg='#000875', font=("Cambria", 20))
        entry_1 = Entry(root2, font=("Ubuntu", 20), fg='#000875', bg='LightCyan', justify='center')
        text = Label(root2, text='Название продукта:', fg='#DA0700', font='Cambria')
        btn = Button(root2, text="Беру!", command=prodi, bg="lime", font='Cambria')
        btn2 = Button(root2, text="Сейчас у маня...", command=how_much, bg="LightGray", font='Cambria')
        btn3 = Button(root2, text="Хорош", command=end, font='Cambria')
        label.place(x=50, y=10)
        text.place(x=110, y=50)
        entry_1.place(x=40, y=70)
        entry_1.focus_set()
        btn.place(x=40, y=120)
        btn2.place(x=190, y=120)
        btn3.place(x=320, y=120)
        root2.mainloop()

    global money
    money_start = money


    buyin = dict()

    def my_products_and_money():
        print("my_products_and_money")
        # print(f'В карзине у Вас:  {cart}')
        # print("Доступно:", money, "грн.")

    def stop_climbing():
        root6 = Tk()
        root6.geometry('600x130+400+300')
        story = Label(root6, text='''Возможно у Вас недостаточно денег,
    для будущих покупок! Пройдите к кассе!''', font=('Arial', 20), fg='blue')
        story.place(x=5, y=20)
        root6.after(2000, lambda: root6.destroy())
        root6.mainloop()

    run = True
    while run:
        prod()
        if user_input == '1':
            print("Сейчас, сейчас где-то в кармане был список, ага вот:  ")
            print(spisok)
            my_products_and_money()

        elif user_input == '2':
            print('Так в корзине у нас  .  .  .  ')

        elif user_input == '3':
            store_products()
            print(store_products)
            run = False

        elif user_input == 'q':
            run = False

        else:
            if not user_input.strip():
                print('error: empty')
                continue
            elif user_input not in products:
                no_product()
                print('Такого продукта в магазине нет!')
                continue

            product_price = products[user_input]

            buyin[user_input] = products[user_input]
            if product_price > money:
                print('НЕдостаточно денег!')
                stop_climbing()
                my_products_and_money()
                run = False
            else:
                money -= product_price
                global cart
                cart += f'{user_input} ({product_price})'
                my_products_and_money()

                buyin[user_input] = products[user_input]
                if money <= product_price:
                    print("Хватить лазить!")
                    stop_climbing()
                    run = False


def speak():
    root8 = Tk()
    root8.geometry('420x100+550+200')
    lbl = Label(root8, text='''Если Вам интересны наши цены
    подойдите к табличке!''', font=("Cambria", 20), fg="DarkSlateBlue")
    lbl.place(x=1, y=15)
    root8.after(2000, lambda: root8.destroy())
    root8.mainloop()


def sms():
    # Вы оплатили товар
    root3 = Tk()
    root3.geometry("500x200+350+250")
    root3.title('Window name')
    root3['bg'] = '#FFA07A'

    def goodluck():
        sl.destroy()
        btn1.destroy()
        btn2.destroy()
        gd = Label(root3, text="Хорошего Вам дня!", font="Broadway 20", fg="green", bg="#C0C0C0")
        gd.place(x=120, y=70)

    def shet():
        sl.destroy()
        btn1.destroy()
        btn2.destroy()
        gd = Label(root3, text="Вызываем полицию?", font="Broadway 20", fg="black", bg="#C0C0C0")
        gd.place(x=100, y=70)

    sl = Label(text='У Вас оплачены продукты?', font='Comfortaa 20', fg='black', bg='#FFA07A')
    btn1 = Button(root3, text='ДА', bg='#228B22', fg='#ccc', width=13, height=3, command=goodluck)
    btn2 = Button(root3, text='НЕТ', bg='#FF0000', fg='#ccc', width=13, height=3, command=shet)
    sl.pack()
    btn1.place(x=120, y=80)
    btn2.place(x=270, y=80)

    root3.mainloop()


running = True
while running:
    for event in pygame.event.get():  # button X == Geme End
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5

            if event.key == pygame.K_DOWN:
                playerY_change = 5
            if event.key == pygame.K_UP:
                playerY_change = -5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 1265:
        playerX = 1265

    playerY += playerY_change
    if playerY <= 0:
        playerY = 0
    elif playerY >= 600:
        playerY = 600

    # Sman moving
    SmanY += SmanY_change
    if SmanY <= 0:
        SmanY_change = 1
    elif SmanY >= 600:
        SmanY_change = -1

    # man moving
    manX += manX_change
    if manX <= 100:
        manX_change = 2
    elif manX >= 700:
        manX_change = -2

    # Сталкновение с рабочим
    if (playerX > manX - 40) and (playerX < manX + 40) and (playerY > manY - 40) and (playerY < manY + 40):
        speak()
        playerY -= 40

    # Сталкновение с охраной
    if (playerX > SmanX - 40) and (playerX < SmanX + 40) and (playerY > SmanY - 40) and (playerY < SmanY + 40):
        sms()
        playerX -= 45

    # Столкновение с мясом
    if (playerX > meatX - 40) and (playerX < meatX + 40) and (playerY > meatY - 40) and (playerY < meatY + 40):
        prod()
        playerY += 20
        playerX += 10

        # Сотолкновение с овощами
    if (playerX > vegetX - 40) and (playerX < vegetX + 40) and (playerY > vegetY - 40) and (playerY < vegetY + 40):
        prod()
        playerX -= 45

        # Сотолкновение с яйцами
    if (playerX > eggsX - 40) and (playerX < eggsX + 40) and (playerY > eggsY - 40) and (playerY < eggsY + 40):
        prod()
        playerX -= 45

        # Сотолкновение с стеной
    if (playerX > bordX - 40) and (playerX < bordX + 40) and (playerY > bordY - 40) and (playerY < bordY + 40):
        store_products()
        playerY += 45

        # Сотолкновение с cashbox
    if (playerX > cashbX - 40) and (playerX < cashbX + 40) and (playerY > cashbY - 40) and (playerY < cashbY + 40):
        root9 = Tk()
        root9.geometry('350x400+500+200')
        lbl = Label(root9, text="Ваш чек:", font=("Cambria", 20))
        lbl1 = Label(root9, text=f"Вы дали: {money_start} грн.", font=("Cambria", 20))
        lbl2 = Label(root9, text="--------------------------------", font=("Cambria", 20))
        lbl3 = Label(root9, text=f"{cart}", font=("Cambria", 20))
        lbl4 = Label(root9, text="--------------------------------", font=("Cambria", 20))
        lbl5 = Label(root9, text=f"Сдача: {money} грн.", font=("Cambria", 20))
        lbl.place(x=10, y=15)
        lbl1.place(x=10, y=55)
        lbl2.place(x=10, y=95)
        lbl3.place(x=10, y=130)
        lbl4.place(x=10, y=260)
        lbl5.place(x=10, y=300)
        root9.after(2000, lambda: root9.destroy())
        root9.mainloop()
        playerY += 45

        # # my_products_and_money()
        # for prod, price in buyin.items():
        #     print(f"{prod}  --- {price} грн.")
        # print('Приходите к нам ещё! :)')

    fpsClock.tick(FPS)
    screen.fill((33, 46, 123))
    screen.blit(floorImg, (0, 0))
    screen.blit(ball1Img, (x1, y1))
    Sman(SmanX, SmanY)
    cashbox(cashbX, cashbY)
    man(manX, manY)
    eggs(eggsX, eggsY)
    meat(meatX, meatY)
    veget(vegetX, vegetY)
    bord(bordX, bordY)
    player(playerX, playerY)

    pygame.display.update()

    x1 += xv1
    y1 += yv1
    xv1 = -xv1 if (x1 > 800 - 49 or x1 < 0) else xv1  # отскок
    yv1 = -yv1 if (y1 > 600 - 49 or y1 < 0) else yv1  # от стенок
