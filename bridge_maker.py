from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()
def checkDirection():
    pRot=round(mc.player.getRotation())
    #Front
    if pRot>=170 and pRot<=190:
        return 1
    #Left
    elif pRot>=260 and pRot<=280:
        return 2
    #Back
    elif (pRot>=350 and pRot<=360) or (pRot>=0 and pRot<=10):
        return 3
    #Right
    elif (pRot>=80 and pRot<=100):
        return 4
    #Wrong direction
    else:
        return 5
def getBridgeDirAndStartPos():
    isWaterInFrontOfPlayer=False
    while isWaterInFrontOfPlayer!=True:
        sleep(0.5)
        direction=checkDirection()
        if direction!=5:
            x,y,z=mc.player.getPos()
            x=round(x)
            y=round(y)
            z=round(z)
            block=-1
            if direction==1:
                blockPos=[x,y,z-1]
                block=mc.getBlock(x,y-1,z-1)
                print(x,y-1,z-1,direction)
            elif direction==2:
                blockPos=[x-1,y,z]
                block=mc.getBlock(x-1,y-1,z)
                print(x-1,y-1,z,direction)
            elif direction==3:
                blockPos=[x,y,z+1]
                block=mc.getBlock(x,y-1,z+1)
                print(x,y-1,z+1,direction)
            else:
                blockPos=[x+1,y,z]
                block=mc.getBlock(x+1,y-1,z)
                print(x+1,y-1,z,direction)
            if block in [8,9]:
                print('Water')
                mc.postToChat('Water')
                isWaterInFrontOfPlayer=True
                blockPos.append(direction)
                return blockPos
            else:
                print('Not water')
                mc.postToChat('Not water')


x,y,z,d=getBridgeDirAndStartPos()
mc.setBlock(x,y,z,44)
stop=False
while stop==False:
    print(d)
    if d==1:
        if mc.getBlock(x,y-1,z-2) in [8,9]:
            mc.setBlock(x-1,y,z,1)
            mc.setBlock(x+1,y,z,1)
            z=z-1
            mc.setBlock(x-1,y,z,1)
            mc.setBlock(x,y,z,1)
            mc.setBlock(x+1,y,z,1)
            mc.setBlock(x-1,y+1,z,113)
            mc.setBlock(x+1,y+1,z,113)
        elif mc.getBlock(x,y-1,z-2) not in [8,9]:
            z=z-1
            mc.setBlock(x,y,z,44)
            mc.setBlock(x-1,y,z,1)
            mc.setBlock(x+1,y,z,1)
            stop=True
    elif d==2:
        if mc.getBlock(x-2,y-1,z) in [8,9]:
            mc.setBlock(x,y,z-1,1)
            mc.setBlock(x,y,z+1,1)
            x=x-1
            mc.setBlock(x,y,z-1,1)
            mc.setBlock(x,y,z,1)
            mc.setBlock(x,y,z+1,1)
            mc.setBlock(x,y+1,z-1,113)
            mc.setBlock(x,y+1,z+1,113)
        elif mc.getBlock(x-2,y-1,z) not in [8,9]:
            x=x-1
            mc.setBlock(x,y,z,44)
            mc.setBlock(x,y,z-1,1)
            mc.setBlock(x,y,z+1,1)
            stop=True
    elif d==3:
        if mc.getBlock(x,y-1,z+2) in [8,9]:
            mc.setBlock(x-1,y,z,1)
            mc.setBlock(x+1,y,z,1)
            z=z+1
            mc.setBlock(x-1,y,z,1)
            mc.setBlock(x,y,z,1)
            mc.setBlock(x+1,y,z,1)
            mc.setBlock(x-1,y+1,z,113)
            mc.setBlock(x+1,y+1,z,113)
        elif mc.getBlock(x,y-1,z+2) not in [8,9]:
            z=z+1
            mc.setBlock(x,y,z,44)
            mc.setBlock(x-1,y,z,1)
            mc.setBlock(x+1,y,z,1)
            stop=True
    elif d==4:
        if mc.getBlock(x+2,y-1,z) in [8,9]:
            print('here')
            mc.setBlock(x,y,z-1,1)
            mc.setBlock(x,y,z+1,1)
            x=x+1
            mc.setBlock(x,y,z-1,1)
            mc.setBlock(x,y,z,1)
            mc.setBlock(x,y,z+1,1)
            mc.setBlock(x,y+1,z-1,113)
            mc.setBlock(x,y+1,z+1,113)
        elif mc.getBlock(x+2,y-1,z) not in [8,9]:
            print('here')
            x=x+1
            mc.setBlock(x,y,z,44)
            mc.setBlock(x,y,z-1,1)
            mc.setBlock(x,y,z+1,1)
            stop=True