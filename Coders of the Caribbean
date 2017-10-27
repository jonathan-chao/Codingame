############################################### Some Code was taking from iannase ########################################################
import sys
import math
import random

z=0

# GAME LOOP -------------------------------------------------------------------------------------------------

while True:

    # MY VARIABLES AND ARRAYS ------------------------------------------------------------------------------

    futureX=0
    futureY=0
    d1=0
    d2=0
    futureCubeX=0
    futureCubeY=0
    futureCubeZ=0
    barrelX,barrelY,barrelCubeX,barrelCubeY,barrelCubeZ,rumInBarrel = [],[],[],[],[],[]
    shipX,shipY,shipCubeX,shipCubeY,shipCubeZ,shipDirection,shipSpeed,shipHealth = [],[],[],[],[],[],[],[]
    enemyShipX,enemyShipY,enemyShipCubeX,enemyShipCubeY,enemyShipCubeZ,enemyShipSpeed,enemyShipDirection, enemyShipHealth = [],[],[],[],[],[],[],[]
    mineX,mineY,mineCubeX,mineCubeY,mineCubeZ = [],[],[],[],[]
    cannonX,cannonY,cannonCubeX,cannonCubeY,cannonCubeZ = [],[],[],[],[]
    futureEnemyXArray,futureEnemyYArray = [],[]
    barrelIndexArray = []
    steer = ""
    mineAlreadyHitX,mineAlreadyHitY=[],[]
    randomTurn=0

    # INPUT ------------------------------------------------------------------------------

    my_ship_count = int(input())
    entity_count = int(input())

    for i in range(entity_count):
        entity_id, entity_type, x, y, arg_1, arg_2, arg_3, arg_4 = input().split()

        # END INPUT ------------------------------------------------------------------------------

        # VARIABLES ------------------------------------------------------------------------------

        entity_id = int(entity_id)
        x = int(x)
        y = int(y)
        arg_1 = int(arg_1)
        arg_2 = int(arg_2)
        arg_3 = int(arg_3)
        arg_4 = int(arg_4)
        cubeX = int(x - (y - (y & 1)) / 2)
        cubeZ = int(y)
        cubeY = int( - cubeX - cubeZ)

        # MY SHIPS ------------------------------------------------------------------------------

        if entity_type == "SHIP" and arg_4 == 1:
            shipX.append(x)
            shipY.append(y)
            shipCubeX.append(cubeX)
            shipCubeY.append(cubeY)
            shipCubeZ.append(cubeZ)
            shipSpeed.append(arg_2)
            shipDirection.append(arg_1)
            shipHealth.append(arg_3)


        # MINES ------------------------------------------------------------------------------

        if entity_type == "MINE":
            mineX.append(x)
            mineY.append(y)
            mineCubeX.append(cubeX)
            mineCubeY.append(cubeY)
            mineCubeZ.append(cubeZ)

        # CANNONBALLS ------------------------------------------------------------------------------

        if entity_type == "CANNONBALL":
            cannonX.append(x)
            cannonY.append(y)
            cannonCubeX.append(cubeX)
            cannonCubeY.append(cubeY)
            cannonCubeZ.append(cubeZ)

        # ENEMY SHIPS ------------------------------------------------------------------------------

        if entity_type == "SHIP" and arg_4 == 0:
            enemyShipX.append(x)
            enemyShipY.append(y)
            enemyShipCubeX.append(cubeX)
            enemyShipCubeY.append(cubeY)
            enemyShipCubeZ.append(cubeZ)
            enemyShipSpeed.append(arg_2)
            enemyShipDirection.append(arg_1)
            enemyShipHealth.append(arg_3)

        # BARRELS ------------------------------------------------------------------------------

        if entity_type == "BARREL":
            barrelX.append(x)
            barrelY.append(y)
            barrelCubeX.append(cubeX)
            barrelCubeY.append(cubeY)
            barrelCubeZ.append(cubeZ)
            rumInBarrel.append(arg_1)

    # VARIABLES ------------------------------------------------------------------------------
    steer="STARBOARD"
    maxSpeed=1
    doNothing="WAIT"

    # DISTANCES AHEAD ------------------------------------------------------------------------------

    def ahead(howMany,enemyIndex):

        rotation = enemyShipDirection[enemyIndex]
        futureEnemyCubeX = futureEnemyCubeY = futureEnemyCubeZ = 0

        if rotation == 0:
            futureEnemyCubeX = enemyShipCubeX[enemyIndex] + howMany
            futureEnemyCubeY = enemyShipCubeY[enemyIndex] - howMany
            futureEnemyCubeZ = enemyShipCubeZ[enemyIndex]

        if rotation == 3:
            futureEnemyCubeX = enemyShipCubeX[enemyIndex] - howMany
            futureEnemyCubeY = enemyShipCubeY[enemyIndex] + howMany
            futureEnemyCubeZ = enemyShipCubeZ[enemyIndex]

        if rotation == 1:
            futureEnemyCubeX = enemyShipCubeX[enemyIndex] + howMany
            futureEnemyCubeY = enemyShipCubeY[enemyIndex]
            futureEnemyCubeZ = enemyShipCubeZ[enemyIndex] - howMany

        if rotation == 2:
            futureEnemyCubeX = enemyShipCubeX[enemyIndex]
            futureEnemyCubeY = enemyShipCubeY[enemyIndex] + howMany
            futureEnemyCubeZ = enemyShipCubeZ[enemyIndex] - howMany

        if rotation == 4:
            futureEnemyCubeX = enemyShipCubeX[enemyIndex] - howMany
            futureEnemyCubeY = enemyShipCubeY[enemyIndex]
            futureEnemyCubeZ = enemyShipCubeZ[enemyIndex] + howMany

        if rotation == 5:
            futureEnemyCubeX = enemyShipCubeX[enemyIndex]
            futureEnemyCubeY = enemyShipCubeY[enemyIndex] - howMany
            futureEnemyCubeZ = enemyShipCubeZ[enemyIndex] + howMany

        futureEnemyX = int(futureEnemyCubeX + (futureEnemyCubeZ - (futureEnemyCubeZ & 1)) / 2)
        futureEnemyY=int(futureEnemyCubeZ)

        if futureEnemyX < 0:
            futureEnemyX += howMany

        if futureEnemyY < 0:
            futureEnemyY += howMany

        return futureEnemyX, futureEnemyY, futureEnemyCubeX, futureEnemyCubeY, futureEnemyCubeZ

    # NOT FACING A WALL ------------------------------------------------------------------------------

    def notFacingWall(ship):

        if shipX[ship]==0 and shipY[ship] != 0 and shipY[ship] != 20:

            if shipDirection[ship] == 1 or shipDirection[ship] == 0 or shipDirection[ship] == 5:
                return True

        if shipX[ship]==22 and shipY[ship] != 0 and shipY[ship] != 20:

            if shipDirection[ship] == 2 or shipDirection[ship] == 3 or shipDirection[ship] == 4:
                return True

        if shipY[ship]==0 and shipX[ship] != 0 and shipX[ship] != 22:

            if shipDirection[ship] == 4 or shipDirection[ship] == 5 or shipDirection[ship] == 0:
                return True

        if shipY[ship]==20 and shipX[ship] != 0 and shipX[ship] != 22:

            if shipDirection[ship] == 1 or shipDirection[ship] == 2 or shipDirection[ship] == 3:
                return True

        if shipX[ship] != 0 and shipX[ship] != 22 and shipY[ship] != 0 and shipY[ship] != 20:

            return True

        return False

    # NOT ON THE WALL ------------------------------------------------------------------------------

    def notOnTheWall(ship):

        if shipX[ship] == 0 or shipY[ship] == 0 or shipX[ship] == 22 or shipY[ship] == 20:
            return True

        return False

    # TURN TOWARDS BARREL STARBOARD SIDE -------------------------------------------------------------------------

    def TurnTowardsBarrelStarboard(ship,speed):

        for i in range(len(barrelCubeX)):

            # Y-PLANE: 1 and 4 # X-PLANE: 2 and 5 # Z-PLANE: 0 and 3

            if shipSpeed[ship] == 0:
                return False

            if shipDirection[ship] == 0 and shipCubeZ[ship] < barrelCubeZ[i] and shipCubeX[ship]+(1*speed) == barrelCubeX[i]:
                return True

            if shipDirection[ship] == 1 and shipCubeY[ship] > barrelCubeY[i] and shipCubeZ[ship]-(1*speed) == barrelCubeZ[i]:
                return True

            if shipDirection[ship] == 2 and shipCubeX[ship] < barrelCubeX[i] and shipCubeY[ship]+(1*speed) == barrelCubeY[i]:
                return True

            if shipDirection[ship] == 3 and shipCubeZ[ship] > barrelCubeZ[i] and shipCubeX[ship]-(1*speed) == barrelCubeX[i]:
                return True

            if shipDirection[ship] == 4 and shipCubeY[ship] < barrelCubeY[i] and shipCubeZ[ship]+(1*speed) == barrelCubeZ[i]:
                return True

            if shipDirection[ship] == 5 and shipCubeX[ship] > barrelCubeX[i] and shipCubeY[ship]-(1*speed) == barrelCubeY[i]:
                return True

        return False

    # TURN TOWARDS BARREL PORT SIDE ------------------------------------------------------------------------------

    def TurnTowardsBarrelPort(ship,speed):

        for i in range(len(barrelCubeX)):

            # Y-PLANE: 1 and 4 # X-PLANE: 2 and 5 # Z-PLANE: 0 and 3

            if shipSpeed[ship] == 0:
                return False

            if shipDirection[ship] == 0 and shipCubeZ[ship] > barrelCubeZ[i] and shipCubeY[ship]-(1*speed) == barrelCubeY[i]:
                return True

            if shipDirection[ship] == 1 and shipCubeY[ship] < barrelCubeY[i] and shipCubeX[ship]+(1*speed) == barrelCubeX[i]:
                return True

            if shipDirection[ship] == 2 and shipCubeX[ship] > barrelCubeX[i] and shipCubeZ[ship]-(1*speed) == barrelCubeZ[i]:
                return True

            if shipDirection[ship] == 3 and shipCubeZ[ship] < barrelCubeZ[i] and shipCubeY[ship]+(1*speed) == barrelCubeY[i]:
                return True

            if shipDirection[ship] == 4 and shipCubeY[ship] > barrelCubeY[i] and shipCubeX[ship]-(1*speed) == barrelCubeX[i]:
                return True

            if shipDirection[ship] == 5 and shipCubeX[ship] < barrelCubeX[i] and shipCubeZ[ship]+(1*speed) == barrelCubeZ[i]:
                return True

        return False

    # STUCK IN A CORNER ------------------------------------------------------------------------------

    def stuckInCorner(ship):

        if shipX[ship] == 0 and shipY[ship] == 20:
            return True

        if shipX[ship] == 22 and shipY[ship] == 0:
            return True

        if shipX[ship] == 0 and shipY[ship] == 0:
            return True

        if shipX[ship] == 22 and shipY[ship] == 20:
            return True

    # BARREL AHEAD ------------------------------------------------------------------------------

    def barrelAhead(ship):

        for i in range(len(barrelCubeX)):

            # Y-PLANE: 1 and 4 # X-PLANE: 2 and 5 # Z-PLANE: 0 and 3

            if shipSpeed[ship] == 0:
                return False

            if shipDirection[ship] == 0 and shipCubeZ[ship] == barrelCubeZ[i] and shipCubeY[ship] > barrelCubeY[i] and shipCubeX[ship] < barrelCubeX[i]:
                return True

            if shipDirection[ship] == 1 and shipCubeY[ship] == barrelCubeY[i] and shipCubeX[ship] < barrelCubeX[i] and shipCubeZ[ship] > barrelCubeZ[i]:
                return True

            if shipDirection[ship] == 2 and shipCubeX[ship] == barrelCubeX[i] and shipCubeY[ship] < barrelCubeY[i] and shipCubeZ[ship] > barrelCubeZ[i]:
                return True

            if shipDirection[ship] == 3 and shipCubeZ[ship] == barrelCubeZ[i] and shipCubeY[ship] < barrelCubeY[i] and shipCubeX[ship] > barrelCubeX[i]:
                return True

            if shipDirection[ship] == 4 and shipCubeY[ship] == barrelCubeY[i] and shipCubeZ[ship] < barrelCubeY[i] and shipCubeX[ship] > barrelCubeX[i]:
                return True

            if shipDirection[ship] == 5 and shipCubeX[ship] == barrelCubeX[i] and shipCubeY[ship] > barrelCubeY[i] and shipCubeZ[ship] < barrelCubeZ[i]:
                return True

        return False

    # CLOSEST BARREL ------------------------------------------------------------------------------

    def closestBarrel(ship):

        lowestDistance = 1000

        for i in range(len(barrelX)):

            d = int((abs(shipCubeX[ship]-barrelCubeX[i])+abs(shipCubeY[ship]-barrelCubeY[i])+abs(shipCubeZ[ship]-barrelCubeZ[i]))/2)

            if d < lowestDistance:
                lowestDistance = d
                index = i

        closestX = barrelX[index]
        closestY = barrelY[index]

        return closestX, closestY

    # DONT SHOOT A MINE TWICE ------------------------------------------------------------------------------

    def alreadyShot():

        for i in range(len(cannonX)):

            if mineX[0] == cannonX[i] and mineY[0] == cannonY[i]:
                return True

        return False

    # CLOSEST CORNER OF THE MAP ------------------------------------------------------------------------------

    def closestCorner(ship):

        if shipX[ship] < 11 and shipY[ship] < 10:
            return 2,2

        if shipX[ship] < 11 and shipY[ship] >= 10:
            return 2,18

        if shipX[ship] >= 11 and shipY[ship] < 10:
            return 1,21

        if shipX[ship] >= 11 and shipY[ship] >= 10:
            return 21,19

    # MINE ------------------------------------------------------------------------------

    def mineAhead(ship):
        for i in range(len(mineCubeX)):
            # Y-PLANE: 1 and 4 # X-PLANE: 2 and 5 # Z-PLANE: 0 and 3
            if shipSpeed[ship] == 0:
                return False

            if shipDirection[ship] == 0 and shipCubeZ[ship] == mineCubeZ[i] and shipCubeY[ship] > mineCubeY[i] and shipCubeX[ship] < mineCubeX[i]:
                return True
            if shipDirection[ship] == 1 and shipCubeY[ship] == mineCubeY[i] and shipCubeX[ship] < mineCubeX[i] and shipCubeZ[ship] > mineCubeZ[i]:
                return True
            if shipDirection[ship] == 2 and shipCubeX[ship] == mineCubeX[i] and shipCubeY[ship] < mineCubeY[i] and shipCubeZ[ship] > mineCubeZ[i]:
                return True
            if shipDirection[ship] == 3 and shipCubeZ[ship] == mineCubeZ[i] and shipCubeY[ship] < mineCubeY[i] and shipCubeX[ship] > mineCubeX[i]:
                return True
            if shipDirection[ship] == 4 and shipCubeY[ship] == mineCubeY[i] and shipCubeZ[ship] < mineCubeY[i] and shipCubeX[ship] > mineCubeX[i]:
                return True
            if shipDirection[ship] == 5 and shipCubeX[ship] == mineCubeX[i] and shipCubeY[ship] > mineCubeY[i] and shipCubeZ[ship] < mineCubeZ[i]:
                return True
        return False

    # CANNONBALL AHOY ------------------------------------------------------------------------------

    def cannonballAhead(ship):

        for i in range(len(cannonCubeX)):

            # Y-PLANE: 1 and 4 # X-PLANE: 2 and 5 # Z-PLANE: 0 and 3

            if shipDirection[ship] == 0 and shipCubeZ[ship] == cannonCubeZ[i]:
                return True

            if shipDirection[ship] == 1 and shipCubeY[ship] == cannonCubeY[i]:
                return True

            if shipDirection[ship] == 2 and shipCubeX[ship] == cannonCubeX[i]:
                return True

            if shipDirection[ship] == 3 and shipCubeZ[ship] == cannonCubeZ[i]:
                return True

            if shipDirection[ship] == 4 and shipCubeY[ship] == cannonCubeY[i]:
                return True

            if shipDirection[ship] == 5 and shipCubeX[ship] == cannonCubeX[i]:
                return True

        return False

    # DONT TURN INTO THAT MINE ------------------------------------------------------------------------------

    def minePreventionSystem(ship):

        for i in range(len(mineCubeX)):

            # Y-PLANE: 1 and 4 # X-PLANE: 2 and 5 # Z-PLANE: 0 and 3

            if shipDirection[ship] == 0 and shipCubeZ[ship] < mineCubeZ[i] and shipCubeX[ship]+(1*speed) == mineCubeX[i]:
                return True

            if shipDirection[ship] == 1 and shipCubeY[ship] > mineCubeY[i] and shipCubeZ[ship]-(1*speed) == mineCubeZ[i]:
                return True

            if shipDirection[ship] == 2 and shipCubeX[ship] < mineCubeX[i] and shipCubeY[ship]+(1*speed) == mineCubeY[i]:
                return True

            if shipDirection[ship] == 3 and shipCubeZ[ship] > mineCubeZ[i] and shipCubeX[ship]-(1*speed) == mineCubeX[i]:
                return True

            if shipDirection[ship] == 4 and shipCubeY[ship] < mineCubeY[i] and shipCubeZ[ship]+(1*speed) == mineCubeZ[i]:
                return True

            if shipDirection[ship] == 5 and shipCubeX[ship] > mineCubeX[i] and shipCubeY[ship]-(1*speed) == mineCubeY[i]:
                return True

            if shipDirection[ship] == 0 and shipCubeZ[ship]-1 == mineCubeZ[i] and shipCubeX[ship]+(1*speed) == mineCubeX[i]:
                return True

            if shipDirection[ship] == 1 and shipCubeY[ship]+1 == mineCubeY[i] and shipCubeZ[ship]-(1*speed) == mineCubeZ[i]:
                return True

            if shipDirection[ship] == 2 and shipCubeX[ship]-1 == mineCubeX[i] and shipCubeY[ship]+(1*speed) == mineCubeY[i]:
                return True

            if shipDirection[ship] == 3 and shipCubeZ[ship]+1 == mineCubeZ[i] and shipCubeX[ship]-(1*speed) == mineCubeX[i]:
                return True

            if shipDirection[ship] == 4 and shipCubeY[ship]-1 == mineCubeY[i] and shipCubeZ[ship]+(1*speed) == mineCubeZ[i]:
                return True

            if shipDirection[ship] == 5 and shipCubeX[ship]+1 == mineCubeX[i] and shipCubeY[ship]-(1*speed) == mineCubeY[i]:
                return True

        return False

    # CHECK IF A SHIP IS IN FRONT OF YOU ------------------------------------------------------------------------

    def noShipAhead(ship):

        for i in range(len(enemyShipX)):

            # Y-PLANE: 1 and 4 # X-PLANE: 2 and 5 # Z-PLANE: 0 and 3

            if shipDirection[ship] == 0 and shipCubeZ[ship] == enemyShipCubeZ[i] and shipCubeY[ship] > enemyShipCubeY[i] and shipCubeX[ship] < enemyShipCubeX[i]:
                return False

            if shipDirection[ship] == 1 and shipCubeY[ship] == enemyShipCubeY[i] and shipCubeX[ship] < enemyShipCubeX[i] and shipCubeZ[ship] > enemyShipCubeZ[i]:
                return False

            if shipDirection[ship] == 2 and shipCubeX[ship] == enemyShipCubeX[i] and shipCubeY[ship] < enemyShipCubeY[i] and shipCubeZ[ship] > enemyShipCubeZ[i]:
                return False

            if shipDirection[ship] == 3 and shipCubeZ[ship] == enemyShipCubeZ[i] and shipCubeY[ship] < enemyShipCubeY[i] and shipCubeX[ship] > enemyShipCubeX[i]:
                return False

            if shipDirection[ship] == 4 and shipCubeY[ship] == enemyShipCubeY[i] and shipCubeZ[ship] < enemyShipCubeY[i] and shipCubeX[ship] > enemyShipCubeX[i]:
                return False

            if shipDirection[ship] == 5 and shipCubeX[ship] == enemyShipCubeX[i] and shipCubeY[ship] > enemyShipCubeY[i] and shipCubeZ[ship] < enemyShipCubeZ[i]:
                return False

        return True

    # REDIRECT ------------------------------------------------------------------------------

    def redirect(index):

        #right

        if shipX[index] >= 19 and shipDirection[index] == 0:
            return True

        elif shipX[index] >= 19 and shipDirection[index] == 1:
            return True

        elif shipX[index] >= 19 and shipDirection[index] == 5:
            return True

        #left

        elif shipX[index] <= 4 and shipDirection[index] == 2:
            return True

        elif shipX[index] <= 4 and shipDirection[index] == 3:
            return True

        elif shipX[index] <= 4 and shipDirection[index] == 4:
            return True

        #top

        elif shipY[index] <= 4 and shipDirection[index] == 1:
            return True

        elif shipY[index] <= 4 and shipDirection[index] == 2:
            return True

        #bottom

        elif shipY[index] >= 17 and shipDirection[index] == 4:
            return True

        elif shipY[index] >= 17 and shipDirection[index] == 5:
            return True

        return False

    # MY MOVES ------------------------------------------------------------------------------

    for i in range(my_ship_count):

        d2=20
        d3=20

        # SHIP 1 ###### SHIP 1 ############### SHIP 1 #######################################################

        if i == 0 or len(enemyShipX) == 1:
            d = int((abs(shipCubeX[0]-enemyShipCubeX[0])+abs(shipCubeY[0]-enemyShipCubeY[0])+abs(shipCubeZ[0]-enemyShipCubeZ[0]))/2)

            speed=enemyShipSpeed[0]
            mySpeed=shipSpeed[0]

            if i == 1:
                d = int((abs(shipCubeX[1]-enemyShipCubeX[0])+abs(shipCubeY[1]-enemyShipCubeY[0])+abs(shipCubeZ[1]-enemyShipCubeZ[0]))/2)

            if i == 2:
                d = int((abs(shipCubeX[2]-enemyShipCubeX[0])+abs(shipCubeY[2]-enemyShipCubeY[0])+abs(shipCubeZ[2]-enemyShipCubeZ[0]))/2)

            aheadxx=round(speed*(1+d/3))

            futureX,futureY,futureCubeX,futureCubeY,futureCubeZ=ahead(aheadxx,0)

            d2 = int((abs(shipCubeX[0]-futureCubeX)+abs(shipCubeY[0]-futureCubeY)+abs(shipCubeZ[0]-futureCubeZ))/2)

            if i == 1:
                d2 = int((abs(shipCubeX[1]-futureCubeX)+abs(shipCubeY[1]-futureCubeY)+abs(shipCubeZ[1]-futureCubeZ))/2)

            if i == 2:
                d2 = int((abs(shipCubeX[2]-futureCubeX)+abs(shipCubeY[2]-futureCubeY)+abs(shipCubeZ[2]-futureCubeZ))/2)


            if i == 0:
                if cannonballAhead(0) and mySpeed != 0:
                    print("STARBOARD")
                    continue

                elif z%2==0 and d <= 5 and speed == 0:
                    print("FIRE", futureX, futureY)
                    continue

                elif z < maxSpeed or mySpeed < maxSpeed and notFacingWall(0):
                    print("FASTER")
                    continue

                elif barrelAhead(0) and mySpeed != 2:
                    print("FASTER")
                    continue

                elif not barrelAhead(0) and mySpeed == 2:
                    print("SLOWER")
                    continue

                elif mineAhead(0):
                    print("STARBOARD")
                    continue

                elif minePreventionSystem(0):
                    print("WAIT")
                    continue

                elif TurnTowardsBarrelStarboard(0, mySpeed) and mySpeed != 2:
                    print("STARBOARD")
                    continue

                elif TurnTowardsBarrelPort(0, mySpeed) and mySpeed != 2:
                    print("PORT")
                    continue

                elif len(mineX) != 0 and z%2 == 0 and not alreadyShot():
                    print("FIRE", mineX[0], mineY[0])
                    continue

                elif z%2==0 and len(barrelX) < 3 and d2 <= 10:
                    print("FIRE", futureX, futureY)
                    continue

                elif redirect(0) and len(barrelX) < 1:
                    print("STARBOARD")
                    continue

                elif len(barrelX) >= 1 and mySpeed != 2:
                    closestX, closestY = closestBarrel(0)
                    print("MOVE", closestX, closestY)
                    continue

                elif len(barrelX) < 1 and mySpeed != 2:
                    print("MOVE", enemyShipX[0], enemyShipY[0])
                    continue

                elif stuckInCorner(0):
                    print("FASTER")
                    continue

                else:
                    print("WAIT")
                    continue

            if i == 1:
                if cannonballAhead(1) and mySpeed != 0:
                    print("STARBOARD")
                    continue

                elif z%2==0 and d <= 5 and speed == 0:
                    print("FIRE", futureX, futureY)
                    continue

                elif z < maxSpeed or mySpeed < maxSpeed and notFacingWall(1):
                    print("FASTER")
                    continue

                elif barrelAhead(1) and mySpeed != 2:
                    print("FASTER")
                    continue

                elif not barrelAhead(1) and mySpeed == 2:
                    print("SLOWER")
                    continue

                elif mineAhead(1):
                    print("STARBOARD")
                    continue

                elif minePreventionSystem(1):
                    print("WAIT")
                    continue

                elif TurnTowardsBarrelStarboard(1, mySpeed) and mySpeed != 2:
                    print("STARBOARD")
                    continue

                elif TurnTowardsBarrelPort(1, mySpeed) and mySpeed != 2:
                    print("PORT")
                    continue

                elif len(mineX) != 0 and z%2 == 0 and not alreadyShot():
                    print("FIRE", mineX[0], mineY[0])
                    continue

                elif z%2==0 and len(barrelX) < 3 and d2 <= 10:
                    print("FIRE", futureX, futureY)
                    continue

                elif redirect(1) and len(barrelX) < 1:
                    print("STARBOARD")
                    continue

                elif len(barrelX) >= 1 and mySpeed != 2:
                    closestX, closestY = closestBarrel(1)
                    print("MOVE", closestX, closestY)
                    continue

                elif len(barrelX) < 1 and mySpeed != 2:
                    print("MOVE", enemyShipX[0], enemyShipY[0])
                    continue

                elif stuckInCorner(1):
                    print("FASTER")
                    continue

                else:
                    print("WAIT")
                    continue


            if i == 2:
                if cannonballAhead(2) and mySpeed != 0:
                    print("STARBOARD")
                    continue

                elif len(barrelX) < 1 and d > 15 and enemyShipHealth[0] < shipHealth[2]:
                    print("SLOWER")
                    continue

                elif z%2==0 and d <= 5 and speed == 0:
                    print("FIRE", futureX, futureY)
                    continue

                elif z < maxSpeed or mySpeed < maxSpeed and notFacingWall(2):
                    print("FASTER")
                    continue

                elif barrelAhead(2) and mySpeed != 2:
                    print("FASTER")
                    continue

                elif not barrelAhead(2) and mySpeed == 2:
                    print("SLOWER")
                    continue

                elif mineAhead(2):
                    print("STARBOARD")
                    continue

                elif minePreventionSystem(2):
                    print("WAIT")
                    continue

                elif TurnTowardsBarrelStarboard(2, mySpeed) and mySpeed != 2:
                    print("STARBOARD")
                    continue

                elif TurnTowardsBarrelPort(2, mySpeed) and mySpeed != 2:
                    print("PORT")
                    continue

                elif len(mineX) != 0 and z%2 == 0 and not alreadyShot():
                    print("FIRE", mineX[0], mineY[0])
                    continue

                elif z%2==0 and len(barrelX) < 3 and d2 <= 10:
                    print("FIRE", futureX, futureY)
                    continue

                elif redirect(2) and len(barrelX) < 1:
                    print("STARBOARD")
                    continue

                elif len(barrelX) >= 1 and mySpeed != 2:
                    closestX, closestY = closestBarrel(2)
                    print("MOVE", closestX, closestY)
                    continue

                elif len(barrelX) < 3 and mySpeed != 2:
                    print("MOVE", enemyShipX[0], enemyShipY[0])
                    continue

                elif stuckInCorner(2):
                    print("FASTER")
                    continue

                else:
                    print("WAIT")
                    continue

        # SHIP 2 ################## SHIP 2 ############################## SHIP 2 ############################

        if i == 1 or len(enemyShipX)==2:

            d = int((abs(shipCubeX[1] - enemyShipCubeX[1]) + abs(shipCubeY[1] - enemyShipCubeY[1]) + abs(shipCubeZ[1] - enemyShipCubeZ[1])) / 2)
            speed = enemyShipSpeed[1]
            mySpeed = shipSpeed[1]

            if i == 2:
                d = int((abs(shipCubeX[2]-enemyShipCubeX[0])+abs(shipCubeY[2]-enemyShipCubeY[0])+abs(shipCubeZ[2]-enemyShipCubeZ[0]))/2)

            aheadxx = round(speed * ( 1 + d / 3))

            futureX,futureY,futureCubeX,futureCubeY,futureCubeZ=ahead(aheadxx,1)

            d2 = int((abs(shipCubeX[1]-futureCubeX)+abs(shipCubeY[1]-futureCubeY)+abs(shipCubeZ[1]-futureCubeZ))/2)

            if i == 2:
                d2 = int((abs(shipCubeX[2]-futureCubeX)+abs(shipCubeY[2]-futureCubeY)+abs(shipCubeZ[2]-futureCubeZ))/2)

            if i == 1:
                if cannonballAhead(1) and mySpeed != 0:
                    print("STARBOARD")
                    continue

                elif z%2==0 and d <= 5 and speed == 0:
                    print("FIRE", futureX, futureY)
                    continue

                elif z < maxSpeed or mySpeed < maxSpeed and notFacingWall(1):
                    print("FASTER")
                    continue

                elif barrelAhead(1) and mySpeed != 2:
                    print("FASTER")
                    continue

                elif not barrelAhead(1) and mySpeed == 2:
                    print("SLOWER")
                    continue

                elif mineAhead(1):
                    print("STARBOARD")
                    continue

                elif minePreventionSystem(1):
                    print("WAIT")
                    continue

                elif TurnTowardsBarrelStarboard(1, mySpeed) and mySpeed != 2:
                    print("STARBOARD")
                    continue

                elif TurnTowardsBarrelPort(1, mySpeed) and mySpeed != 2:
                    print("PORT")
                    continue

                elif len(mineX) != 0 and z%2 == 0 and not alreadyShot():
                    print("FIRE", mineX[0], mineY[0])
                    continue

                elif z%2==0 and len(barrelX) < 3 and d2 <= 10:
                    print("FIRE", futureX, futureY)
                    continue

                elif redirect(1) and len(barrelX) < 1:
                    print("STARBOARD")
                    continue

                elif len(barrelX) >= 1 and mySpeed != 2:
                    closestX, closestY = closestBarrel(1)
                    print("MOVE", closestX, closestY)
                    continue

                elif len(barrelX) < 1 and mySpeed != 2:
                    print("MOVE", enemyShipX[0], enemyShipY[0])
                    continue

                elif stuckInCorner(1):
                    print("FASTER")
                    continue

                else:
                    print("WAIT")
                    continue

            # TWO ENEMIES, MY THIRD SHIP

            if i == 2:
                if cannonballAhead(2) and mySpeed != 0:
                    print("STARBOARD")
                    continue

                elif z%2==0 and d <= 5 and speed == 0:
                    print("FIRE", futureX, futureY)
                    continue

                elif z < maxSpeed or mySpeed < maxSpeed and notFacingWall(2):
                    print("FASTER")
                    continue

                elif barrelAhead(2) and mySpeed != 2:
                    print("FASTER")
                    continue

                elif not barrelAhead(2) and mySpeed == 2:
                    print("SLOWER")
                    continue

                elif mineAhead(2):
                    print("STARBOARD")
                    continue

                elif minePreventionSystem(2):
                    print("WAIT")
                    continue

                elif TurnTowardsBarrelStarboard(2, mySpeed) and mySpeed != 2:
                    print("STARBOARD")
                    continue

                elif TurnTowardsBarrelPort(2, mySpeed) and mySpeed != 2:
                    print("PORT")
                    continue

                elif len(mineX) != 0 and z%2 == 0 and not alreadyShot():
                    print("FIRE", mineX[0], mineY[0])
                    continue

                elif z%2==0 and len(barrelX) < 3 and d2 <= 10:
                    print("FIRE", futureX, futureY)
                    continue

                elif redirect(2) and len(barrelX) < 1:
                    print("STARBOARD")
                    continue

                elif len(barrelX) >= 1 and mySpeed != 2:
                    closestX, closestY = closestBarrel(2)
                    print("MOVE", closestX, closestY)
                    continue

                elif len(barrelX) < 1 and mySpeed != 2:
                    print("MOVE", enemyShipX[0], enemyShipY[0])
                    continue

                elif stuckInCorner(2):
                    print("FASTER")
                    continue

                else:
                    print("WAIT")
                    continue

        # SHIP 3 ################## SHIP 3 ##################### SHIP 3 ####################################

        if i == 2:

            d = int((abs(shipCubeX[2]-enemyShipCubeX[2])+abs(shipCubeY[2]-enemyShipCubeY[2])+abs(shipCubeZ[2]-enemyShipCubeZ[2]))/2)
            speed=enemyShipSpeed[2]
            mySpeed=shipSpeed[2]
            aheadxx=round(speed*(1+d/3))

            futureX,futureY,futureCubeX,futureCubeY,futureCubeZ=ahead(aheadxx,2)

            d2 = int((abs(shipCubeX[2]-futureCubeX)+abs(shipCubeY[2]-futureCubeY)+abs(shipCubeZ[2]-futureCubeZ))/2)

            if cannonballAhead(2) and mySpeed != 0:
                print("STARBOARD")
                continue

            elif z%2==0 and d <= 5 and speed == 0:
                print("FIRE", futureX, futureY)
                continue

            elif z < maxSpeed or mySpeed < maxSpeed and notFacingWall(2):
                print("FASTER")
                continue

            elif barrelAhead(2) and mySpeed != 2:
                print("FASTER")
                continue

            elif not barrelAhead(2) and mySpeed == 2:
               print("SLOWER")
               continue

            elif mineAhead(2):
                print("STARBOARD")
                continue

            elif minePreventionSystem(2):
                    print("WAIT")
                    continue

            elif TurnTowardsBarrelStarboard(2, mySpeed) and mySpeed != 2:
                print("STARBOARD")
                continue

            elif TurnTowardsBarrelPort(2, mySpeed) and mySpeed != 2:
                print("PORT")
                continue

            elif len(mineX) != 0 and z%2 == 0 and not alreadyShot():
                print("FIRE", mineX[0], mineY[0])
                continue

            elif z%2==0 and len(barrelX) < 3 and d2 <= 10:
                print("FIRE", futureX, futureY)
                continue

            elif redirect(2) and len(barrelX) < 1:
                print("STARBOARD")
                continue

            elif len(barrelX) >= 1 and mySpeed != 2:
                closestX, closestY = closestBarrel(2)
                print("MOVE", closestX, closestY)
                continue

            elif len(barrelX) < 1 and enemyShipHealth[2] < shipHealth[2]:
                cornerX,cornerY = closestCorner(2)
                print("STARBOARD")
                continue

            elif len(barrelX) < 1 and mySpeed != 2:
                print("MOVE", enemyShipX[0], enemyShipY[0])
                continue

            elif stuckInCorner(2):
                print("FASTER")
                continue

            else:
                print("WAIT")
                continue
    z+=1
