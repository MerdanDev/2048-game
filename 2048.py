from tkinter import *  #tkinter kitaphanasyndan ähli 
import glob, os
# komponentleri çagyrýarysm muny etmek hökmän däl sebäbi
# içinden ulanmaýan komponentlerimiz bar.  
from random import randint
# random kitaphanysyndan randint komponentini çagyrýarys,
# bu bize kompýutere tötänleýin hereketi etdirmek üçin gerek.

tk = Tk() #tkinteri tk diýip atlandyrýarys, onuň arka fonuny sazlaýarys,
# bize her bir san görnüşi üçin aýratyn surat gerek, olar hökmany ýagdaýda deň bolmaly.
# Suratyň beter uly bolmazlygyna üns beriň!

img_list = []
for filename in sorted(glob.glob('gif/*.gif'), key=os.path.getmtime): #.gif format üçin
    img = PhotoImage(file = filename)
    img_list.append(img)

img_list.reverse()
img_list.insert(0, img_list[-1])
del img_list[-1]

buttons, num_arrs = [], []  # ýörite buttonlary saklamak üçin buttons
# diýen listi ulanýarys. Olaryň bahalaryny saklamak üçin num_arrs 
# listini peýdalanýarys
maximum, selected_btn = 0, 0 # maximum bize oýunyň ölçegini saklaýarys,
# bu bize listler bilen işlemek üçin ulanýarys. selected_btn biz 
# default button hökmünde ulanýarys
button_select = True # bu üýtgeýän ululyk bize menýy we oýun panelinden 
# klawituranyň düwmelerini işlemäge rugsat bermek üçin ulanylýar.
# ýagny eger true bolsa menýu panelinde düwmeler işleýär, 
# bolmasa oçun panelinde işleýär

def set_num(): # bu funksiýa düwmeleriň bahalaryna görä suratyny üýtgetýer 
    for x in range(len(num_arrs)):
        for y in range(len(num_arrs)):
            if num_arrs[x][y] == 0:
                buttons[x][y].configure(image = img_list[0])
            elif num_arrs[x][y] == 2:
                buttons[x][y].configure(image = img_list[1])
            elif num_arrs[x][y] == 4:
                buttons[x][y].configure(image = img_list[2])
            elif num_arrs[x][y] == 8:
                buttons[x][y].configure(image = img_list[3])
            elif num_arrs[x][y] == 16:
                buttons[x][y].configure(image = img_list[4])
            elif num_arrs[x][y] == 32:
                buttons[x][y].configure(image = img_list[5])
            elif num_arrs[x][y] == 64:
                buttons[x][y].configure(image = img_list[6])
            elif num_arrs[x][y] == 128:
                buttons[x][y].configure(image = img_list[7])
            elif num_arrs[x][y] == 256:
                buttons[x][y].configure(image = img_list[8])
            elif num_arrs[x][y] == 512:
                buttons[x][y].configure(image = img_list[9])
            elif num_arrs[x][y] == 1024:
                buttons[x][y].configure(image = img_list[10])
            elif num_arrs[x][y] == 2048:
                buttons[x][y].configure(image = img_list[11])
            elif num_arrs[x][y] == 4096:
                buttons[x][y].configure(image = img_list[12])
            elif num_arrs[x][y] == 8192:
                buttons[x][y].configure(image = img_list[13])
            elif num_arrs[x][y] == 16384:
                buttons[x][y].configure(image = img_list[14])
            else:
                buttons[x][y].configure(text = num_arrs[x][y], padx = 43, padt = 43)

def give_rand_num(): # bu funksiýa tötänleýin ýerden,
# ýagny san bolmadyk ýerden san çykarýar ol 2 ýa-da 4 bolup bilýär
    global maximum
    
    while True:
        # print("rand")
        x_pos = randint(0, maximum - 1)
        y_pos = randint(0, maximum - 1)
        if num_arrs[x_pos][y_pos] == 0:
            rand_num = randint(0, 1)
            if rand_num == 0:
                num_arrs[x_pos][y_pos] = 2
            else:
                num_arrs[x_pos][y_pos] = 4    
            break
    set_num()

def move(direction):
    global maximum
    check_changed = []
    for x in range(len(num_arrs)):
        check_changed.append([])
        for y in range(len(num_arrs)):
            check_changed[x].append(num_arrs[x][y])
    # print(check_changed)
    if direction == 3 or direction == 2:
        second_arr = []
        for x in range(len(num_arrs)):
            second_arr.append([])
            for y in range(len(num_arrs)):
                second_arr[x].append(num_arrs[y][x])

        for x in range(len(second_arr)):
            maximum = len(second_arr)
            y = 0
            if direction == 3:
                second_arr[x].reverse()
            while y < maximum:
                if y == maximum - 1:
                    y += 1
                    continue

                elif second_arr[x][y] == 0:
                    del second_arr[x][y]
                    maximum -= 1
                    
                elif second_arr[x][y] == second_arr[x][y + 1]:
                    second_arr[x][y] *= 2
                    del second_arr[x][y + 1]
                    maximum -= 1
                    y +=1
                    
                elif second_arr[x][y] != second_arr[x][y + 1]:
                    if second_arr[x][y + 1] == 0:
                        del second_arr[x][y + 1]
                        maximum -= 1
                    else:
                        y += 1
                    
            for y in range(len(second_arr) - len(second_arr[x])):
                second_arr[x].append(0)

            if direction == 3:
                second_arr[x].reverse()
        for x in range(len(num_arrs)):
            for y in range(len(num_arrs)):
                num_arrs[y][x] = second_arr[x][y]
        maximum = len(num_arrs)

    elif direction == 4 or direction == 1:
        for x in range(len(num_arrs)):
            maximum = len(num_arrs)
            y = 0
            if direction == 4:
                num_arrs[x].reverse()
            
            while y < maximum:
                if y == maximum - 1:
                    y += 1
                    continue
                
                elif num_arrs[x][y] == 0:
                    del num_arrs[x][y]
                    maximum -= 1
                    
                elif num_arrs[x][y] == num_arrs[x][y + 1]:
                    num_arrs[x][y] *= 2
                    del num_arrs[x][y + 1]
                    maximum -= 1
                    y +=1
                    
                elif num_arrs[x][y] != num_arrs[x][y + 1]:
                    if num_arrs[x][y + 1] == 0:
                        del num_arrs[x][y + 1]
                        maximum -= 1
                    else:
                        y += 1
                    
            for y in range(len(num_arrs) - len(num_arrs[x])):
                num_arrs[x].append(0)

            if direction == 4:
                num_arrs[x].reverse()

        maximum = len(num_arrs)
    # print(check_changed)
    # print(num_arrs)

    if check_changed != num_arrs:
        give_rand_num()

def restart():
    global num_arrs
    global buttons
    for x in range(len(num_arrs)):
        for y in range(len(num_arrs)):
            buttons[x][y].grid_forget()
    buttons, num_arrs = [], []
    button0.grid(row = 1, column = 0)
    button1.grid(row = 2, column = 0)
    button2.grid(row = 3, column = 0)

def key_press(event):
    global button_select
    global selected_btn
    # print(event.keysym)

    if button_select:
        if (event.keysym == "Up" or event.char == 'w') and selected_btn > 0:
            print("worked up", selected_btn, selected_btn>0)
            selected_btn -= 1
            btns[selected_btn+1].configure(bg = '#ffffff')
            btns[selected_btn].configure(bg = '#aaaaaa')
        elif (event.keysym == "Down" or event.char == 's') and selected_btn < 2:
            print("worked down", selected_btn, selected_btn<2)
            selected_btn += 1
            btns[selected_btn-1].configure(bg = '#ffffff')
            btns[selected_btn].configure(bg = '#aaaaaa')
        elif event.keysym == "Return":
            button_select = False
            config(selected_btn+4)
        
    elif not button_select:
        if event.keysym == "Left" or event.char == 'a':
            move(1)
        elif event.keysym == "Up" or event.char == 'w':
            move(2)
        elif event.keysym == "Down" or event.char == 's':
            move(3)
        elif event.keysym == "Right" or event.char == 'd':
            move(4)
        elif event.keysym == "Escape":
            button_select = True
            restart()

def config(length):
    global maximum
    global button_select
    if button_select == True:
        button_select = False
    maximum = length
    for x in range(length):
        buttons.append([])
        num_arrs.append([])
        for y in range(length):
            buttons[x].append(Button(tk, image = img_list[0], bd = 1, bg = '#bf6e3e'))
            buttons[x][y].grid(row = x, column = y)
            num_arrs[x].append(0)
    give_rand_num()

    # button_left = Button(tk, text = "←", padx = 42, pady = 42, command = lambda: move(1))
    # button_left.grid(row = length + 1, column = 0)
    # button_up = Button(tk, text = "↑", padx = 42, pady = 42, command = lambda: move(2))
    # button_up.grid(row = length, column = 1)
    # tk.bind("<Up>", key_press)
    # button_down = Button(tk, text = "↓", padx = 42, pady = 42, command = lambda: move(3))
    # button_down.grid(row = length + 1, column = 1)
    # tk.bind("<Down>", key_press)
    # button_right = Button(tk, text = "→", padx = 42, pady = 42, command = lambda: move(4))
    # button_right.grid(row = length + 1, column = 2)
    # tk.bind("<Right>", key_press)
    button0.grid_forget()
    button1.grid_forget()
    button2.grid_forget()
tk.bind("<Key>", key_press)

button0 = Button(tk, text = "4x4", bd = 5, bg = '#aaaaaa', padx = 42, pady = 10, command = lambda: config(4))
button0.grid(row = 1, column = 0)
button1 = Button(tk, text = "5x5", bd = 5, padx = 42, pady = 10, command = lambda: config(5))
button1.grid(row = 2, column = 0)
button2 = Button(tk, text = "6x6", bd = 5, padx = 42, pady = 10, command = lambda: config(6))
button2.grid(row = 3, column = 0)


btns = [button0, button1, button2]

mainloop()