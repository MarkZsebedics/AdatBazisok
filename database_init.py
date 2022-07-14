import mysql.connector as mysql


def createDatabase():
    #a csatlakozashoz szuksegesvaltozok beallitasa
    dbhost = 'localhost'
    dbuser = 'root'
    con = mysql.connect(host=dbhost, user=dbuser)
    cursor = con.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS CHESS ;')
    cursor.execute('USE CHESS;')
    cursor.execute('CREATE TABLE IF NOT EXISTS Player (Name VARCHAR(40) not Null PRIMARY KEY, Birthdate DATE DEFAULT NULL, Nationality VARCHAR(30) DEFAULT NULL, MMR INT(3));')
    cursor.execute('CREATE TABLE IF NOT EXISTS Tournament (Name VARCHAR(50) not Null  PRIMARY KEY,startTime DATE, EndTime DATE,Place VARCHAR(20),Prize int(10));')
    cursor.execute('CREATE TABLE IF NOT EXISTS Game (time DATE Null ,Winner varchar(40) not null , Loser varchar(40) not null,Tier varchar(20),tname varchar(40),PRIMARY KEY(time,Winner,loser),FOREIGN KEY (`tname`) REFERENCES Tournament(`Name`) on delete cascade on update cascade) ;')
    cursor.execute('CREATE TABLE IF NOT EXISTS Participate ( Placement int(2),tName varchar(50),pName varchar(40),Foreign key (tName) references tournament(name)on delete cascade on update cascade ,foreign key (pName) references player(Name) on delete cascade on update cascade ,primary key(pName,tName));')

#Rekordok feltoltese egyesevel
def recordUpload():
    dbhost = 'localhost'
    dbuser = 'root'
    con = mysql.connect(host=dbhost, user=dbuser)
    cursor = con.cursor()
    cursor.execute('USE CHESS;')
    cursor.execute(
        'INSERT INTO `player` (`Name`, `Birthdate`, `Nationality`, `MMR`) VALUES ("Magnus Carlsen", "1990-11-30", "Norway", "2855");')
    cursor.execute(
        "INSERT INTO `player` (`Name`, `Birthdate`, `Nationality`, `MMR`) VALUES ('Liren Ding', '1992-10-24', 'China', '2799');")
    cursor.execute(
        "INSERT INTO `player` (`Name`, `Birthdate`, `Nationality`, `MMR`) VALUES ('Fabiano Caruana', '1992-07-30', 'USA', '2791');")
    cursor.execute(
        "INSERT INTO `player` (`Name`, `Birthdate`, `Nationality`, `MMR`) VALUES ('Ian Nepomniachtchi', '1990-07-14', 'Russia', '2782');")
    cursor.execute(
        "INSERT INTO `player` (`Name`, `Birthdate`, `Nationality`, `MMR`) VALUES ('Levon Aronian', '1982-10-06', 'Armenia', '2782');")
    cursor.execute(
        "INSERT INTO `player` (`Name`, `Birthdate`, `Nationality`, `MMR`) VALUES ('Anish Giri', '1994-06-28', 'Netherlands', '2774');")
    cursor.execute(
        "INSERT INTO `player` (`Name`, `Birthdate`, `Nationality`, `MMR`) VALUES ('Alexander Grischuk', '1983-10-31', 'Russia', '2773');")
    cursor.execute(
        "INSERT INTO `player` (`Name`, `Birthdate`, `Nationality`, `MMR`) VALUES ('Wesley So', '1993-10-09', 'USA', '2772');")
    cursor.execute(
        " INSERT INTO `player` (`Name`, `Birthdate`, `Nationality`, `MMR`) VALUES ('Alireza Firouzja', '2003-06-18', 'France', '2770');")
    cursor.execute(
        " INSERT INTO `player` (`Name`, `Birthdate`, `Nationality`, `MMR`) VALUES ('Maxime Vachier-Lagrave', '1990-10-21', 'France', '2766');")
    cursor.execute(
        "INSERT INTO `player` (`Name`, `Birthdate`, `Nationality`, `MMR`) VALUES ('Shakhriyar Mamedyarov', '1985-04-12', 'Azerbaijan', '2765');")
    cursor.execute(
        "INSERT INTO `player` (`Name`, `Birthdate`, `Nationality`, `MMR`) VALUES ('Richard Rapport', '1996-03-25', 'Hungary', '2763');")
    cursor.execute(
        "INSERT INTO `player` (`Name`, `Birthdate`, `Nationality`, `MMR`) VALUES ('Teimour Radjabov', '1987-03-12', 'Azerbaijan', '2763');")
    cursor.execute(
        "INSERT INTO `player` (`Name`, `Birthdate`, `Nationality`, `MMR`) VALUES ('Jan-Krzysztof Duda', '1998-04-26', 'Poland', '2756');")
    cursor.execute(
        "INSERT INTO `player` (`Name`, `Birthdate`, `Nationality`, `MMR`) VALUES ('Leinier Dominguez Perez', '1983-09-23', 'USA', '2752');")
    cursor.execute(
        "INSERT INTO `player` (`Name`, `Birthdate`, `Nationality`, `MMR`) VALUES ('Viswanathan Anand', '1969-12-11', 'India', '2751');")
    cursor.execute(
        "INSERT INTO `player` (`Name`, `Birthdate`, `Nationality`, `MMR`) VALUES ('Wang Hao', '1989-08-04', 'China', '2744');")
    cursor.execute(
        "INSERT INTO `player` (`Name`, `Birthdate`, `Nationality`, `MMR`) VALUES ('Sergey Karjakin', '1990-01-12', 'Russia', '2743');")
    cursor.execute(
        "INSERT INTO `player` (`Name`, `Birthdate`, `Nationality`, `MMR`) VALUES ('Hikaru Nakamura', '1987-12-09', 'USA', '2736');")
    cursor.execute(
        "INSERT INTO `player` (`Name`, `Birthdate`, `Nationality`, `MMR`) VALUES ('Nikita Vitiugov', '1987-02-04', 'Russia', '2734');")
    #comit nelkul nem megy vegbe semmilyen valtozas
    con.commit()

    cursor.execute("INSERT INTO `tournament` (`Name`, `startTime`, `EndTime`, `Place`, `Prize`)VALUES ('Magnus Carlsen Invitational', '2021-03-13', '2021-03-21', 'online', '1500000');")
    cursor.execute("INSERT INTO `participate` (`Placement`, `tName`, `pName`) VALUES ('1', 'Magnus Carlsen Invitational', 'Anish Giri');")
    cursor.execute("INSERT INTO `participate` (`Placement`, `tName`, `pName`) VALUES ('8', 'Magnus Carlsen Invitational', 'Alireza Firouzja');")
    cursor.execute("INSERT INTO `participate` (`Placement`, `tName`, `pName`) VALUES ('8', 'Magnus Carlsen Invitational', 'Hikaru Nakamura');")
    cursor.execute("INSERT INTO `participate` (`Placement`, `tName`, `pName`) VALUES ('4', 'Magnus Carlsen Invitational', 'Wesley So');")
    cursor.execute("INSERT INTO `participate` (`Placement`, `tName`, `pName`) VALUES ('3', 'Magnus Carlsen Invitational', 'Magnus Carlsen');")
    cursor.execute("INSERT INTO `participate` (`Placement`, `tName`, `pName`) VALUES ('2', 'Magnus Carlsen Invitational', 'Ian Nepomniachtchi');")
    cursor.execute("INSERT INTO `participate` (`Placement`, `tName`, `pName`) VALUES ('8', 'Magnus Carlsen Invitational', 'Maxime Vachier-Lagrave');")
    cursor.execute("INSERT INTO `participate` (`Placement`, `tName`, `pName`) VALUES ('8', 'Magnus Carlsen Invitational', 'Levon Aronian');")
    cursor.execute("INSERT INTO `participate` (`Placement`, `tName`, `pName`) VALUES ('16', 'Magnus Carlsen Invitational', 'Sergey Karjakin');")
    cursor.execute("INSERT INTO `participate` (`Placement`, `tName`, `pName`) VALUES ('16', 'Magnus Carlsen Invitational', 'Teimour Radjabov');")
    cursor.execute("INSERT INTO `participate` (`Placement`, `tName`, `pName`) VALUES ('16', 'Magnus Carlsen Invitational', 'Shakhriyar Mamedyarov');")
    cursor.execute("INSERT INTO `game` (`time`, `Winner`, `Loser`, `Tier`, `tname`) VALUES ('2021-03-16', 'Anish Giri', 'Maxime Vachier-Lagrave', 'QuarterFinal', 'Magnus Carlsen Invitational');")
    cursor.execute("INSERT INTO `game` (`time`, `Winner`, `Loser`, `Tier`, `tname`) VALUES ('2021-03-16', 'Wesley So', 'Alireza Firouzja', 'QuarterFinal', 'Magnus Carlsen Invitational');")
    cursor.execute("INSERT INTO `game` (`time`, `Winner`, `Loser`, `Tier`, `tname`) VALUES ('2021-03-16', 'Ian Nepomniachtchi', 'Hikaru Nakamura', 'QuarterFinal', 'Magnus Carlsen Invitational');")
    cursor.execute("INSERT INTO `game` (`time`, `Winner`, `Loser`, `Tier`, `tname`) VALUES ('2021-03-16', 'Magnus Carlsen', 'Levon Aronian', 'QuarterFinal', 'Magnus Carlsen Invitational');")
    cursor.execute("INSERT INTO `game` (`time`, `Winner`, `Loser`, `Tier`, `tname`) VALUES ('2021-03-18', 'Anish Giri', 'Wesley So', 'SemiFinal', 'Magnus Carlsen Invitational');")
    cursor.execute("INSERT INTO `game` (`time`, `Winner`, `Loser`, `Tier`, `tname`) VALUES ('2021-03-19', 'Ian Nepomniachtchi', 'Magnus Carlsen', 'SemiFinal', 'Magnus Carlsen Invitational');")
    cursor.execute("INSERT INTO `game` (`time`, `Winner`, `Loser`, `Tier`, `tname`) VALUES ('2021-03-12', 'Magnus Carlsen', 'Wesley So', '3rd Place', 'Magnus Carlsen Invitational');")
    cursor.execute("INSERT INTO `game` (`time`, `Winner`, `Loser`, `Tier`, `tname`) VALUES ('2021-03-21', 'Anish Giri', 'Ian Nepomniachtchi', 'Final', 'Magnus Carlsen Invitational');")
    con.commit()
    con.close()

#rekordok feltoltese Batchekben
def recordUploadSmarter():
    dbhost = 'localhost'
    dbuser = 'root'
    con = mysql.connect(host=dbhost, user=dbuser)
    cursor = con.cursor()
    cursor.execute('USE CHESS;')
    cursor.execute( "INSERT INTO `tournament` (`Name`, `startTime`, `EndTime`, `Place`, `Prize`)VALUES ('2019 FIDE World Cup', '2019-09-10', '2021-10-04', 'Khanty-Mansiysk', '1600000');")
    cursor.execute( "INSERT INTO `tournament` (`Name`, `startTime`, `EndTime`, `Place`, `Prize`)VALUES ('2021 FIDE World Cup', '2021-07-12', '2021-08-06', 'Krasnaya Polyana', '1900000');")
    part_data = [
        ('1','2021 FIDE World Cup','Jan-Krzysztof Duda'),
        ('2','2021 FIDE World Cup','Sergey Karjakin'),
        ('3','2021 FIDE World Cup','Magnus Carlsen'),
        ('16','2021 FIDE World Cup','Alexander Grischuk'),
        ('16','2021 FIDE World Cup','Maxime Vachier-Lagrave'),
        ('64','2021 FIDE World Cup','Anish Giri'),
        ('64','2021 FIDE World Cup','Shakhriyar Mamedyarov'),
        ('64','2021 FIDE World Cup','Fabiano Caruana'),
        ('128','2021 FIDE World Cup','Alireza Firouzja'),
        ('128','2021 FIDE World Cup','Leinier Dominguez Perez'),

        ('1', '2019 FIDE World Cup', 'Liren Ding'),
        ('3', '2019 FIDE World Cup', 'Teimour Radjabov'),
        ('4', '2019 FIDE World Cup', 'Maxime Vachier-Lagrave'),
        ('8', '2019 FIDE World Cup', 'Alexander Grischuk'),
        ('8', '2019 FIDE World Cup', 'Nikita Vitiugov'),
        ('8', '2019 FIDE World Cup', 'Levon Aronian'),
        ('16', '2019 FIDE World Cup', 'Leinier Dominguez Perez'),
        ('16', '2019 FIDE World Cup', 'Wesley So'),
        ('16', '2019 FIDE World Cup', 'Ian Nepomniachtchi'),
        ('16', '2019 FIDE World Cup', 'Jan-Krzysztof Duda')
    ]
    stmt_part = 'Insert into participate(Placement,tName,pName) Values (%s, %s, %s);'
    cursor.executemany(stmt_part, part_data)
    con.commit()

    stmt_game = 'Insert into game(time,winner,loser,tier,tname) values (%s, %s, %s, %s, %s);'
    game_data = [
        ('2021-08-06','Jan-Krzysztof Duda','Sergey Karjakin','final','2021 FIDE World Cup'),
        ('2021-08-06','Magnus Carlsen','Vladimir Fedoseev','thirdPlace','2021 FIDE World Cup'),
        ('2021-08-04','Jan-Krzysztof Duda','Magnus Carlsen','semiFinal','2021 FIDE World Cup'),
        ('2021-08-04','Sergey Karjakin','Vladimir Fedoseev','semiFinal','2021 FIDE World Cup'),
        ('2021-08-02','Jan-Krzysztof Duda','Santosh Gujrathi Vidit','quarterFinal','2021 FIDE World Cup'),
        ('2021-08-02','Magnus Carlsen','Etienne Bacrot','quarterFinal','2021 FIDE World Cup'),
        ('2021-08-01','Sergey Karjakin','Sam Shankland','quarterFinal','2021 FIDE World Cup'),
        ('2021-08-06','Vladimir Fedoseev','M.amin Tatabaei','quarterFinal','2021 FIDE World Cup'),
        ('2021-07-29','Santosh Gujrathi Vidit','Vasif Durarbayli','Eighth-finals','2021 FIDE World Cup'),
        ('2021-07-29','Vladimir Fedoseev','Velimir Ivic','Eighth-finals','2021 FIDE World Cup'),
        ('2021-07-28','M.amin Tatabaei','Halik M. Martirosyan','Eighth-finals','2021 FIDE World Cup'),
        ('2021-07-28','Sergey Karjakin','Maxime Vachier-Lagrave','Eighth-finals','2021 FIDE World Cup'),
        ('2021-07-26','Sam Shankland','Peter Svidler','Eighth-finals','2021 FIDE World Cup'),
        ('2021-07-26','Jan-Krzysztof Duda','Alexander Grischuk','Eighth-finals','2021 FIDE World Cup'),
        ('2021-07-25', 'Magnus Carlsen', 'Andrey Esipenko', 'Eighth-finals', '2021 FIDE World Cup'),
        ('2021-07-25','Nodirbek Abdusattorov','Anish Giri','32nd-finals','2021 FIDE World Cup'),
        ('2021-07-24','Halik M. Martirosyan','Shakhriyar Mamedyarov','32nd-finals','2021 FIDE World Cup'),
        ('2021-07-24','Magnus Carlsen','Radoslaw wojtaszek','32nd-finals','2021 FIDE World Cup'),
        ('2021-07-22','Alexander Grischuk','Anton Korobov','32nd-finals','2021 FIDE World Cup'),
        ('2021-07-22','Jan-Krzysztof Duda','Pouya Idani','32nd-finals','2021 FIDE World Cup'),
        ('2021-07-22', 'Maxime Vachier-Lagrave', 'R Praggnanandhaa', '32nd-finals', '2021 FIDE World Cup'),
        ('2021-07-22', 'Serger Karjakin', 'Vladislav Artemiev', '32nd-finals', '2021 FIDE World Cup'),
        ('2021-07-19','Magnus Carlsen','Aryan Tari','64nd-finals','2021 FIDE World Cup'),
        ('2021-07-19','Alexander Grischuk','Alan Pichot','64nd-finals','2021 FIDE World Cup'),
        ('2021-07-19','Jan-Krzysztof Duda','Samuel Sevian','64nd-finals','2021 FIDE World Cup'),
        ('2021-07-19','Maxime Vachier-Lagrave',' Paravyan','64nd-finals','2021 FIDE World Cup'),
        ('2021-07-19','Serger Karjakin','Grigoriy Oparin','64nd-finals','2021 FIDE World Cup'),
        ('2021-07-19', 'Rinat Jumabayev', 'Fabiano Caruana', '64nd-finals', '2021 FIDE World Cup'),
        ('2021-07-15','Magnus Carlsen','Sasa Martinovic','128nd-finals','2021 FIDE World Cup'),
        ('2021-07-15','Jakhongir Vakhidov','Leinier Dominguez Perez ','128nd-finals','2021 FIDE World Cup'),
        ('2021-07-15','Javokhir Sindarov','Alireza Firouzja','128nd-finals','2021 FIDE World Cup'),
        ('2021-07-13','Alexander Grischuk','Federico Perez Ponsa','128nd-finals','2021 FIDE World Cup'),
        ('2021-07-13','Jan-Krzysztof Duda','Guillermo Vazquez','128nd-finals','2021 FIDE World Cup'),
        ('2021-07-11','Anish Giri','Boris Savchenko','128nd-finals','2021 FIDE World Cup'),
        ('2021-07-11','Bobby Cheng','Levon Aronian','128nd-finals','2021 FIDE World Cup'),
        ('2021-07-08','Shakhriyar Mamedyarov','Sevag Krikor','128nd-finals','2021 FIDE World Cup'),
        ('2021-07-08','Maxime Vachier-Lagrave','Elshan Moradiabadi','128nd-finals','2021 FIDE World Cup'),
        ('2021-07-06','Serger Karjakin','Shamsiddin Vokhidov','128nd-finals','2021 FIDE World Cup'),
        ('2021-07-06','Fabiano Caruana','Susanto Megaranto','128nd-finals','2021 FIDE World Cup'),

        ('2019-10-04','Teimour Radjabov','Liren Ding','final','2021 FIDE World Cup'),
        ('2019-10-03','Maxime Vachier-Lagrave','Yangyi Yu','3rd','2021 FIDE World Cup'),
        ('2019-10-01','Teimour Radjabov','Maxime Vachier-Lagrave','semifinal','2021 FIDE World Cup'),
        ('2019-10-01','Liren Ding','Yangyi Yu','semifinal','2021 FIDE World Cup'),
        ('2019-09-29','Liren Ding','Alexander Grischuk','quarterFInal','2021 FIDE World Cup'),
        ('2019-09-29','Yangyi Yu','Nikita Vitiugov','quarterFInal','2021 FIDE World Cup'),
        ('2019-09-27','Maxime Vachier-Lagrave','Levon Aronian','quarterFInal','2021 FIDE World Cup'),
        ('2019-09-27','Teimour Radjabov','Jeffrey Xiong','quarterFInal','2021 FIDE World Cup'),
    ]
    cursor.executemany(stmt_game, game_data)
    con.commit()

