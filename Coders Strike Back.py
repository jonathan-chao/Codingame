import sys
turn=0
x = 0
y = 0
# game loop
while True:
    
    prevX = x
    prevY = y

    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]
    
    if prevX == 0:
        prevX = x
        prevY = y

    
    """
    #velx and vely for velocity
    velX = x - prevX
    velY = y - prevY
   """
   #distance 
   # The checkpoints are circular, with a radius of 600 units.
    if next_checkpoint_dist < 1500: 
        thrust =30
    if next_checkpoint_dist < 650: 
        thrust =19
    else:
        thrust = 100
    
    #angle
    # if next_checkpoint_angle > 20 or next_checkpoint_angle < -20:
    #     thrust = 58
    # elif next_checkpoint_angle > 35 or next_checkpoint_angle < -30:
    #     thrust = 70
    # elif next_checkpoint_angle > 45 or next_checkpoint_angle < -40:
    #     thrust = 80
    # elif next_checkpoint_angle > 50 or next_checkpoint_angle < -50:
    #     thrust = 100
    if abs(next_checkpoint_angle) > 90:
        thrust = 0
    # elif next_checkpoint_angle > 180 or next_checkpoint_angle < -180: # do u understand that there're only 360 angles? and if it's [-180...180] then it can't be >180 or <-180
    #     thrust = 10
    
    if abs(next_checkpoint_angle) < 50 and next_checkpoint_dist<2600 and ((next_checkpoint_x-8000)**2+(next_checkpoint_y-4500)**2)**0.5>3000:
        next_checkpoint_x = 9000
        next_checkpoint_y = 4500
        thrust = 30
    
    
    #boost when checkpoint distance is 7000 and angle is 0
    if next_checkpoint_dist > 7000 and next_checkpoint_angle == 0: #( -5 < next_checkpoint_angle < 5):
        thrust = "BOOST"
    
    if turn==0:
        thrust=0
    #shield
    #if next_checkpoint_dist < 500 and next_checkpoint_angle < 35:
     #   thrust = "SHIELD"
       
    print(str(next_checkpoint_x -(x-prevX)*3)+ " " + str(next_checkpoint_y -(y-prevY)*3) + " " + str(thrust))
    turn+=1
