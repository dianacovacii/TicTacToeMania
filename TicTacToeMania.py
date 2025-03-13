import pygame, sys
import random
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Tic-Tac-Toe')

font = pygame.font.SysFont("Average", 40, bold=True)
surf = font.render('Quit', True, 'white')
clock = pygame.time.Clock()

available_spots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board = [" "," "," "," "," "," ", " ", " ", " "]

winner = ""

img_o = pygame.image.load("o.png")
img_o = pygame.transform.scale(img_o, (50,68))
img_x =pygame.image.load("x.png")
img_x = pygame.transform.scale(img_x, (50,68))

#o image dimensions 80x98
#x image dimensions 80x98



button_1 = pygame.Rect(87, 87, 75, 75)
button_2 = pygame.Rect(87, 162, 75, 75)
button_3 = pygame.Rect(87, 237, 75, 75)
button_4 = pygame.Rect(162, 87, 75, 75)
button_5 = pygame.Rect(162, 162, 75, 75)
button_6 = pygame.Rect(162, 237, 75, 75)
button_7 = pygame.Rect(237, 87, 75, 75)
button_8 = pygame.Rect(237, 162, 75, 75)
button_9 = pygame.Rect(237, 237, 75, 75)
button_list = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9]

image_olist = []
image_xlist = []

def change_board(board, index, box, char, available_spots):
  board[index] = char
  available_spots.remove(available_spots[box])

def is_winner(board, letter):
    return (board[0]==board[1]==board[2]==letter) or (board[3]==board[4]==board[5]==letter) or (board[6]==board[7]==board[8]==letter) or (board[0]==board[3]==board[6]==letter) or(board[1]==board[4]==board[7]==letter) or (board[2]==board[5]==board[8]==letter) or (board[0]==board[4]==board[8]==letter) or (board[2]==board[4]==board[6]==letter)   

def end_game(winner):
  if winner == 'X':
    print("Game is over. You lost. Better luck next time.")
  elif winner == 'no':
      print ("Game is tied. Better luck next time.")
  else: 
    print("YOU WON!")

def is_tie(board, letter, available_spots):
    return not is_winner(board, letter) and len(available_spots) == 0
  
def computer_move(available_spots, board, button_list, image_xlist):
  
  for letter in ['X', 'O']:
    for i in available_spots: 
      board_copy = board[:]
      board_copy[i-1] = letter
      
      if is_winner(board_copy, letter):
        p = available_spots.index(i)
        image_xlist.append((button_list[p].x, button_list[p].y))
        button_list.remove(button_list[p])
        
        return change_board(board, i-1, p,'X', available_spots)

  open_corners, open_edges = [], []
  
  for i in available_spots: 
    if i in [1, 3, 7, 9]:
      open_corners.append(i)
    
  if len(open_corners) > 0:
    index = random.randint(0, len(open_corners)-1)
    move = open_corners[index]
    p = available_spots.index(move)
    image_xlist.append((button_list[p].x, button_list[p].y))
    button_list.remove(button_list[p])
    
    return change_board(board, move-1, p, 'X',available_spots)
    

  if 5 in available_spots:
    p = available_spots.index(5)
    image_xlist.append(button_list[p].x, button_list[p].y)
    button_list.remove(button_list[p])
    
    return change_board(board, 4, p, 'X', available_spots)
  
  for i in available_spots: 
    if i in [2, 4, 6, 8]:
      open_edges.append(i)

  if len(open_edges) > 0:
    index = random.randint(0, len(open_edges)-1)
    p = available_spots.index(move)
    move = open_edges[index]   
    image_xlist.append(button_list[p].x, button_list[p].y)
    button_list.remove(button_list[p])
    return change_board(board, move-1, p, 'X', available_spots)



def draw_grid():
  pygame.draw.rect(DISPLAYSURF,(52, 67, 122),(87,157,225,10))
  pygame.draw.rect(DISPLAYSURF,(52, 67, 122),(87,230,225,10))
  pygame.draw.rect(DISPLAYSURF,(52, 67, 122),(157,87,10,225))
  pygame.draw.rect(DISPLAYSURF,(52, 67, 122),(230,87,10,225))


while True:
  DISPLAYSURF.fill('light blue')
  for event in pygame.event.get():
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
      
    if event.type == pygame.MOUSEBUTTONDOWN:
      mouse_position = pygame.mouse.get_pos()
        
      for button in button_list: 
        if button.collidepoint(mouse_position):
          p = button_list.index(button)
          image_olist.append((button.x, button.y))
          button_list.remove(button)
          board_box = available_spots[p]
          
          change_board(board, board_box-1, p, "O", available_spots)
          if is_winner(board, 'O'):
            winner = 'O'
            break
          if is_tie(board, 'O', available_spots):
            winner = 'no'
            break
            
          computer_move(available_spots, board, button_list, image_xlist)
          if is_winner(board, 'X'):
            winner = 'X'
            break
          if is_tie(board, 'X', available_spots):
            winner = 'no'
            break

    
        if winner != '':
          end_game(winner)
          pygame.quit()
          sys.exit()
    
  a, b = pygame.mouse.get_pos()
  
  for button in button_list:
    if button.x <= a<= button.x + 75 and button.y <= b <= button.y +75:
      pygame.draw.rect(DISPLAYSURF, (110, 110, 110), button)
    else: 
      pygame.draw.rect(DISPLAYSURF, (185, 217, 231), button)

    for image in image_olist:
        DISPLAYSURF.blit(img_o, (image[0]+10,image[1]))
    for image in image_xlist: 
        DISPLAYSURF.blit(img_x, (image[0]+10,image[1]))

    draw_grid()
    
  pygame.display.update()
  clock.tick(15)