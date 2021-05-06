from robolink import *    # RoboDK API      
from robodk import*        # Robot toolbox

RDK = Robolink() 

robot = RDK.ItemUserPick('',ITEM_TYPE_ROBOT) 	#adquirir todos los parámetros del robot 
if not robot.Valid(): 
    quit() 
reference = robot.Parent()  # devuelve el artículo 
robot.setPoseFrame(reference)#establece el marco de referencia de un robot 
pose_ref=robot.Pose()  #devuelve la posición actual del robot con matriz 
print (pose_ref)
print("----")
b=robodk.pose_2_xyzrpw(pose_ref) # devuelve la posición actual del robot 
print("b = ",b) 

frameletras = RDK.Item("Frame 2",ITEM_TYPE_FRAME) 
robot.setPoseFrame(frameletras)

tarletras = RDK.Item("letras",ITEM_TYPE_TARGET) 
tarletras = tarletras.Pose() 

for i in range(5): 
    if i < 1:
        robot.MoveJ(tarletras) 
    robot.MoveL(tarletras*transl(-20*i,20,0))     
     

aprox = transl(0,0,-100) 
retract = transl(0,0,-50) 
for i in range(3): 
    Refi = RDK.Item("Target "+str(i+2),ITEM_TYPE_TARGET) 
    RefTar = Refi.Pose()     
    robot.MoveJ(RefTar*aprox)     
    robot.MoveL(RefTar)     
    robot.MoveJ(RefTar*retract) 
