import pygame
import random

def make_number_32_based(number):
    remainder = number % 32
    if remainder == 0:
        return number
    elif remainder <= 16:
        upper = number - remainder
        return upper
    elif remainder > 16:
        lower = number - remainder
        return lower
    else:
        return 0

# Top left (0 ,0), bottom right (608, 480)

def check_mouse_on_mole(click_position, mole_position):
    first_bound_x = mole_position[0]
    first_bound_y = mole_position[1]
    second_bound_x = mole_position[0] + 32
    second_bound_y = mole_position[1] + 32
    if click_position[0] - first_bound_x >= 0 and second_bound_x - click_position[0] >= 0:
        if click_position[1] - first_bound_y >= 0 and second_bound_y - click_position[1] >= 0:
            return True
    return False



def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        vertical_lines, horizontal_lines = 640//32, 512//32
        running = True
        x, y = 0, 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            for i in range(1, vertical_lines + 1):
                pygame.draw.line(screen, (0, 0, 0), ((i * 32), 0), ((i * 32), 512))
            for i in range(1, horizontal_lines + 1):
                pygame.draw.line(screen, (0, 0, 0), (0, (i * 32)), (640, (i * 32)))
            screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))
            mole_spot = (x, y)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = event.pos
                whacked_mole = check_mouse_on_mole(mouse_position, mole_spot)
                if whacked_mole:
                    x = make_number_32_based(random.randint(0, 609))
                    y = make_number_32_based(random.randint(0, 481))
                    print(x)
                    print(y)
                    screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))

            # no mole past this point
            pygame.display.flip()

            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
