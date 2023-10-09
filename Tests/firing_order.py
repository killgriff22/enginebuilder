import pygame
import engine_generator
screen = pygame.display.set_mode((700, 500))
running = True
cylinders = [0, 1, 2, 3, 4, 5]  # holds all cylinder numbers
banks = [[0, 1, 2], [3, 4, 5]]  # holds cylinder numbers by bank
Banks = []  # holds the bank objects
offsets = [0, 0]  # holds degree offsets of cylinders
pygame.font.init()
font = pygame.font.SysFont("Arial", 20)
for i, bank in enumerate(banks):
    Banks.append(engine_generator.Bank(bank, offsets[i]))
engine = None
modifying = None
while running:
    cyls = []
    screen.fill((0, 0, 0))
    if not engine:
        for x, bank in enumerate(Banks):
            for y, cylinder in enumerate(bank.cylinders):
                cyls.append(pygame.draw.circle(screen, (255, 255, 255),
                                               (250+(x * 100 + 50), 150+(y * 100 + 50)), 30))
                screen.blit(font.render(f"{cylinders.index(cylinder) if cylinder in cylinders else 'N'}:{cylinder}", True,
                            (0, 0, 0)), (250+(x*100+50), 150+(y*100+50)))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, cylinder in enumerate(cyls):
                if cylinder.collidepoint(event.pos):
                    modifying = i
        if event.type == pygame.KEYDOWN:
            if modifying:
                if event.key >= pygame.K_0 and event.key <= pygame.K_9-(9-(len(cylinders)-1)):
                    cylinders[event.key-pygame.K_0] = modifying
                    modifying = None
                modifying = None
    pygame.display.flip()
