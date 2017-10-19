import sys
import math

# game loop
while True:
    
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

   #distance 
   # The checkpoints are circular, with a radius of 600 units.
    if next_checkpoint_dist < 600: # how can distance be <15 if its radius is 600? if it will be in 15pix, it won't be nextcp anymore, u will have another cp's distance
        thrust =10
    else:
        thrust = 100
    
    #angle
    if next_checkpoint_angle > 90 or next_checkpoint_angle < -90:
        thrust = 0
    #thrust when checkpoint distance is 3000 and angle is 0
    if next_checkpoint_dist > 7000 and ( -5 < next_checkpoint_angle < 5):
        thrust = "BOOST"
            
    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + str(thrust))
