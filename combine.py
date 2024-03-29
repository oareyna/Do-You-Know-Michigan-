import pygame
import sys
from pygame import mixer
pygame.display.set_caption("Do you know Michigan?")

pygame.init()
mixer.music.load("background.wav")
mixer.music.play(-1)
screen = pygame.display.set_mode((960, 540))

background = pygame.image.load('pres.png')
background2 = pygame.image.load("goak.png")
background3 = pygame.image.load("kitty.png")
background4 = pygame.image.load("dog.png")
background5 = pygame.image.load("fifth.png")
background6 = pygame.image.load("sixth.png")
background7 = pygame.image.load("seventh.png")
background8 = pygame.image.load("eigth.png")
background9 = pygame.image.load("ninth.png")
background10 = pygame.image.load("tenth.png")
pompompurin = pygame.image.load("pompompurin2.png")
font = pygame.font.Font('freesansbold.ttf', 20)
fool="Correct"
playerImg = pygame.image.load('snorlax.png')
kuromi = pygame.image.load('kuromi2.png')

screen_width = 960
screen_height = 540

point=0

def display_text(text, position):
    rendered_text = font.render(text, True, (255, 20, 147))
    screen.blit(rendered_text, position)

color = 255, 20, 147
def get_input():

    input_text = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return input_text
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        screen.fill((0, 200, 0))
        screen.blit(pompompurin, (0, 0))
        display_text("Enter your name:", (screen_width // 2 - 100, screen_height // 2 - 50))
        display_text(input_text, (screen_width // 2 - 100, screen_height // 2))
        pygame.display.flip()
        # x=False

def greet_user(username):
    global point
    screen.fill((250, 250, 250))
    screen.blit(kuromi, (0, 0))
    if username.lower() == "nicholas":
        point -= 100
    elif username.lower() == "olivia":
        point += 1000

    greeting = f"Hello, {username}, you have {point} points!!!"
    display_text(greeting, (300, 220))
    status()
    pygame.display.flip()

def main():
    username = get_input()
    greet_user(username)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

def player():
    screen.fill((250, 250, 250))
    screen.blit(playerImg, (200,300))

apple="Incorrect"
def show_score(x, y):
    score = font.render(str(fool), True, (0, 0, 0))
    screen.blit(score, (x, y))
def incorrect(x, y):
    score = font.render(str(apple), True, (0, 0, 0))
    screen.blit(score, (x, y))
def points(x, y):
    score = font.render(str(point), True, (0, 0, 0))
    screen.blit(score, (x, y))

def status():
    o = "  Status based off points:"
    oa = "-100 >= x : Hates michigan"
    ob = "   0 >= x : Foreigner"
    oc = "   2 >= x : Thinks michigan is ohio"
    od = "   5 >= x : visited Michigan for a day "
    oe = "   7 >= x : Grandma lives in Michigan"
    of = "   9 >= x : Wannabe Canadian"
    og = "    10/10 : Is michigan"
    oh = "   10 < x : Is goated"
    a="Hates michigan"
    b="Foreigner"
    c="Thinks michigan is ohio"
    d="visited Michigan for a day"
    e="Grandma lives in Michigan"
    f="Wannabe Canadian"
    g="Is michigan"
    h="Is goated"
    score = font.render(str(o), True, (color))
    screen.blit(score, (10, 20))
    score = font.render(str(oa), True, (color))
    screen.blit(score, (10, 40))
    score = font.render(str(ob), True, (color))
    screen.blit(score, (10, 60))
    score = font.render(str(oc), True, (color))
    screen.blit(score, (10, 80))
    score = font.render(str(od), True, (color))
    screen.blit(score, (10, 100))
    score = font.render(str(oe), True, (color))
    screen.blit(score, (10, 120))
    score = font.render(str(of), True, (color))
    screen.blit(score, (10, 140))
    score = font.render(str(og), True, (color))
    screen.blit(score, (10, 160))
    score = font.render(str(oh), True, (color))
    screen.blit(score, (10, 180))
    if point <= -100:
        score = font.render(str(a), True, (color))
        screen.blit(score, (340, 300))
    elif point <= 0:
        score = font.render(str(b), True, (color))
        screen.blit(score, (340, 300))
    elif point <= 2:
        score = font.render(str(c), True, (color))
        screen.blit(score, (340, 300))
    elif point <= 5:
        score = font.render(str(d), True, (color))
        screen.blit(score, (340, 260))
    elif point <= 7:
        score = font.render(str(e), True, (color))
        screen.blit(score, (340, 300))
    elif point <= 9:
        score = font.render(str(f), True, (color))
        screen.blit(score, (340, 300))
    elif point == 10:
        score = font.render(str(g), True, (color))
        screen.blit(score, (340, 300))
    elif point > 10:
        score = font.render(str(h), True, (color))
        screen.blit(score, (340, 300))
    pygame.display.update()

elp="Points:"
def poke(x, y):
    score = font.render(str(elp), True, (0, 0, 0))
    screen.blit(score, (x, y))
clock = pygame.time.Clock()

def cream():
    player()
    show_score(50, 200)
    pygame.display.flip()

running = True
jib = True
jab = True
jirk = True
jack=True
juice = True
juke = True
juck = True
jv = True
jeep = True
java = True
image_permanent = False
chirp = False
rap = False
plank=False
guitar = False
clarinet = False
piano = False
violin = False
viola = False
conductor = False
prat = False
while running:
    clock.tick(2)
    screen.fill((250, 250, 250))
    screen.blit(background, (0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if jib == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    image_permanent = True
                    point+=1
                    jib = False

                elif event.key == pygame.K_a or event.key == pygame.K_c or event.key == pygame.K_d:
                    point-=1
                    player()
                    incorrect(430, 100)
        elif jab == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    chirp = True
                    point+=1
                    jab = False

                elif event.key == pygame.K_a or event.key == pygame.K_b or event.key == pygame.K_d:
                    point-=1
                    player()
                    incorrect(430, 100)

        elif jirk == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    rap = True
                    point+=1
                    jirk = False

                elif event.key == pygame.K_c or event.key == pygame.K_b or event.key == pygame.K_d:
                    point-=1
                    player()
                    incorrect(430, 100)

        elif jack == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    plank = True
                    point+=1
                    jack = False

                elif event.key == pygame.K_c or event.key == pygame.K_a or event.key == pygame.K_d:
                    point-=1
                    player()
                    incorrect(430, 100)
        elif juice == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    guitar = True
                    point+=1
                    juice = False

                elif event.key == pygame.K_c or event.key == pygame.K_a or event.key == pygame.K_b:
                    point-=1
                    player()
                    incorrect(430, 100)
        elif juke == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    clarinet = True
                    point+=1
                    juke = False

                elif event.key == pygame.K_c or event.key == pygame.K_a or event.key == pygame.K_d:
                    point-=1
                    player()
                    incorrect(430, 100)
        elif juck == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    piano = True
                    point+=1
                    juck = False

                elif event.key == pygame.K_c or event.key == pygame.K_a or event.key == pygame.K_d:
                    point-=1
                    player()
                    incorrect(430, 100)
        elif jv == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    violin = True
                    point+=1
                    jv = False

                elif event.key == pygame.K_b or event.key == pygame.K_a or event.key == pygame.K_d:
                    point-=1
                    player()
                    incorrect(430, 100)
        elif jeep == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    viola = True
                    point+=1
                    jeep = False

                elif event.key == pygame.K_c or event.key == pygame.K_a or event.key == pygame.K_b:
                    point-=1
                    player()
                    incorrect(430, 100)
        elif java == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    conductor = True
                    point+=1
                    java = False

                elif event.key == pygame.K_c or event.key == pygame.K_b or event.key == pygame.K_d:
                    point-=1
                    player()
                    incorrect(430, 100)

    if image_permanent:
        player()
        show_score(430, 100)
        pygame.display.update()
        screen.blit(background2, (0, 0))
        poke(20,100)
        points(100,100)
        pygame.display.update()
        image_permanent = False
        background=background2


    if chirp:
        player()
        show_score(430, 100)
        pygame.display.update()
        screen.blit(background3, (0, 0))
        poke(20,100)
        points(100,100)
        pygame.display.update()
        chirp = False
        background = background3

    elif rap:
        player()
        show_score(430, 100)
        pygame.display.update()
        screen.blit(background4, (0, 0))
        poke(20,100)
        points(100,100)
        pygame.display.update()
        rap = False
        background = background4

    elif plank:
        player()
        show_score(430, 100)
        pygame.display.update()
        screen.blit(background5, (0, 0))
        poke(20,100)
        points(100,100)
        pygame.display.update()
        plank = False
        background = background5

    elif guitar:
        player()
        show_score(430, 100)
        pygame.display.update()
        screen.blit(background6, (0, 0))
        poke(20,100)
        points(100,100)
        pygame.display.update()
        guitar = False
        background = background6
    elif clarinet:
        player()
        show_score(430, 100)
        pygame.display.update()
        screen.blit(background7, (0, 0))
        poke(20,100)
        points(100,100)
        pygame.display.update()
        clarinet = False
        background = background7
    elif piano:
        player()
        show_score(430, 100)
        pygame.display.update()
        screen.blit(background8, (0, 0))
        poke(20,100)
        points(100,100)
        pygame.display.update()
        piano = False
        background = background8
    elif violin:
        player()
        show_score(430, 100)
        pygame.display.update()
        screen.blit(background9, (0, 0))
        poke(20,100)
        points(100,100)
        pygame.display.update()
        violin = False
        background = background9
    elif viola:
        player()
        show_score(430, 100)
        pygame.display.update()
        screen.blit(background10, (0, 0))
        poke(20,100)
        points(100,100)
        pygame.display.update()
        viola = False
        background = background10
    elif conductor:
        player()
        show_score(430, 100)
        pygame.display.update()
        screen.blit(background10, (0, 0))
        poke(20,100)
        points(100,100)
        pygame.display.update()
        conductor = False
        prat = True
        background = background10
    elif prat:
        main()
        status()


    pygame.display.update()

pygame.quit()


