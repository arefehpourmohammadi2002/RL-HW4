import pygame
import sys

# --- Configuration for 4x12 Grid ---
GRID_ROWS = 4        # 4 Rows (Indices 0 to 3)
GRID_COLS = 12       # 12 Columns (Indices 0 to 11)
CELL_SIZE = 70       
MARGIN = 20          

WINDOW_WIDTH = GRID_COLS * CELL_SIZE + MARGIN * 2
WINDOW_HEIGHT = GRID_ROWS * CELL_SIZE + MARGIN * 2

# Colors (RGB)
BG_COLOR = (15, 15, 15)
GRID_COLOR = (40, 40, 40)
CELL_COLOR = (30, 30, 30)
SPECIAL_CELL_COLOR = (70, 40, 20)  # Muted Crimson/Orange for the bottom middle cells

POLICY_BLUE_COLOR = (0, 150, 255)  
POLICY_RED_COLOR = (255, 50, 50)    

# --- Two Policy Arrays (4x12 Examples) ---
policy_blue = [
    ((0, 0), (0, 1)),
    ((0, 1), (0, 2)),
    ((0, 2), (1, 2)),
    ((1, 2), (1, 3))
]

policy_red = [
    ((0, 0), (1, 0)),
    ((1, 0), (2, 0)),
    ((2, 0), (2, 1))
]

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("4x12 Policy Grid - Cliff Layout")
clock = pygame.time.Clock()

def get_cell_center(row, col):
    """Calculates the center pixel coordinate of a grid cell."""
    x = MARGIN + col * CELL_SIZE + CELL_SIZE // 2
    y = MARGIN + row * CELL_SIZE + CELL_SIZE // 2
    return (x, y)

def draw_grid():
    """Draws the 4x12 grid, giving a different color to bottom-row middle cells."""
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            
            # Check if it's the bottom row (index 3) AND NOT the first (0) or last (11) column
            if row == GRID_ROWS - 1 and col > 0 and col < GRID_COLS - 1:
                current_color = SPECIAL_CELL_COLOR
            else:
                current_color = CELL_COLOR

            rect = pygame.Rect(
                MARGIN + col * CELL_SIZE, 
                MARGIN + row * CELL_SIZE, 
                CELL_SIZE - 4, 
                CELL_SIZE - 4
            )
            pygame.draw.rect(screen, current_color, rect)

def draw_policy_step(start, end, color, offset=(0, 0)):
    """Draws a step line from start cell to end cell with an optional pixel offset."""
    start_pt = get_cell_center(start[0], start[1])
    end_pt = get_cell_center(end[0], end[1])
    
    start_pt = (start_pt[0] + offset[0], start_pt[1] + offset[1])
    end_pt = (end_pt[0] + offset[0], end_pt[1] + offset[1])
    
    pygame.draw.line(screen, color, start_pt, end_pt, width=5)
    pygame.draw.circle(screen, color, end_pt, 6)

# --- Main Loop ---
running = True
while running:
    screen.fill(BG_COLOR)
    draw_grid()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw Blue Policy Steps
    for start, end in policy_blue:
        draw_policy_step(start, end, POLICY_BLUE_COLOR, offset=(-4, -4))
        
    # Draw Red Policy Steps
    for start, end in policy_red:
        draw_policy_step(start, end, POLICY_RED_COLOR, offset=(4, 4))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()