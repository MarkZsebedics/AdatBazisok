import tkinter as tk
from tkinter import messagebox as MessageBox
from tkinter import *
from tkinter import font as font
import mysql.connector as mysql
from PIL import ImageTk, Image

import database_init

#Adatbazis letrehozasa es feltoltese ha meg nincs, kulonben sql error, amit ignoralva megy tovabb
try:
    database_init.createDatabase()
except:
    print('mar letre van hozva az adatbazis')
try:
    database_init.recordUpload()
    database_init.recordUploadSmarter()
except:
    print('mar fel van toltve adatokkal')

#Bekeri egy Jatekos nevet, es Kiirja az osszes bajnoksagot amiben szerepelt, es hogy hanyadik helyet ert el
def player_tournaments():
    #ures inputra hibat dob
    if e_playerInTournaments.get() == "":
        MessageBox.showinfo("info", 'Player mezo kotelezo')
    else:
        #nemures inputra futtatja a lekerdezest a megadott stringre
        con = mysql.connect(host=dbhost, user=dbuser, database=dbname)
        cursor = con.cursor()
        pName = e_playerInTournaments.get()
        #lekeri annak a jatekosnak az adatait, akinek a neve megegyezik az input Stringgel
        cursor.execute(f'select * from player where name = "{pName}"')
        jnev = cursor.fetchall()
        #lekeri a jatekos bajnoksagokban elert eredmenyeit
        cursor.execute(f'Select Placement, tname from participate  where pName ="{pName}" ;')
        adatok = cursor.fetchall()
        #lekeri a Participate tabla oszlopneveit, hogy kiIrassuk a kepernyore
        cursor.execute(
            f'SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`="chess" AND `TABLE_NAME`="participate"; ')
        columns = cursor.fetchall()
        del columns[2]
        #Ha ures a jatekos nevere szolo lekerdezes akkor nincs benne az adatbazisban olyan nev
        #mint a pontos String
        if jnev == []:
            queryList.delete(0, queryList.size())
            queryList.insert(queryList.size() + 1, f'Nincs ilyen nevu jatekos az adatbazisban!')
        #amennyiben volt ilyen jatekos, de ures a jatekos nevevel valo lekerdezes amiben a bajnoksagokat
        #kertuk akkor egy bajnoksagban sem szerepelt
        elif adatok == []:
            queryList.delete(0, queryList.size())
            queryList.insert(queryList.size() + 1, f'Ez a jatekos nem nevezett\n egy bajnoksagra sem')
        #Kulonben pedig kiiratjuk egy tablaba a jatekos bajnoksagait
        else:
            #A queryList egy olyan objektum amivel a belerakott szovege megjelennek egy tablazat szeru
            #grafikus feluleten. Az UI-n egy helyen tobb lekerdezes eredmenye is ott lehet, igy eloszor
            #toroljuk a benne levo szoveget, aztan feltoltjuk az ujjal
            rows = adatok
            queryList.delete(0, queryList.size())
            queryList.insert(queryList.size() + 1, columns)
            for row in rows:
                insertData = '{} {}'.format(row[0], row[1])
                queryList.insert(queryList.size() + 1, insertData)
        e_playerInTournaments.delete(0, 'end')
        con.close()

#Ki listazza egy bajnoksag vegeredmenyet
def tournament_result():
    #ures inputra hibat dob
    if e_tournamentResult.get() == "":
        MessageBox.showinfo("info", 'Result mezo kotelezo')
    else:
        #nemures inputra futtatja a lekerdezest a megadott stringre
        con = mysql.connect(host=dbhost, user=dbuser, database=dbname)
        cursor = con.cursor()
        tName = e_tournamentResult.get()
        cursor.execute(f'Select pName,Placement from participate where tName ="{tName}" order by placement asc;')
        adatok = cursor.fetchall()
        cursor.execute(
            f'select `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`="chess" AND `TABLE_NAME`="participate"; ')
        columns = cursor.fetchall()
        del columns[1]
        csere = columns[0]
        columns[0] = columns[1]
        columns[1] = csere
        if adatok == []:
            queryList.delete(0, queryList.size())
            queryList.insert(queryList.size() + 1, 'Nem talalhato ilyen nevu bajnoksag')
        else:
            rows = adatok
            queryList.delete(0, queryList.size())
            queryList.insert(queryList.size() + 1, columns)
            for row in rows:
                insertData = '{} {}'.format(row[0], row[1])
                queryList.insert(queryList.size() + 1, insertData)
        e_tournamentResult.delete(0, 'end')
        con.close()

#Kiirja hogy melyik jatekos hany gyozelemmel rendelkezik, csokkeno sorrendben
def gamesWon():
    con = mysql.connect(host=dbhost, user=dbuser, database=dbname)
    cursor = con.cursor()
    cursor.execute(
        'select name, count(winner) as "gyozelmek szama" from player left join game on player.name=game.winner group by name order by count(winner) desc;')
    adatok = cursor.fetchall()
    columns = ['Nev','Gyozelmek']
    if adatok == []:
        queryList.delete(0, queryList.size())
        queryList.insert(queryList.size() + 1, 'Nem talalhato ilyen nevu bajnoksag')
    else:
        rows = adatok
        queryList.delete(0, queryList.size())
        queryList.insert(queryList.size() + 1, columns)
        for row in rows:
            insertData = '{} {}'.format(row[0], row[1])
            queryList.insert(queryList.size() + 1, insertData)
    con.close()

#Kiirja orszagonkent hanyan neveztek FIDE bajnoksagokra
def nationsOfFIDE():
    con = mysql.connect(host=dbhost, user=dbuser, database=dbname)
    cursor = con.cursor()
    cursor.execute(
        'select nationality, count(nationality) as "participants" from player left join participate on name =pname where tname like "%FIDE%" group by nationality order by count(nationality) desc;')
    adatok = cursor.fetchall()
    columns = ['Orszag', 'Nevezesek_szama']
    if adatok == []:
        queryList.delete(0, queryList.size())
        queryList.insert(queryList.size() + 1, 'Nem talalhato ilyen nevu bajnoksag')
    else:
        rows = adatok
        queryList.delete(0, queryList.size())
        queryList.insert(queryList.size() + 1, columns)
        for row in rows:
            insertData = '{} {}'.format(row[0], row[1])
            queryList.insert(queryList.size() + 1, insertData)
    con.close()

#Kiirja azokat a jatekosokat akik nyertek bajnoksagot
def champions():
    con = mysql.connect(host=dbhost, user=dbuser, database=dbname)
    cursor = con.cursor()
    cursor.execute('select * from player where name in(select pName from participate where placement =1);')
    adatok = cursor.fetchall()
    cursor.execute(
        f'SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`="chess" AND `TABLE_NAME`="player"; ')
    columns = cursor.fetchall()

    if adatok == []:
        queryList.delete(0, queryList.size())
        queryList.insert(queryList.size() + 1, 'Nem talalhato ilyen nevu bajnoksag')
    else:
        rows = adatok
        queryList.delete(0, queryList.size())
        queryList.insert(queryList.size() + 1, columns)
        for row in rows:
            insertData = '{} {} {} {}'.format(row[0], row[1], row[2], row[3])
            queryList.insert(queryList.size() + 1, insertData)
    con.close()

#Lekeri a kert nevu jatekos minden adatat
def player_get():
    if e_name.get() == "":
        MessageBox.showinfo("info", 'Nev mezo kotelezo')
    else:
        con = mysql.connect(host=dbhost, user=dbuser, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from Player where name="{}"'.format(e_name.get()))
        rows = cursor.fetchmany(4)
        e_birth.delete(0, 'end')
        e_nation.delete(0, 'end')
        e_rank.delete(0, 'end')
        for row in rows:
            e_birth.insert(0, row[1])
            e_nation.insert(0, row[2])
            e_rank.insert(0, row[3])
        con.close()

#Lekeri a kert nevu bajnoksag minden adatat
def tournament_get():
    if e_tName.get() == "":
        MessageBox.showinfo("info", 'Nev mezo kotelezo')
    else:
        con = mysql.connect(host=dbhost, user=dbuser, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from Tournament where name="{}"'.format(e_tName.get()))
        rows = cursor.fetchmany(4)
        e_start.delete(0, 'end')
        e_end.delete(0, 'end')
        e_place.delete(0, 'end')
        e_reward.delete(0, 'end')
        for row in rows:
            e_start.insert(0, row[1])
            e_end.insert(0, row[2])
            e_place.insert(0, row[3])
            e_reward.insert(0, row[4])
        con.close()

#Beszur egy uj jatekost a megadott adatokkal
def player_insert():
    if e_name.get() == "" or e_birth.get() == "" or e_nation.get() == "" or e_rank.get() == "":
        MessageBox.showinfo('info', 'minden mezo kitoltese kotelezo')
    else:
        con = mysql.connect(host=dbhost, user=dbuser, database=dbname)
        cursor = con.cursor()
        cursor.execute(
            'insert into player values("{}","{}","{}","{}")'.format(e_name.get(), e_birth.get(), e_nation.get(),
                                                                    e_rank.get()))
        cursor.execute('commit')
        e_name.delete(0, 'end')
        e_birth.delete(0, 'end')
        e_nation.delete(0, 'end')
        e_rank.delete(0, 'end')
        MessageBox.showinfo('Info', 'sikeres beszuras!')
        display_selected(variable.get())
        con.close()

#Beszur egy uj bajnoksagot a megadott adatokkal
def tournament_insert():
    if e_tName.get() == "" or e_start.get() == "" or e_end.get() == "" or e_place.get() == "" or e_reward.get() == "":
        MessageBox.showinfo('info', 'minden mezo kitoltese kotelezo')
    else:
        con = mysql.connect(host=dbhost, user=dbuser, database=dbname)
        cursor = con.cursor()
        cursor.execute(
            'insert into tournament values("{}","{}","{}","{}", "{}")'.format(e_tName.get(), e_start.get(), e_end.get(),
                                                                              e_place.get(), e_reward.get()))
        cursor.execute('commit')
        e_tName.delete(0, 'end')
        e_start.delete(0, 'end')
        e_end.delete(0, 'end')
        e_place.delete(0, 'end')
        e_reward.delete(0, 'end')
        MessageBox.showinfo('Info', 'sikeres beszuras!')
        display_selected(variable.get())
        con.close()

#Kitorli a megadott nevu jatekost az adatbazisbol
def player_delete():
    if e_name.get() == "":
        MessageBox.showinfo('info', 'minden mezo kitoltese kotelezo')
    else:
        con = mysql.connect(host=dbhost, user=dbuser, database=dbname)
        cursor = con.cursor()
        cursor.execute('delete from player where name="{}"'.format(e_name.get()))
        cursor.execute('commit')
        e_name.delete(0, 'end')
        e_birth.delete(0, 'end')
        e_nation.delete(0, 'end')
        e_rank.delete(0, 'end')
        MessageBox.showinfo('Info', 'Torles vegrehajtva')
        display_selected(variable.get())
        con.close()

#Kitorli a megadott nevu bajnoksagot az adatbazisbol
def tournament_delete():
    if e_tName.get() == "":
        MessageBox.showinfo('info', 'minden mezo kitoltese kotelezo')
    else:
        con = mysql.connect(host=dbhost, user=dbuser, database=dbname)
        cursor = con.cursor()
        cursor.execute('delete from tournament where name="{}"'.format(e_tName.get()))
        cursor.execute('commit')
        e_tName.delete(0, 'end')
        e_start.delete(0, 'end')
        e_end.delete(0, 'end')
        e_place.delete(0, 'end')
        e_reward.delete(0, 'end')
        MessageBox.showinfo('Info', 'Torles vegrehajtva')
        display_selected(variable.get())
        con.close()

#Frissiti a megadott nevu jatekos adatait
def player_update():
    if e_name.get() == "":
        MessageBox.showinfo('info', 'minden mezo kitoltese kotelezo')
    else:
        con = mysql.connect(host=dbhost, user=dbuser, database=dbname)
        cursor = con.cursor()
        cursor.execute('update player set name="{}",birthDate="{}", nationality="{}", mmr="{}" where name="{}"'.format(
            e_name.get(), e_birth.get(), e_nation.get(), e_rank.get(), e_name.get()))
        cursor.execute('commit')
        e_name.delete(0, 'end')
        e_birth.delete(0, 'end')
        e_nation.delete(0, 'end')
        e_rank.delete(0, 'end')
        MessageBox.showinfo('Info', 'Frissites vegrehajtva')
        display_selected(variable.get())
        con.close()

#Frissiti a megadott nevu bajnoksag adatait
def tournament_update():
    if e_tName.get() == "" or e_start.get() == "" or e_end.get() == "" or e_place.get() == "" or e_reward.get() == "":
        MessageBox.showinfo('info', 'minden mezo kitoltese kotelezo')
    else:
        con = mysql.connect(host=dbhost, user=dbuser, database=dbname)
        cursor = con.cursor()
        cursor.execute(
            'update tournament set name="{}",startTime="{}", endTime="{}", Place="{}", Prize={} where name="{}"'.format(
                e_tName.get(), e_start.get(), e_end.get(), e_place.get(), e_reward.get(), e_tName.get()))
        cursor.execute('commit')
        e_tName.delete(0, 'end')
        e_start.delete(0, 'end')
        e_end.delete(0, 'end')
        e_place.delete(0, 'end')
        e_reward.delete(0, 'end')
        MessageBox.showinfo('Info', 'Frissites vegrehajtva')
        display_selected(variable.get())
        con.close()

#lenyilo lista amiben kivalaszthatjuk melyik tablaban szereplo adatokat listazzuk ki
def listByChoice(table):
    con = mysql.connect(host=dbhost, user=dbuser, database=dbname)
    cursor = con.cursor()
    cursor.execute(f'select * from {table}')
    rows = cursor.fetchall()
    choiceLST.delete(0, choiceLST.size())
    cursor.execute(
        f'SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`="chess" AND `TABLE_NAME`="{table}"; ')
    columns = cursor.fetchall()
    choiceLST.insert(choiceLST.size() + 1, columns)
    # try-ok egymasba agyazva, mert a kulonbozo adattablak kulonbozo mennyisegu oszloppal rendelkeznek
    #Eleg szofisztikalatlan megoldas, de "It just works"
    for row in rows:  
        try:
            insertData = '{} {} {} {} {}'.format(row[0], row[1], row[2], row[3], row[4])
            choiceLST.insert(choiceLST.size() + 1, insertData)
        except(Exception):
            try:
                insertData = '{} {} {} {}'.format(row[0], row[1], row[2], row[3])
                choiceLST.insert(choiceLST.size() + 1, insertData)
            except(Exception):
                try:
                    insertData = '{} {} {}'.format(row[0], row[1], row[2])
                    choiceLST.insert(choiceLST.size() + 1, insertData)
                except(Exception):
                    pass

# lenyilo valasztasi lehetoseg az adattablak kilistazasara
def display_selected(choice=None):  
    if choice == None:
        choiceLST.delete(0, choiceLST.size())
    else:
        choice = variable.get()
        listByChoice(choice)

#A xampos adatbazishoz valo csatlakozas, valtozhatnak az ertekek
if __name__ == '__main__':
    dbhost = 'localhost'
    dbuser = 'root'
    dbpass = 'test123'
    dbname = 'chess'

    #Main window
    root = tk.Tk()
    root.geometry("1425x698")
    root.title("Best Chess Stats")

    #Hatter
    img = ImageTk.PhotoImage(Image.open('chess_bg.jpg'))
    panel = tk.Label(root, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")


    myFont = font.Font(family='Verdana', size=10)

    #rengeteg UI element, textboxok, nyomhato gombok, es szovegek
    name = tk.Label(root, text='Nev', font=myFont)
    name.place(x=40, y=100)

    birth = tk.Label(root, text='Szuldatum', font=myFont)
    birth.place(x=40, y=140)

    nation = tk.Label(root, text='Szarmazas', font=myFont)
    nation.place(x=40, y=180)

    rank = tk.Label(root, text='MMR', font=myFont)
    rank.place(x=40, y=220)

    tournament_result_label = tk.Label(root, text='Bajnoksag neve', font=myFont)
    tournament_result_label.place(x=750, y=100)

    player_tournaments_label = tk.Label(root, text='Jatekos Neve', font=myFont)
    player_tournaments_label.place(x=750, y=140)

    tname = tk.Label(root, text='Nev', font=myFont)
    tname.place(x=40, y=440)

    tstart = tk.Label(root, text='Kezdesi Datum', font=myFont)
    tstart.place(x=40, y=480)

    tend = tk.Label(root, text='Befejezesi datum', font=myFont)
    tend.place(x=40, y=520)

    tplace = tk.Label(root, text='Helyszin', font=myFont)
    tplace.place(x=40, y=560)

    treward = tk.Label(root, text='Ossznyeremeny', font=myFont)
    treward.place(x=40, y=600)

    e_name = tk.Entry()
    e_name.place(x=170, y=100)

    e_birth = tk.Entry()
    e_birth.place(x=170, y=140)

    e_nation = tk.Entry()
    e_nation.place(x=170, y=180)

    e_rank = tk.Entry()
    e_rank.place(x=170, y=220)

    e_tName = tk.Entry()
    e_tName.place(x=170, y=440)

    e_start = tk.Entry()
    e_start.place(x=170, y=480)

    e_end = tk.Entry()
    e_end.place(x=170, y=520)

    e_place = tk.Entry()
    e_place.place(x=170, y=560)

    e_reward = tk.Entry()
    e_reward.place(x=170, y=600)

    e_tournamentResult = tk.Entry()
    e_tournamentResult.place(x=880, y=100)

    e_playerInTournaments = tk.Entry()
    e_playerInTournaments.place(x=880, y=140)

    insert_button = tk.Button(root, text="Beszur", bg="green", command=player_insert, font=myFont)
    insert_button.place(x=40, y=250)

    update_button = tk.Button(root, text="Frissit", bg="green", command=player_update, font=myFont)
    update_button.place(x=110, y=250)

    delete_button = tk.Button(root, text="Torol", bg="green", command=player_delete, font=myFont)
    delete_button.place(x=180, y=250)

    get_button = tk.Button(root, text="Leker", bg="green", command=player_get, font=myFont)
    get_button.place(x=250, y=250)

    Tinsert_button = tk.Button(root, text="Beszur", bg="green", command=tournament_insert, font=myFont)
    Tinsert_button.place(x=40, y=640)

    Tupdate_button = tk.Button(root, text="Frissit", bg="green", command=tournament_update, font=myFont)
    Tupdate_button.place(x=110, y=640)

    Tdelete_button = tk.Button(root, text="Torol", bg="green", command=tournament_delete, font=myFont)
    Tdelete_button.place(x=180, y=640)

    Tget_button = tk.Button(root, text="Leker", bg="green", command=tournament_get, font=myFont)
    Tget_button.place(x=250, y=640)

    result_button = tk.Button(root, text="Bajnoksag vegallasa", bg="green", command=tournament_result, font=myFont)
    result_button.place(x=1040, y=100)

    pTournaments_button = tk.Button(root, text="Jatekos bajnoksagokban", bg="green", command=player_tournaments,
                                    font=myFont)
    pTournaments_button.place(x=1040, y=140)

    gamesWon_button = tk.Button(root, text="Meccs gyozelmek listaja", bg="green", command=gamesWon, font=myFont)
    gamesWon_button.place(x=1040, y=200)

    nationsOfFideButton = tk.Button(root, text="Nemzet szerinti lista, a FIDE bajnoksagain belul", bg="green",
                                    command=nationsOfFIDE, font=myFont)
    nationsOfFideButton.place(x=1040, y=260)

    champsButton = tk.Button(root, text="Bajnokok kilistazasa", bg="green", command=champions, font=myFont)
    champsButton.place(x=1040, y=320)

    choiceLST = tk.Listbox(root, width=70)
    choiceLST.config(font=myFont)
    choiceLST.place(x=750, y=470)

    queryList = tk.Listbox(root, width=35)
    queryList.config(font=myFont)
    queryList.place(x=750, y=200)

    tables = ['Player', 'Game', 'Participate', 'Tournament']
    variable = StringVar()
    variable.set(tables[3])
    dropdown = OptionMenu(
        root,
        variable,
        *tables,
        command=display_selected
    )

    dropdown.config(bg='green')
    dropdown.place(x=750, y=440)

    root.mainloop()
