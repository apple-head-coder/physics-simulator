import pygame

pygame.init()

window = pygame.display.set_mode((960, 640))

FPS = 60


def tick():
    pass


def draw():
    pass


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        if run:
            tick()
            draw()

    pygame.quit()


if __name__ == "__main__":
    main()
