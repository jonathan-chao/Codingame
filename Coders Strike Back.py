import sys
import math

# game loop
while True:
    
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]
    
    prevX = next_checkpoint_x
    prevY = next_checkpoint_y
    """
    #velx and vely for velocity
    velX = x - prevX
    velY = y - prevY
   """
   #distance 
   # The checkpoints are circular, with a radius of 600 units.
    if next_checkpoint_dist < 1000: 
        thrust =30
    if next_checkpoint_dist < 650: 
        thrust =19
    else:
        thrust = 100
    
    #angle
    if next_checkpoint_angle > 20 or next_checkpoint_angle < -20:
        thrust = 58
    elif next_checkpoint_angle > 35 or next_checkpoint_angle < -30:
        thrust = 70
    elif next_checkpoint_angle > 45 or next_checkpoint_angle < -40:
        thrust = 80
    elif next_checkpoint_angle > 50 or next_checkpoint_angle < -50:
        thrust = 85
    elif next_checkpoint_angle > 90 or next_checkpoint_angle < -90:
        thrust = 90
    elif next_checkpoint_angle > 180 or next_checkpoint_angle < -180:
        thrust = 10
    
    
    #boost when checkpoint distance is 7000 and angle is 0
    if next_checkpoint_dist > 7000 and next_checkpoint_angle == 0: #( -5 < next_checkpoint_angle < 5):
        thrust = "BOOST"
    
    #shield
    #if next_checkpoint_dist < 500 and next_checkpoint_angle < 35:
     #   thrust = "SHIELD"
       
    print(str(next_checkpoint_x -(x-prevX)*3)+ " " + str(next_checkpoint_y -(y-prevY)*3) + " " + str(thrust))
