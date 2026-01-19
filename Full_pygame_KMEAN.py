

import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((1200, 700))
# #pygame: screen.blit(parameter,x,y coordinate )- block image transfer = paste

pygame.display.set_caption("kmeans visualization")

running = True
clock = pygame.time.Clock()

BACKGROUND = (214, 214, 214)
BLACK = (0, 0, 0)
BACKGROUND_PANEL = (249, 255, 230)
WHITE = (255, 255, 255)

# Cluster Colors
COLORS = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (0, 255, 255),  # Cyan
    (255, 0, 255),  # Magenta
]

# Variables
K = 0
error = 0
points = []
clusters = []
labels = []

# Font Setup
font = pygame.font.SysFont('sans', 40)
text_plus = font.render('+', True, WHITE)
text_minus = font.render('-', True, WHITE)
text_run = font.render("Run", True, WHITE)
text_random = font.render("Random", True, WHITE)
text_algorithm = font.render("Algorithm", True, WHITE)
text_reset = font.render("Reset", True, WHITE)

while running:
    clock.tick(60)
    screen.fill(BACKGROUND)

    # --- DRAW INTERFACE ---
    
    # Draw panel
    pygame.draw.rect(screen, BLACK, (50, 50, 700, 500))
    pygame.draw.rect(screen, BACKGROUND_PANEL, (55, 55, 690, 490))

    # Draw the Points
    for i in range(len(points)):
        # If the point has no cluster (-1), draw it white
        if labels[i] == -1:
            pygame.draw.circle(screen, BLACK, (points[i][0], points[i][1]), 6)
            pygame.draw.circle(screen, WHITE, (points[i][0], points[i][1]), 4)
        else:
            # Color based on cluster label
            pygame.draw.circle(screen, COLORS[labels[i]], (points[i][0], points[i][1]), 6)
            pygame.draw.circle(screen, WHITE, (points[i][0], points[i][1]), 4)

    # Draw the Centroids
    for i in range(len(clusters)):
        pygame.draw.circle(screen, COLORS[i], (int(clusters[i][0]), int(clusters[i][1])), 10)

    # K button + 
    pygame.draw.rect(screen, BLACK, (850, 50, 50, 50))
    screen.blit(text_plus, (860, 50))

    # K button -
    pygame.draw.rect(screen, BLACK, (950, 50, 50, 50))
    screen.blit(text_minus, (960, 50))

    # K value text
    text_k = font.render("K = " + str(K), True, BLACK)
    screen.blit(text_k, (1050, 50))

    # Run button
    pygame.draw.rect(screen, BLACK, (850, 150, 150, 50))
    screen.blit(text_run, (900, 150))

    # Random button
    pygame.draw.rect(screen, BLACK, (850, 250, 150, 50))
    screen.blit(text_random, (850, 250))

    # Reset button
    pygame.draw.rect(screen, BLACK, (850, 550, 150, 50))
    screen.blit(text_reset, (850, 550))  

    # Algorithm button
    pygame.draw.rect(screen, BLACK, (850, 450, 150, 50))
    screen.blit(text_algorithm, (850, 450))  

    # Error text
    text_error = font.render("Error = " + str(int(error)), True, BLACK)
    screen.blit(text_error, (850, 350))

    # --- EVENT HANDLING ---
    
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Create Point in Panel
            if 50 < mouse_x < 750 and 50 < mouse_y < 550:
                labels.append(-1)
                points.append([mouse_x, mouse_y])
                print("Point created at", mouse_x, mouse_y)

            # Change K button +
            if 850 < mouse_x < 900 and 50 < mouse_y < 100:
                if K < 6: # Cap K at 6 because we only have 6 colors
                    K += 1
                print("K +")
            
            # Change K button -
            if 950 < mouse_x < 1000 and 50 < mouse_y < 100:
                if K > 0:
                    K -= 1
                print("K -")

            # Run button (Assign clusters)
            if 850 < mouse_x < 1000 and 150 < mouse_y < 200:
                if len(clusters) == 0:
                    print("Error: No clusters! Press Random first.")
                    continue
                
                error = 0 # Reset error
                for i in range(len(points)):
                    distances = []
                    for c in clusters:
                        # Corrected math formula (using c[1])
                        dis = math.sqrt((points[i][0] - c[0])**2 + (points[i][1] - c[1])**2)
                        distances.append(dis)
                    
                    min_dis = min(distances)
                    labels[i] = distances.index(min_dis) # Corrected variable name
                    error += min_dis
                print("Points assigned to clusters")

            # Random button (Initialize centroids)
            if 850 < mouse_x < 1000 and 250 < mouse_y < 300:
                clusters = []
                for i in range(K):
                    random_x = random.randint(50, 700)
                    random_y = random.randint(50, 500)
                    clusters.append([random_x, random_y])
                print("Random centroids created")

            # Algorithm button (Move centroids)
            if 850 < mouse_x < 1000 and 450 < mouse_y < 500:
                if len(clusters) == 0:
                    print("Error: No clusters initialized.")
                    continue

                for i in range(K):
                    sum_x = 0
                    sum_y = 0
                    count = 0
                    for j in range(len(points)):
                        if labels[j] == i:
                            sum_x += points[j][0]
                            sum_y += points[j][1]
                            count += 1
                    
                    if count != 0:
                        clusters[i] = [sum_x/count, sum_y/count]
                print("Centroids updated")

            # Reset button
            if 850 < mouse_x < 1000 and 550 < mouse_y < 600:
                K = 0
                points = []
                clusters = []
                labels = []
                error = 0
                print("Reset!")

    pygame.display.flip()

pygame.quit()