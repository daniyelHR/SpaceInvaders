class Ship:
    # ShotDirection
    # sprite

    def shot(self, isUp, posH, posV):
        fill(25, 255, 0)
        b = Bullet(isUp, posH, posV) # tworzymy instancję pocisku
        bullet_group.add(b) # dodajemy do listy sktywnych pocisków ów pocisk
        rect(0, 20, 20, 20) # to zostawiam w celach debugowych 
        self.speed = 3  # ustawienie prędkości ruchu pocisku


class Player(Ship):

    # poczatkowa pozycja
    def __init__(self):
        self.positionH = 350
        self.positionV = 475
        self.sprite = loadImage("Gracz One.png")  # teraz trzeba ją w oddzielnej metodzie rysować uwzględniając pozycję
        # zmienne potrzebne do porusznia eksplozją
        self.a = 380
        self.b = 260
        self.c = 420
        self.d = 260
        self.e = 380
        self.f = 300
        self.g = 420
        self.h = 300
        self.i = 40
        # zmienne spadających gwiazd
        self.aa = 5
        self.bb = 5
        self.cc = 1
        self.dd = 100
        self.ee = 300

    # grafika - spadające_gwiazdy_animacja
    def shooting_stars(self):
        self.aa = self.aa + 5
        self.bb = self.bb + 5
        self.cc = self.cc + 0.15
        self.dd = self.dd + 5
        self.ee = self.ee + 5
        
        if (self.aa > 800) or (self.bb > 600):
            self.aa = random(0,300)
            self.bb = random(0,400)
            self.cc = 1
        if (self.dd > 800) or (self.ee > 600):
            self.dd = random(0,300)
            self.ee = random(0,400)
            self.cc = 1
        fill(255, 255, 100)
        stroke(255, 255, 200)
        rect(self.aa, self.bb, self.cc, self.cc)
        rect(self.dd, self.ee, self.cc, self.cc)

    # grafika - eksplozja_animacja - trzeba uwzględnić pozycję z której ma eksplozja nastąpić
    def sketch_explosion(self):
        self.sprite = loadImage("explosion.png")
        if (self.positionV < 440 and self.positionV > 320) and (
            (
                self.positionH > 40 and self.positionH < 160
            )  # utrudnienie - eksplozja gracza po wleceniu w tarcze
            or (self.positionH > 280 and self.positionH < 420)
            or (self.positionH > 540 and self.positionH < 680)
        ):
            image(self.sprite, self.positionH - 15, self.positionV - 15)
        #player1.sketch_explosion()

    def changePositionH(self, offset):
        self.positionH = self.positionH + offset

    def changePositionV(self, offset):
        self.positionV = self.positionV + offset

    def sketch_player(self):
        image(self.sprite, self.positionH, self.positionV, 100, 80)


class Enemy(Ship):
    nextShot = 0
    quantity = 6

    def __init__(self, pos):
        self.positionHorizontal = pos
        self.positionVertical = 15
        self.movementDirection = 1
        self.visability = True
        self.sprite = loadImage("Ship.png")

    def changePosition(self):
        if self.positionHorizontal < 0:
            self.positionVertical += 50
            self.movementDirection = 1
        if self.positionHorizontal > 700:
            self.positionVertical += 50
            self.movementDirection = 0
        if self.movementDirection == 0:
            self.positionHorizontal -= 1.7
        if self.movementDirection == 1:
            self.positionHorizontal += 1.7
    def changeVisability(self):
        self.visability = False  # zmina visability
        # sprawdzanie czy wszyscy zestrzeleni (areEnemiesDestroyed)
        # doliczenie punktów

    def sketch_ship(self):
        image(self.sprite, self.positionHorizontal, self.positionVertical)
		
class Bullet:
    def __init__(self, direction, posH, posV):  # tu powinna być przekazana pozycja statku
        self.positionH = posH
        self.positionV = posV
        self.direction = 0

    def update(self):  # movement - metoda
        self.positionV += 5  # szybkosc lotu pocisku
        if self.positionV >= 600:
            bullet_group.remove(self)
			 
    def sketch_bullet(self):
        fill(255, 0, 0)
        stroke(0)
        beginShape()
        curveVertex(50, 60)
        curveVertex(30, 30)
        curveVertex(75, 60)
        curveVertex(100, 100)
        curveVertex(50, 120)
        curveVertex(30, 30)
        curveVertex(80, 80)
        endShape(CLOSE)

    def sketch_bullet2(self):
        rect(100, 100, 10, 10)
        rect(90, 110, 10, 10)
        rect(100, 110, 10, 10)
        rect(110, 110, 10, 10)
        rect(80, 120, 10, 10)
        rect(90, 120, 10, 10)
        rect(100, 120, 10, 10)
        rect(110, 120, 10, 10)
        rect(120, 120, 10, 10)
        rect(90, 130, 10, 10)
        rect(100, 130, 10, 10)
        rect(110, 130, 10, 10)
        rect(100, 140, 10, 10)
        rect(100, 150, 10, 10)
        noStroke()

    def update_movement(self):
        fill(255, 0, 0)
        stroke(0)
        beginShape()
        curveVertex(50 + self.positionH, 60 + self.positionV)
        curveVertex(30 + self.positionH, 30 + self.positionV)
        curveVertex(75 + self.positionH, 60 + self.positionV)
        curveVertex(100 + self.positionH, 100 + self.positionV)
        curveVertex(50 + self.positionH, 120 + self.positionV)
        curveVertex(30 + self.positionH, 30 + self.positionV)
        curveVertex(80 + self.positionH, 80 + self.positionV)
        endShape(CLOSE)


class RepairKit:
    def sketch_RepairKit(self):
        self.sprite = loadImage("RepairKit.png")  # to tylko załadowanie grafiki, nie rysowanie, powinnodziać isę raz, nie co klatkę
        self.positionH = 0
        self.positionV = 500
        image(self.sprite, self.positionH, self.positionV)
        self.visability = False


class Shield:
    def sketch_shield(self):
        fill(102, 255, 255)
        stroke(10, 150, 0)
        rect(80, 400, 120, 50)
        rect(340, 400, 120, 50)
        rect(600, 400, 120, 50)

        self.visability = True  # to raczej w konstruktorze powinno być

    def changeVisability(shield):
        pass


class Interface:
    points = 0
    health = 100

    def draw_health(self):

        fill(255, 0, 0)
        rect(550, 550, self.health * 2, 30)

        textSize(30)
        text("Health: " + str(self.health), 550, 540)

    def bulletOrShipIntoYou(self):
        self.health -= 10
        image(loadImage("gameover.png"), 300,400)# wyświetlenie GameOver
        player1.sketch_explosion()
    def areEnemiesDestroyed(self):
        for enemy in enemyList:
            if enemy.visability == True:
                return False
        text("Brawo! Zwycięstwo!", width / 3, height / 2)
        return True

    def addPoint(self):
        Interface.points += 1

    def showScore(self):
        textSize(30)
        text(
            "Score:" + str(Interface.points), 5, 50
        )  # metoda wyświetlająca bieżącą punktację


def setup():  # ta funkcja może występować tylko raz w programie
    size(800, 600)
    global enemyList, player1, ship1, bullet_group, tlo, s, repairKit, interface
    tlo = loadImage("background.jpg")  # rozdzielczość 300 ustawiamy dla wydruków, do wyświetlania 72...
    player1 = Player()
    enemyList = []
    for num, i in enumerate(range(Enemy.quantity)):
        enemyList.append(Enemy(0 + num * 100))
    bullet_group = set()
    s = Shield()
    interface = Interface()
    repairKit = RepairKit()


def draw():
    image(tlo, 0, 0)
    player1.sketch_player()
    player1.shooting_stars()
    s.sketch_shield()
    repairKit.sketch_RepairKit()
    
    if keyPressed:
        if key == "a" or keyCode == 37:  # jeżeli strzałka w lewo albo 'a'
            player1.changePositionH(-5)
        if key == "d" or keyCode == 39:  # jeżeli strzałka w prawo albo 'd'
            player1.changePositionH(5)
        '''
        if key == "w" or keyCode == 38:  # jeżeli strzałka w gore albo 'w'
            player1.changePositionV(-5)
        if key == "s" or keyCode == 40:  # jeżeli strzałka w dol albo 's'
            player1.changePositionV(5)
        '''
        if key == " " or key == ENTER: # jeżeli spacja lub enter lub strzałka w dół
            player1.shot(True, player1.positionH, player1.positionV)
			
    for enemy in enemyList:
        enemy.changePosition()
        if enemy.positionVertical >=player1.positionV-15:
            interface.bulletOrShipIntoYou()
        enemy.sketch_ship()
        enemy.nextShot -= 1  # loop countdown to shot
        if enemy.nextShot <= 0:  # loop countdown to shot
            isShooting = int(random(0, 2))  # drawing whether the opponent shoots
            enemy.nextShot = 100  # loop countdown to shot
            if isShooting == 1:  # if the shot is drawn
                enemy.shot(False, enemy.positionHorizontal, enemy.positionVertical)

    for bullet in bullet_group:
        bullet.update()
        bullet.update_movement() # przesunięcie w odpowiednim kierunku pozycji każdego z aktywnych pocisków na ekranie (liście pocisków ekranu)
        bullet.sketch_bullet2()

    # sprawdzenie, czy pozycja vertykalna pocisku jest na wysokości statku - taka jak pozycje vertykalne statków
    # sprawdzenie, czy dotyka gracza lub przeciwnika
    # sprawdzenie, czy kierunek strzały jest zgodny ze statkiem którego dotyka
    # zależnie od tego którego statku dotyka, wywołanie bulletIntoYou lub zmiana visability wroga

    interface.showScore() # wyświetlenie aktualnej liczby punktów
    interface.draw_health()
