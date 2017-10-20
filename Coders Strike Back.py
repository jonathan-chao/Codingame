import sys
import math

# game loop
while True:
    
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

   #distance 
   # The checkpoints are circular, with a radius of 600 units.
    if next_checkpoint_dist < 500: 
        thrust =15
    else:
        thrust = 100
    
    #angle
    if next_checkpoint_angle > 90 or next_checkpoint_angle < -90:
        thrust = 0
    #thrust when checkpoint distance is 3000 and angle is 0
    if next_checkpoint_dist > 9000 and next_checkpoint_angle == 0: #( -5 < next_checkpoint_angle < 5):
        thrust = "BOOST"
            
    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + str(thrust))
