import asyncio
import pygame, sys
pygame.init()
screen = pygame.display.set_mode((552, 900))
clock = pygame.time.Clock()
TIMER_EVENT = pygame.USEREVENT
pygame.time.set_timer(TIMER_EVENT, 1000)
n = 3


async def main():
    a, b, c = 0, 0, 0
    image = pygame.image.load('timer.jpg')
    font = pygame.font.SysFont('', 200)
    while True:
        await asyncio.sleep(0)
        screen.blit(image, (0, 0))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == TIMER_EVENT:
                c += 1
                if c == n:
                    c = 0
                    b += 1
                    if b == n:
                        b = 0
                        a += 1
                        if a == n:
                            a, b, c = 0, 0, 0
        screen.blit(font.render(str(a), True, (0, 0, 0)), (50, 710))
        screen.blit(font.render(str(b), True, (0, 0, 0)), (175, 710))
        screen.blit(font.render(str(c), True, (0, 0, 0)), (300, 710))
        pygame.display.update()
        clock.tick(30)


if __name__ == '__main__':
    asyncio.run(main())
