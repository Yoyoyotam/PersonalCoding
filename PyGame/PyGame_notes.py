


""" To stop keymotion after key is pressed"""
if event.type == pygame.KEYUP:
    if event.key == pygame.K_LEFT:
        lead_x_change = 0
    if event.key == pygame.K_RIGHT:
        lead_x_change = 0
    if event.key == pygame.K_DOWN:
        lead_y_change = 0
    if event.key == pygame.K_UP:
        lead_y_change = 0

""" X / Y movement """
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_LEFT:
        lead_x_change = -10
    if event.key == pygame.K_RIGHT:
        lead_x_change = 10
    if event.key == pygame.K_DOWN:
        lead_y_change = 10
    if event.key == pygame.K_UP:
        lead_y_change = -10

lead_x += lead_x_change
lead_y += lead_y_change
