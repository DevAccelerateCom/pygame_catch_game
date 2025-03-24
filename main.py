import pygame, random

# Impostazioni iniziali
pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Catch the Ball")
player = pygame.Rect(200,200,30,30)
ball = pygame.Rect(random.randint(0,370),random.randint(0,370),20,20)
score = 0
font = pygame.font.SysFont(None, 24)
clock = pygame.time.Clock()

# Ciclo del gioco
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # Movimento giocatore
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player.x -= 4
    if keys[pygame.K_RIGHT]: player.x += 4
    if keys[pygame.K_UP]: player.y -= 4
    if keys[pygame.K_DOWN]: player.y += 4
    
    # Limiti schermo
    player.clamp_ip(screen.get_rect())
    
    # Collisione
    if player.colliderect(ball):
        ball.topleft = random.randint(0,370),random.randint(0,370)
        score +=1
    
    # Disegno
    screen.fill("white")
    pygame.draw.rect(screen,"dodgerblue",player)
    pygame.draw.ellipse(screen,"red",ball)
    screen.blit(font.render(f'Score: {score}',True,"black"),(10,10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
