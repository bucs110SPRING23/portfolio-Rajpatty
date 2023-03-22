import pygame

def threenp1(n):
    while not n == 1:
        count = 0
        while n > 1.0:
            count = count + 1
            if n % 2 == 0:
                n = int(n / 2)
            else:
                n = int(3 * n + 1)
        return count

def threenp1range(upper_limit):
    objs_in_sequence = {}
    for i in range(2,upper_limit + 1):
        objs_in_sequence[i] = threenp1(i)
    return objs_in_sequence

def graph_coordinates(threenplus1_iters_dict):
    pygame.init()
    kappa = pygame.display.set_mode()
    pygame.draw.lines(kappa, "mediumspringgreen", False, list(threenplus1_iters_dict.items()))
    tau = list(threenplus1_iters_dict.items())
    max_so_far = 0
    for i in range(len(tau)):
        if (tau[i][1] > max_so_far):
            max_so_far = tau[i][1]
    new_display = pygame.transform.flip(kappa, False, False)
    width, height = new_display.get_size()
    new_display = pygame.transform.scale(new_display, (width * 5, height * 5))
    kappa.blit(new_display, (0, 0))
    font = pygame.font.Font(None,50)
    msg = font.render("The highest value is:" + str(max_so_far), False, "powderblue")
    kappa.blit(msg, (542,370))
    pygame.display.flip()
    pygame.time.wait(4000)

def main():
    print(threenp1range(100))
    graph_coordinates(threenp1range(100))

main()