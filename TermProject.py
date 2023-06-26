import pygame # 1. pygame 선언
import random
pygame.init() # 2. pygame 초기화
pygame.display.set_caption("다람쥐의 모험")


flying_enemies = []
walking_enemies = []
player_walk = [pygame.image.load('sprite\squirrel\walk1.png'),pygame.image.load('sprite\squirrel\walk2.png'),
               pygame.image.load('sprite\squirrel\walk3.png'),pygame.image.load('sprite\squirrel\walk4.png'),
               pygame.image.load('sprite\squirrel\walk5.png'),pygame.image.load('sprite\squirrel\walk6.png'),
               pygame.image.load('sprite\squirrel\walk7.png'),pygame.image.load('sprite\squirrel\walk8.png')]
enemy1_move = [pygame.image.load('sprite\enemy1\img2.png'),pygame.image.load('sprite\enemy1\img4.png'),
               pygame.image.load('sprite\enemy1\img6.png'),pygame.image.load('sprite\enemy1\img8.png'),
               pygame.image.load('sprite\enemy1\img10.png'),pygame.image.load('sprite\enemy1\img14.png'),
               pygame.image.load('sprite\enemy1\img14.png'),pygame.image.load('sprite\enemy1\img16.png')]

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load('sprite\squirrel\walk1.png')
        self.image = pygame.transform.scale(self.image, (100, 100)) # 넓이, 높이
        self.rect = self.image.get_rect()
        self.rect.centerx = player_posX
        self.rect.centery = player_posY
        self.walkcount = 0
        
    def get_rect(self):
        return self.rect
    
    def plus_walk_point(self):
        self.walkcount += 1
        if self.walkcount == 8:
            self.walkcount = 0
            self.image = player_walk[self.walkcount]
        else:
            self.image = pygame.transform.scale(self.image, (100,100))
            self.image = player_walk[self.walkcount]

class FlyingEnemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.FlyingEnemy_x = screen_width
        self.FlyingEnemy_y = random.randrange(0,7)*100
        self.x = screen_width
        enemy1 = pygame.image.load('sprite\enemy1\img2.png')
        enemy1 = pygame.transform.scale(enemy1,(100,100))
        enemy2 = pygame.image.load('sprite\enemy2\img2.png')
        enemy2 = pygame.transform.scale(enemy2,(100,100))
        enemy3 = pygame.image.load('sprite\enemy3\img2.png')
        enemy3= pygame.transform.scale(enemy3,(100,100))
        enemy4 = pygame.image.load('sprite\enemy4\img2.png')
        enemy4 = pygame.transform.scale(enemy4,(100,100))
        flying_enemies.append(enemy1)
        flying_enemies.append(enemy2)
        flying_enemies.append(enemy3)
        flying_enemies.append(enemy4)
        self.random_num = random.randrange(0,4)
        self.image = flying_enemies[self.random_num]
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.FlyingEnemy_x
        self.rect.centery = self.FlyingEnemy_y
        
        # 적 이미지 랜덤 변경
    def change_flyingEnemy(self):
        random.shuffle(flying_enemies)
        self.image = flying_enemies[0]
        # 적 이미지 움직이기
    def randomSpeed(self):
        self.x -= random.randrange(45,95) # enemy의 속도를 랜덤으로 조절 -> 적들이 불규칙적으로 등장하도록 한다.
        self.FlyingEnemy_x = self.x
        
        # 적이 화면 끝에 도달하면 위치 초기화
    def returnAndreset(self):
        self.FlyingEnemy_x = screen_width
        self.FlyingEnemy_y = random.randrange(0,7)*100
        
        # 적의 현재 x 좌표 넘기기
    def get_pos(self):
        return self.x
        
        # 적 그리기
    def draw_flyingEnemy(self):
        screen.blit(self.image,(self.FlyingEnemy_x,self.FlyingEnemy_y))
        
    def check_enemy_position(self):
        if self.FlyingEnemy_x <= 0 :
            self.return_enemy()
        else:
            screen.blit(self.image,(self.FlyingEnemy_x,self.FlyingEnemy_y))
            
    def return_enemy(self):
        self.x = 1600
        self.FlyingEnemy_y = random.randrange(0,7)*100
        random.shuffle(flying_enemies)
        self.image = flying_enemies[0]
        
    def get_rect(self):
        return self.rect

class walkingEnemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.WalkingEnemy_x = screen_width
        self.WalkingEnemy_y = 700
        self.x = screen_width

        enemy5 = pygame.image.load('sprite\enemy5\img2.png')
        enemy5 = pygame.transform.scale(enemy5,(100,100))
        enemy6 = pygame.image.load('sprite\enemy6\img2.png')
        enemy6 = pygame.transform.scale(enemy6,(100,100))

        walking_enemies.append(enemy5)
        walking_enemies.append(enemy6)
        
        self.random_num = random.randrange(0,2)
        self.image = walking_enemies[self.random_num]
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.WalkingEnemy_x
        self.rect.centery = self.WalkingEnemy_y
        self.enemy_walkcount = 0
        
        # 적 이미지 랜덤 변경
    def change_walkingEnemy(self):
        random.shuffle(walking_enemies)
        self.image = walking_enemies[0]
        self.enemy_walkcount = 0
        # 적 이미지 움직이기
    def randomSpeed(self):
        self.x -= random.randrange(25,45)
        self.WalkingEnemy_x = self.x
        
        # 적이 화면 끝에 도달하면 위치 초기화
    def returnAndreset(self):
        self.WalkingEnemy_x = screen_width
        self.WalkingEnemy_y = 700
        
        # 적의 현재 x 좌표 넘기기
    def get_pos(self):
        return self.x
        
        # 적 그리기
    def draw_WalkingEnemy(self):
        screen.blit(self.image,(self.WalkingEnemy_x,self.WalkingEnemy_y))
        
    def check_enemy_position(self):
        if self.WalkingEnemy_x <= 0 :
            self.return_enemy()
        else:
            screen.blit(self.image,(self.WalkingEnemy_x,self.WalkingEnemy_y))
            
    def return_enemy(self):
        self.x = 1600
        self.WalkingEnemy_y = 700
        random.shuffle(walking_enemies)
        self.image = walking_enemies[0]
        
    def get_rect(self):
        return self.rect
        
# 3. pygame에 사용되는 전역변수 선언
WHITE = (255,255,255)
screen_height = 900
screen_width = 1600
size = [1600,900]
screen = pygame.display.set_mode(size)
done= False
clock= pygame.time.Clock()

#배경화면 생성
background = pygame.image.load('background1.png')
background = pygame.transform.scale(background, (1600,900))
background2 = background.copy()
backgorund1_x = 0
background2_x = 1600 # background width

#플레이어
is_jump_up =False
is_jump_down = False
player_posX = 300
player_posY = 700



# 4. pygame 무한루프
def runGame():
    global done, screen_height, background, backgorund1_x, background2_x
    global flying_enemies, walking_enemies
    global player_posX, player_posY, is_jump_up,is_jump_down

    start_time_count = pygame.time.get_ticks()

    x = 300 # 주인공의 X 좌표
    y = 700 # 주인공의 Y 좌표
    
    # 캐릭터 생성
    flyingEnemy1 = FlyingEnemy()
    flyingEnemy1.change_flyingEnemy()
    
    flyingEnemy2 = FlyingEnemy()
    flyingEnemy2.change_flyingEnemy()
    
    flyingEnemy3 = FlyingEnemy()
    flyingEnemy3.change_flyingEnemy()
    
    walkingEnemy1 = walkingEnemy()
    walkingEnemy1.change_walkingEnemy()
    
    player = Player()
    
    #캐릭터들의 좌표 값
    
    flyingEnemy1_rect = flyingEnemy1.get_rect()
    flyingEnemy1_rect.left = flyingEnemy1.FlyingEnemy_x
    flyingEnemy1_rect.top = flyingEnemy1.FlyingEnemy_y
    
    flyingEnemy2_rect = flyingEnemy2.get_rect()
    flyingEnemy2_rect.left = flyingEnemy2.FlyingEnemy_x
    flyingEnemy2_rect.top = flyingEnemy2.FlyingEnemy_y
    
    flyingEnemy3_rect = flyingEnemy3.get_rect()
    flyingEnemy3_rect.left = flyingEnemy3.FlyingEnemy_x
    flyingEnemy3_rect.top = flyingEnemy3.FlyingEnemy_y
    
    walkingEnemy1_rect = walkingEnemy1.get_rect()
    walkingEnemy1_rect.left = walkingEnemy1.WalkingEnemy_x
    walkingEnemy1_rect.top = walkingEnemy1.WalkingEnemy_y
    
    player_rect = player.get_rect()
    player_rect.left = player_posX
    player_rect.top = player_posY
    
    gameover_font = pygame.font.SysFont('g마켓산스ttfmedium', 80)
    gameover_text = gameover_font.render('GAME OVER',True,(255,0,0))
    # Gameover 텍스트의 사이즈 가져오기 (화면 가운데 배치시키기 위해)
    size_text_width = gameover_text.get_rect().size[0] # 가로 크기
    size_text_height = gameover_text.get_rect().size[1] # 세로 크기
 
    # gameover의 좌표를 화면 가운데 배치
    x_pos_gameover = screen_width/2-size_text_width/2
    y_pos_gameover = screen_height/2-size_text_height/2

    player.image = pygame.transform.scale(player.image, (100,100))
    
    while not done:
        clock.tick(10) # 1초에 10번 화면 출력 의미
        screen.fill(WHITE) # 배경 채우기
        moveback() # 배경 움직이기
        
        for event in pygame.event.get(): # 해당 게임안에서 이벤트 가져온다 (이벤트는 리스트 형태로 받아오기 때문애 FOR 로 확인한다.)
            if event.type == pygame.QUIT:
                done=True

            # 방향키 입력에 대한 이벤트 처리
            if event.type == pygame.KEYDOWN:
                if event.key== pygame.K_UP: # 좌표상에서 Y + 할수록 아래로 가게되므로 - 해준다.
                    is_jump_up = True
                    is_jump_down = False
                elif event.key == pygame.K_DOWN:
                    is_jump_down = True
                    is_jump_up = False
            
        if is_jump_up == True:
            y -= 100
            player_posY = y
            y = 0
            is_jump_up = False
        if is_jump_down == True:
            y += 100
            player_posY = y
            y = 0
            is_jump_down = False
            
        
        player.plus_walk_point()
        player.image = pygame.transform.scale(player.image, (100,100))
            
        if player_posY >= 0:
            if player_posY <= 700:
                screen.blit(player.image, (player_posX, player_posY))
                y = player_posY
                
            else:
                screen.blit(player.image, (player_posX, 700))       
                player_posY = 700
                y = 700
        else:
            screen.blit(player.image, (player_posX, 0))
            y = 0
            
        # 캐릭터 움직이기 및 끝에 다다르면 다시 뒤로 가져오기
        flyingEnemy1.randomSpeed()
        flyingEnemy1.check_enemy_position()
        flyingEnemy2.randomSpeed()
        flyingEnemy2.check_enemy_position()
        flyingEnemy3.randomSpeed()
        flyingEnemy3.check_enemy_position()
        walkingEnemy1.randomSpeed()
        walkingEnemy1.check_enemy_position()
        
        # 바뀐 캐릭터들의 좌표값 알아보기
        player_rect = player.get_rect()
        player_rect.left = player_posX
        player_rect.top = player_posY
    
        flyingEnemy1_rect = flyingEnemy1.get_rect()
        flyingEnemy1_rect.left = flyingEnemy1.FlyingEnemy_x
        flyingEnemy1_rect.top = flyingEnemy1.FlyingEnemy_y
        
        flyingEnemy2_rect = flyingEnemy2.get_rect()
        flyingEnemy2_rect.left = flyingEnemy2.FlyingEnemy_x
        flyingEnemy2_rect.top = flyingEnemy2.FlyingEnemy_y\
            
        flyingEnemy3_rect = flyingEnemy3.get_rect()
        flyingEnemy3_rect.left = flyingEnemy3.FlyingEnemy_x
        flyingEnemy3_rect.top = flyingEnemy3.FlyingEnemy_y
        
        walkingEnemy1_rect = walkingEnemy1.get_rect()
        walkingEnemy1_rect.left = walkingEnemy1.WalkingEnemy_x
        walkingEnemy1_rect.top = walkingEnemy1.WalkingEnemy_y
        
        # 주인공과 적의 충돌 감지
        if player_rect.colliderect(flyingEnemy1_rect):
            draw_gameover()
            pygame.display.update()
            pygame.time.delay(2000)
            done = True
        elif player_rect.colliderect(flyingEnemy2_rect):
            draw_gameover()
            pygame.display.update()
            pygame.time.delay(2000)
            done = True            
        elif player_rect.colliderect(flyingEnemy3_rect):
            draw_gameover()
            pygame.display.update()
            pygame.time.delay(2000)
            done = True            
        
        elif player_rect.colliderect(walkingEnemy1_rect):
            draw_gameover()
            pygame.display.update()
            pygame.time.delay(2000)
            done = True
        seconds = (pygame.time.get_ticks()-start_time_count)/1000
        seconds = round(seconds)
        draw_time(seconds)
        pygame.display.flip() # 전체 surface 업데이트 하기
        pygame.display.update()
        
def draw_time(seconds):
    if done == False: # 게임 종료 시 호출 안함
        font_time = pygame.font.SysFont("FixedSsy",50,True,False)
        text_time = font_time.render("Time : " + str(seconds), True, (255,255,255))
        screen.blit(text_time,[30,30])
    
    
    
def moveback():
    global backgorund1_x, background2_x
    backgorund1_x -= 10 #배경화면 움직이는 세기
    background2_x -= 10 #배경화면 움직이는 세기
    if backgorund1_x == -1600 :
        backgorund1_x = 1600
    if background2_x == -1600:
        background2_x = 1600
    screen.blit(background, (backgorund1_x,0))
    screen.blit(background2, (background2_x,0))
    
    
def draw_gameover():
    font1 = pygame.font.SysFont("FixedSsy",150,True,False)
    gameoverscore = font1.render("GameOver",True,(255,0,0))
    text_rect = gameoverscore.get_rect()
    text_rect.centerx = round(screen_width/2)
    text_rect.centery = round(screen_height/2)
    screen.blit(gameoverscore,[text_rect.x,text_rect.y])
runGame()
pygame.quit()

        