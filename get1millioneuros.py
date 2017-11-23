import sys, random, tkinter
from tkinter import messagebox
from tkinter import *

gui = tkinter.Tk()

gui.geometry('910x450')

gui.title('GET 1 MILLION EUROS!')

q1 = ['What city is the capital of England?', 'a - London', 'b - Moscow', 'c - Prague', 'd - Paris']
q2 = ['What was the name of the Greek goddess of love?', 'a - Athena', 'b - Aphrodite', 'c - Euterpe', 'd - Hecate']
q3 = ['Where will the Mundial 2018?', 'a - Germany', 'b - France', 'c - Russia', 'd - England']
q4 = ['Which the sience is called queen every siences?', 'a - Biology', 'b - History', 'c - Physics', 'd - Maths']
q5 = ['What city is the capital of China:', 'a - Beijing', 'b - Berlin', 'c - Tokyo', 'd - Moscow']
q6 = ['The famous Polish computer game is:', 'a - Silent Hill',  'b - The Witcher', 'c - Fifa', 'd - Resident Evil']
q7 = ['Which ocean is the biggest?', 'a - Atlantic Ocean', 'b - Indian Ocean', 'c - Pacific Ocean', 'd - Arctic Ocean']
q8 = ['The famous movie which action was in the cosmos is:', 'a - The Predator', 'b - Rambo', 'c - The Terminator', 'd - The Star Wars']

q9 = ['Where is Albania?', 'a - Europe', 'b - Asia', 'c - Africa', 'd - South America']
q10 = ['The light on the North Pole?', 'a - Rainbow', 'b - Aurora borealis', 'c - Glow', 'd - Mirage']
q11 = ['What is the name of the power unit', 'a - Decibel', 'b - Volt', 'c - Watt', 'd - Boron']
q12 = ['What is the name the famous car with Italy?', 'a - BMW', 'b - Mercedes', 'c - Maseratti', 'd - Ferrari']
q13 = ['The games console made by Microsoft is:', 'a - Xbox', 'b - Pegasus', 'c - Playstation', 'd - Nintendo']
q14 = ['What is the name a fameous polish painter which painted darkness pictures?', 'a - Leonardo Davinci', 'b - Zdzisław Beksiński', 'c - Jan Matejko', 'd - Julian Tuwim']
q15 = ['How many people live on the world in 2017 year?', 'a - 6.5 billion', 'b - 7 billion', 'c - 7.5 billion', 'd - 8 billion']
q16 = ['What is the name the tallest building in the world?', 'a - Freedom Tower, ', 'b - Warsaw Spire', 'c - Empire State Building', 'd - Burdż Chalifa']

q17 = ['Wchich Superhero drew Bob Kane?', 'a - Batman', 'b - Spiderman', 'c - Captain America', 'd - Superman']
q18 = ['How years ago sank The Titanic?', 'a - 1911', 'b - 1912', 'c - 1913', 'd - 1914']
q19 = ['What animal is particulary treat in China?', 'a - Tiger', 'b - Elephant', 'c - Panda', 'd - Bear']
q20 = ['Which place on list the tallest peaks is peak Broad Peak?', 'a - First', 'b - Second', '3 - Fifth', 'd - Twelfth']
q21 = ['What is the marasaka?', 'a - Cherry', 'b - Apple', 'c - Fig', 'd - Pear']
q22 = ['The myrmecology is branch science about:', 'a - Butterflies', 'b - Ants', 'c - Frogs', 'd - Beetles']
q23 = ['Who is director movie "The Matador"?', 'a - Christopher Nolan ', 'b - Andrew Wajda', 'c - Pedro Almodóvar', 'd - Ron Howard']
q24 = ['How many people live in Japan?', 'a - 50 millions', 'b - 85 millions', 'c - 110 millions', 'd - 127 millions']

draw_easy = [q1,q2,q3,q4,q5,q6,q7,q8]
draw_medium = [q9,q10,q11,q12,q13,q14,q15,q16]
draw_hard = [q17,q18,q19,q20,q21,q22,q23,q24]

random.seed()
score = 0
gameover = 0
quest = 0
answer_a = 0
answer_b = 0
answer_c = 0
answer_d = 0
answer_good = 0
circle_1 = 0
circle_2 = 0
circle_3 = 0
circle_access = 0
early_end = 0
exit_cash = 0
current_cash = 0
draw_remove_easy = 0
draw_remove_medium = 0
draw_remove_hard = 0
list = [answer_a,answer_b,answer_c,answer_d]
answer = 0
circle_answer_1 = 0
circle_answer_2 = 0
circle_answer_3 = 0

class Questions():

    def quest(self):
        global quest
        global answer_a
        global answer_b
        global answer_c
        global answer_d
        global answer_good
        global list
        global score
        global gameover
        global draw_easy
        global draw_medium
        global draw_hard
        global draw_remove_easy
        global draw_remove_medium
        global draw_remove_hard
        global gui_button
        global gui_button_a
        global gui_label
        global gui_button_b
        global gui_button_c
        global gui_button_d
        global gui_label
        draw_result_easy = random.choice(draw_easy)
        draw_remove_easy = draw_result_easy
        draw_result_medium = random.choice(draw_medium)
        draw_remove_medium = draw_result_medium
        draw_result_hard = random.choice(draw_hard)
        draw_remove_hard = draw_result_hard
        if score == 0 or score == 1 or score == 2 or score == 3:
            quest = draw_result_easy[0]
            answer_a = draw_result_easy[1]
            answer_b = draw_result_easy[2]
            answer_c = draw_result_easy[3]
            answer_d = draw_result_easy[4]
        elif score == 4 or score == 5 or score == 6 or score == 7:
            quest = draw_result_medium[0]
            answer_a = draw_result_medium[1]
            answer_b = draw_result_medium[2]
            answer_c = draw_result_medium[3]
            answer_d = draw_result_medium[4]
        elif score == 8 or score == 9 or score == 10 or score == 11:
            quest = draw_result_hard[0]
            answer_a = draw_result_hard[1]
            answer_b = draw_result_hard[2]
            answer_c = draw_result_hard[3]
            answer_d = draw_result_hard[4]

        gui_label.config(text=quest)

        gui_button_a.config(text=answer_a, command=answer.answer_click_A)

        gui_button_b.config(text=answer_b, command=answer.answer_click_B)

        gui_button_c.config(text=answer_c, command=answer.answer_click_C)

        gui_button_d.config(text=answer_d, command=answer.answer_click_D)

        if score == 0 or score == 1 or score == 2 or score == 3:
            if draw_result_easy == q1 or draw_result_easy == q5:
                answer_good = answer_a
                list = [answer_b, answer_c, answer_d]
            elif draw_result_easy == q2 or draw_result_easy == q6:
                answer_good = answer_b
                list = [answer_a, answer_c, answer_d]
            elif draw_result_easy == q3 or draw_result_easy == q7:
                answer_good = answer_c
                list = [answer_a, answer_b, answer_d]
            elif draw_result_easy == q4 or draw_result_easy == q8:
                answer_good = answer_d
                list = [answer_a, answer_b, answer_c]
        elif score == 4 or score == 5 or score == 6 or score == 7:
            if draw_result_medium == q9 or draw_result_medium == q13:
                answer_good = answer_a
            elif draw_result_medium == q10 or draw_result_medium == q14:
                answer_good = answer_b
            elif draw_result_medium == q11 or draw_result_medium == q15:
                answer_good = answer_c
            elif draw_result_medium == q12 or draw_result_medium == q16:
                answer_good = answer_d
        elif score == 8 or score == 9 or score == 10 or score == 11:
            if draw_result_hard == q17 or draw_result_hard == q21:
                answer_good = answer_a
            elif draw_result_hard == q18 or draw_result_hard == q22:
                answer_good = answer_b
            elif draw_result_hard == q19 or draw_result_hard == q23:
                answer_good = answer_c
            elif draw_result_hard == q20 or draw_result_hard == q24:
                answer_good = answer_d

class Answers():

    def answer_click_A(self):
        global answer_good

        global score
        global gameover

        if answer_good == answer_a:
            score += 1
        else:
            gameover += 1
        if gameover >= 1:
            game_over()
        if answer_good == answer_a:
            if score == 0 or score == 1 or score == 2 or score == 3:
                draw_easy.remove(draw_remove_easy)
            if score == 4 or score == 5 or score == 6 or score == 7:
                draw_medium.remove(draw_remove_medium)
            if score == 8 or score == 9 or score == 10 or score == 11:
                draw_hard.remove(draw_remove_hard)
        score_check()

    def answer_click_B(self):
        global score
        global gameover
        if answer_good == answer_b:
            score += 1
        else:
            gameover += 1
        if gameover >= 1:
            game_over()
        if answer_good == answer_b:
            if score == 0 or score == 1 or score == 2 or score == 3:
                draw_easy.remove(draw_remove_easy)
            if score == 4 or score == 5 or score == 6 or score == 7:
                draw_medium.remove(draw_remove_medium)
            if score == 8 or score == 9 or score == 10 or score == 11:
                draw_hard.remove(draw_remove_hard)
        score_check()

    def answer_click_C(self):
        global score
        global gameover
        if answer_good == answer_c:
            score += 1
        else:
            gameover += 1
        if gameover >= 1:
            game_over()
        if answer_good == answer_c:
            if score == 0 or score == 1 or score == 2 or score == 3:
                draw_easy.remove(draw_remove_easy)
            if score == 4 or score == 5 or score == 6 or score == 7:
                draw_medium.remove(draw_remove_medium)
            if score == 8 or score == 9 or score == 10 or score == 11:
                draw_hard.remove(draw_remove_hard)
        score_check()

    def answer_click_D(self):
        global score
        global gameover
        if answer_good == answer_d:
            score += 1
        else:
            gameover += 1
        if gameover >= 1:
            game_over()
        if answer_good == answer_d:
            if score == 0 or score == 1 or score == 2 or score == 3:
                draw_easy.remove(draw_remove_easy)
            if score == 4 or score == 5 or score == 6 or score == 7:
                draw_medium.remove(draw_remove_medium)
            if score == 8 or score == 9 or score == 10 or score == 11:
                draw_hard.remove(draw_remove_hard)
        score_check()

class Circles():

    def help_circles_5050():
        global answer_a
        global answer_b
        global answer_c
        global answer_d
        global answer_good
        global list
        global circle_1
        global circle_answer_1
        if circle_1 == 0:
            help = random.choice(list)
            list2 = [answer_good, help]
            help2 = random.sample(list2, 2)
            circle_answer_1 = help2
            gui_label_circle_1.config(text='Lifebuoy 50/50:     One of these answers is good:    ' + str(circle_answer_1))
            circle_1 += 1
        else:
            gui_label_circle_1.config(text='Lifebuoy 50/50:     You have not this lifebuoy')

    def help_circles_phone():
        global answer_a
        global answer_b
        global answer_c
        global answer_d
        global answer_good
        global list
        global circle_2
        global circle_answer_2
        list2 = [1,2,3]
        if circle_2 == 0:
            result = random.choice(list2)
            if result == 1:
                help = random.choice(list)
                list2 = [answer_good, help]
                help2 = random.sample(list2, 2)
                circle_answer_2 = help2
                gui_label_circle_2.config(text='Lifebuoy phone to friend:     Your friend is certainly that good answer is:     ' + str(circle_answer_2))
            elif result == 2:
                circle_answer_2 = answer_good
                gui_label_circle_2.config(text= 'Lifebuoy phone to friend:     Your friend thinks that one of these answers is good:     ' + str(circle_answer_2))
            elif result == 3:
                gui_label_circle_2.config(text='Lifebuoy phone to friend:     Your friend do not to know good answer!')
            circle_2 += 1
        else:
            gui_label_circle_2.config(text='Lifebuoy phone to friend:     You have not this lifebuoy!')

    def help_circles_audience():
        global answer_good
        global circle_3
        global circle_answer_3
        a = 0
        b = 0
        c = 0
        d = 0
        precent = 100
        if circle_3 == 0:
            if answer_good == answer_a:
                a += 30
                precent -= 30
            if answer_good == answer_b:
                b += 30
                precent -= 30
            if answer_good == answer_c:
                c += 30
                precent -= 30
            if answer_good == answer_d:
                d += 30
                precent -= 30
            p1 = random.randint(0,precent)
            a += p1
            precent -= p1
            p2 = random.randint(0,precent)
            b += p2
            precent -= p2
            p3 = random.randint(0,precent)
            c += p3
            precent -= p3
            p4 = precent
            d += p4
            gui_label_circle_3.config(text='Lifebuoy help of audience:     Result vote audience: ' + '    a - ' + str(a) + '%    ' + '    b -' + str(b) + '%    ' '    c -' + str(c) + '%    ' '    d -' + str(d) + '%    ')
            circle_3 += 1
        else:
            gui_label_circle_3.config(text='Lifebuoy help of audience:     You have not this lifebuoy!')

def score_check():
    global early_end
    global current_cash
    global exit_cash
    if score == 1:
        current_cash = 500
        game_end = messagebox.askyesno(title='Good Answer!', message='Good answer! Do you want to play next? You current win is: ' + str(current_cash) + ' euro!')
        gui_label_current_cash.config(text='You current win: ' + str(current_cash) + ' euro')
        if game_end == 1:
            question_2()
        elif game_end == 0:
            game_end_yes = messagebox._show(title='Thank you!',message='Thank you! You win: ' + str(current_cash) + ' euro!')
            sys.exit()

    if score == 2:
        current_cash = 1000
        exit_cash = 1000
        game_end = messagebox._show(title='Good Answer!', message='You have guaranteed: ' + str(current_cash) + ' euro! You can safely answer on next question!')
        gui_label_current_cash.config(text='You current win is: ' + str(current_cash) + ' euro!')
        gui_label_exit_cash.config(text='You have guaranteed: ' + str(exit_cash) + ' euro!')
        question_3()

    if score == 3:
        current_cash = 2000
        exit_cash = 1000
        game_end = messagebox.askyesno(title='Good Answer!', message='Do you want to play next? You current win is: ' + str(current_cash) + ' euro!')
        gui_label_current_cash.config(text='You current win is: ' + str(current_cash) + ' euro!')
        if game_end == 1:
            question_4()
        elif game_end == 0:
            game_end_yes = messagebox._show(title='Thank you!',message='Thank you! You win: ' + str(current_cash) + ' euro!')
            sys.exit()

    if score == 4:
        current_cash = 5000
        game_end = messagebox.askyesno(title='Good Answer!', message='Good Answer! Do you want to play next? You current win is: ' + str(current_cash) + ' euro!')
        gui_label_current_cash.config(text='You current win is: ' + str(current_cash) + ' euro!')
        if game_end == 1:
            question_5()
        elif game_end == 0:
            game_end_yes = messagebox._show(title='Thank you!',message='Thank you! You win: ' + str(current_cash) + ' euro!')
            sys.exit()

    if score == 5:
        current_cash = 10000
        game_end = messagebox.askyesno(title='Good Answer!', message='Good Answer! Do you want to play next? You current win is: ' + str(current_cash) + ' euro!')
        gui_label_current_cash.config(text='You current win is: ' + str(current_cash) + ' euro!')
        if game_end == 1:
            question_6()
        elif game_end == 0:
            game_end_yes = messagebox._show(title='Thank you!',message='Thank you! You win: ' + str(current_cash) + ' euro!')
            sys.exit()

    if score == 6:
        current_cash = 20000
        game_end = messagebox.askyesno(title='Good Answer!', message='Good Answer! Do you want to play next? You current win is: ' + str(current_cash) + ' euro!')
        gui_label_current_cash.config(text='You current win is: ' + str(current_cash) + ' euro!')
        if game_end == 1:
            question_7()
        elif game_end == 0:
            game_end_yes = messagebox._show(title='Thank you!',message='Thank you! You win: ' + str(current_cash) + ' euro!')
            sys.exit()

    if score == 7:
        current_cash = 40000
        exit_cash = 40000
        game_end = messagebox._show(title='Good Answer!', message='Good Answer! You have guaranteed: ' + str(current_cash) + ' euro. You can safely answer on next question!')
        gui_label_current_cash.config(text='You current win is: ' + str(current_cash) + ' euro!')
        gui_label_exit_cash.config(text='You have guaranteed: ' + str(exit_cash) + ' euro!')
        question_8()

    if score == 8:
        current_cash = 75000
        game_end = messagebox.askyesno(title='Good Answer!', message='Good Answer! Do you want to play next? You current win is: ' + str(current_cash) + ' euro!')
        gui_label_current_cash.config(text='You current win is: ' + str(current_cash) + ' euro!')
        if game_end == 1:
            question_9()
        elif game_end == 0:
            game_end_yes = messagebox._show(title='Thank you!',message='Thank you! You win: ' + str(current_cash) + ' euro!')
            sys.exit()

    if score == 9:
        current_cash = 125000
        game_end = messagebox.askyesno(title='Good Answer!', message='Good Answer! Do you want to play next? You current win is: ' + str(current_cash) + ' euro!')
        gui_label_current_cash.config(text='You current win is: ' + str(current_cash) + ' euro!')
        if game_end == 1:
            question_10()
        elif game_end == 0:
            game_end_yes = messagebox._show(title='Thank you!',message='Thank you! You win: ' + str(current_cash) + ' euro!')
            sys.exit()

    if score == 10:
        current_cash = 250000
        game_end = messagebox.askyesno(title='Good Answer!', message='Good Answer! Do you want to play next? You current win is: ' + str(current_cash) + ' euro!')
        gui_label_current_cash.config(text='You current win is: ' + str(current_cash) + ' euro!')
        if game_end == 1:
            question_11()
        elif game_end == 0:
            game_end_yes = messagebox._show(title='Thank you!',message='Thank you! You win: ' + str(current_cash) + ' euro!')
            sys.exit()

    if score == 11:
        current_cash = 500000
        game_end = messagebox.askyesno(title='Good Answer!', message='Good Answer! Do you want to play next? You current win is: ' + str(current_cash) + ' euro!')
        gui_label_current_cash.config(text='You current win is: ' + str(current_cash) + ' euro!')
        if game_end == 1:
            question_12()
        elif game_end == 0:
            game_end_yes = messagebox._show(title='Thank you!',message='Thank you! You win: ' + str(current_cash) + ' euro!')
            sys.exit()

    if score == 12:
        exit_cash = 1000000
        game_end = messagebox.askyesno(title='You win!!', message='You win! Congratulations! You win 100.000.000 euro!')
        gui_label_current_cash.config(text='You current win is: ' + str(current_cash) + ' euro!')
        if game_end == 1:
            sys.exit()

def game_over():
    exit_game = messagebox._show(title='Bad answer!', message='You lose! You win is ' + str(exit_cash) + ' euro!')
    sys.exit()

quest1 = Questions()
quest2 = Questions()
quest3 = Questions()
quest4 = Questions()
quest5 = Questions()
quest6 = Questions()
quest7 = Questions()
quest8 = Questions()
quest9 = Questions()
quest10 = Questions()
quest11 = Questions()
quest12 = Questions()
answer = Answers()

def question_1():
    gui_label_quest_number.config(text='Question number 1 for 500 euro')
    quest1.quest()

def question_2():
    gui_label_quest_number.config(text='Question number 2 for 1000 euro')
    if circle_1 > 0:
        gui_label_circle_1.config(text='Lifebuoy 50/50:     You have not this lifebuoy!')
    if circle_2 > 0:
        gui_label_circle_2.config(text='Lifebuoy phone to friend:     You have not this lifebuoy!')
    if circle_3 > 0:
        gui_label_circle_3.config(text='Lifebuoy help of audience:     You have not this lifebuoy!')
    quest2.quest()

def question_3():
    gui_label_quest_number.config(text='Question number 3 for 2000 euro')
    if circle_1 > 0:
        gui_label_circle_1.config(text='Lifebuoy 50/50:     You have not this lifebuoy!')
    if circle_2 > 0:
        gui_label_circle_2.config(text='Lifebuoy phone to friend:     You have not this lifebuoy!')
    if circle_3 > 0:
        gui_label_circle_3.config(text='Lifebuoy help of audience:     You have not this lifebuoy!')
    quest3.quest()

def question_4():
    gui_label_quest_number.config(text='Question number 4 for 5000 euro')
    if circle_1 > 0:
        gui_label_circle_1.config(text='Lifebuoy 50/50:     You have not this lifebuoy!')
    if circle_2 > 0:
        gui_label_circle_2.config(text='Lifebuoy phone to friend:     You have not this lifebuoy!')
    if circle_3 > 0:
        gui_label_circle_3.config(text='Lifebuoy help of audience:     You have not this lifebuoy!')
    quest4.quest()

def question_5():
    gui_label_quest_number.config(text='Question number 5 for 10.000 euro')
    if circle_1 > 0:
        gui_label_circle_1.config(text='Lifebuoy 50/50:     You have not this lifebuoy!')
    if circle_2 > 0:
        gui_label_circle_2.config(text='Lifebuoy phone to friend:     You have not this lifebuoy!')
    if circle_3 > 0:
        gui_label_circle_3.config(text='Lifebuoy help of audience:     You have not this lifebuoy!')
    quest5.quest()

def question_6():
    gui_label_quest_number.config(text='Question number 6 for 20.000 euro')
    if circle_1 > 0:
        gui_label_circle_1.config(text='Lifebuoy 50/50:     You have not this lifebuoy!')
    if circle_2 > 0:
        gui_label_circle_2.config(text='Lifebuoy phone to friend:     You have not this lifebuoy!')
    if circle_3 > 0:
        gui_label_circle_3.config(text='Lifebuoy help of audience:     You have not this lifebuoy!')
    quest6.quest()

def question_7():
    gui_label_quest_number.config(text='Question number 7 for 40.000 euro')
    if circle_1 > 0:
        gui_label_circle_1.config(text='Lifebuoy 50/50:     You have not this lifebuoy!')
    if circle_2 > 0:
        gui_label_circle_2.config(text='Lifebuoy phone to friend:     You have not this lifebuoy!')
    if circle_3 > 0:
        gui_label_circle_3.config(text='Lifebuoy help of audience:     You have not this lifebuoy!')
    quest7.quest()

def question_8():
    gui_label_quest_number.config(text='Question number 8 for 75.000 euro')
    if circle_1 > 0:
        gui_label_circle_1.config(text='Lifebuoy 50/50:     You have not this lifebuoy!')
    if circle_2 > 0:
        gui_label_circle_2.config(text='Lifebuoy phone to friend:     You have not this lifebuoy!')
    if circle_3 > 0:
        gui_label_circle_3.config(text='Lifebuoy help of audience:     You have not this lifebuoy!')
    quest8.quest()

def question_9():
    gui_label_quest_number.config(text='Question number 9 for 125.000 euro')
    if circle_1 > 0:
        gui_label_circle_1.config(text='Lifebuoy 50/50:     You have not this lifebuoy!')
    if circle_2 > 0:
        gui_label_circle_2.config(text='Lifebuoy phone to friend:     You have not this lifebuoy!')
    if circle_3 > 0:
        gui_label_circle_3.config(text='Lifebuoy help of audience:     You have not this lifebuoy!')
    quest9.quest()

def question_10():
    gui_label_quest_number.config(text='Question number 10 for 250.000 euro')
    if circle_1 > 0:
        gui_label_circle_1.config(text='Lifebuoy 50/50:     You have not this lifebuoy!')
    if circle_2 > 0:
        gui_label_circle_2.config(text='Lifebuoy phone to friend:     You have not this lifebuoy!')
    if circle_3 > 0:
        gui_label_circle_3.config(text='Lifebuoy help of audience:     You have not this lifebuoy!')
    quest10.quest()

def question_11():
    gui_label_quest_number.config(text='Question number 11 for 500.000 euro')
    if circle_1 > 0:
        gui_label_circle_1.config(text='Lifebuoy 50/50:     You have not this lifebuoy!')
    if circle_2 > 0:
        gui_label_circle_2.config(text='Lifebuoy phone to friend:     You have not this lifebuoy!')
    if circle_3 > 0:
        gui_label_circle_3.config(text='Lifebuoy help of audience:     You have not this lifebuoy!')
    quest11.quest()

def question_12():
    gui_label_quest_number.config(text='Question number 12 for 100.000.000 euro')
    if circle_1 > 0:
        gui_label_circle_1.config(text='Lifebuoy 50/50:     You have not this lifebuoy!')
    if circle_2 > 0:
        gui_label_circle_2.config(text='Lifebuoy phone to friend:     You have not this lifebuoy!')
    if circle_3 > 0:
        gui_label_circle_3.config(text='Lifebuoy help of audience:     You have not this lifebuoy!')
    quest12.quest()

gui_label_current_cash = tkinter.Label(gui, text='GET 1 MILLION EUROS!')
gui_label_current_cash.place(y=10, x=390)

gui_label_current_cash = tkinter.Label(gui, text='You current win is: ' + str(current_cash) + ' euro')
gui_label_current_cash.place(y=60, x=160)

gui_label_exit_cash = tkinter.Label(gui, text='You guaranteed win is: ' + str(exit_cash) + ' euro')
gui_label_exit_cash.place(y=60, x=470)

gui_label_quest_number = tkinter.Label(gui, text='Question:')
gui_label_quest_number.place(y=110, x=90)
gui_label = tkinter.Label(gui, text=quest)
gui_label.place(y=130, x=90)

gui_button_a = tkinter.Button(gui, text=answer_a, command=answer.answer_click_A, height = 1, width = 50)
gui_button_a.place(x=70, y=180)

gui_button_b = tkinter.Button(gui, text=answer_b, command=answer.answer_click_B, height = 1, width = 50)
gui_button_b.place(x=470, y=180)

gui_button_c = tkinter.Button(gui, text=answer_c, command=answer.answer_click_C, height = 1, width = 50)
gui_button_c.place(x=70, y=230)

gui_button_d = tkinter.Button(gui, text=answer_d, command=answer.answer_click_D, height = 1, width = 50)
gui_button_d.place(x=470, y=230)

gui_label_circle_1 = tkinter.Label(gui, text='Lifebuoy 50/50:     ' + str(circle_answer_1))
gui_label_circle_1.place(y=300, x=10)

gui_label_circle_2 = tkinter.Label(gui, text='Lifebuoy help of audience:     ' + str(circle_answer_2))
gui_label_circle_2.place(y=330, x=10)

gui_label_circle_3 = tkinter.Label(gui, text='Lifebuoy phone to friend:     ' + str(circle_answer_3))
gui_label_circle_3.place(y=360, x=10)

gui_circle5050 = tkinter.Button(gui, text='Lifebuoy 50/50:', command=Circles.help_circles_5050, height = 1, width = 40)
gui_circle5050.place(x=10, y=400)

gui_circle_audience = tkinter.Button(gui, text='Lifebuoy help of audience', command=Circles.help_circles_audience, height = 1, width = 40)
gui_circle_audience.place(x=310, y=400)

gui_circle_phone = tkinter.Button(gui, text='Lifebuoy phone to friend', command=Circles.help_circles_phone, height = 1, width = 40)
gui_circle_phone.place(x=610, y=400)

game_start = tkinter.messagebox.askyesno(title = 'GET 1 MILLION EUROS!', message = 'Do you want to play about 1 million euro?')
if game_start == 1:
    question_1()
else:
    sys.exit()

gui.mainloop()
