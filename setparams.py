from robolink import *    # RoboDK API      
from robodk import*        # Robot toolbox

RDK = Robolink() 

robot = RDK.ItemUserPick('',ITEM_TYPE_ROBOT) 	#adquirir todos los parámetros del robot 
if not robot.Valid(): 
    quit() 
reference = robot.Parent()  # devuelve el artículo 
robot.setPoseFrame(reference)#establece el marco de referencia de un robot 
pose_ref=robot.Pose()  #devuelve la posición actual del robot con matriz
b=robodk.pose_2_xyzrpw(pose_ref) # devuelve la posición actual del robot 

frameletras = RDK.Item("FrameLetras",ITEM_TYPE_FRAME) 
robot.setPoseFrame(frameletras)

tarletras = RDK.Item("Letras",ITEM_TYPE_TARGET) 
tarletras = tarletras.Pose()


robot.setPoseFrame(frameletras)
ORDEN1 = 0

RDK.RunProgram("WeldOn(-1)")
RDK.setParam("orden1",ORDEN1)
while (ORDEN1 < 3):
    robot.MoveJ(tarletras*roty(-pi))
    robot.MoveJ(tarletras*transl(0,50,0)*roty(-pi))
    robot.MoveJ(tarletras*transl(100,0,50)*roty(-pi))
    ORDEN1+= 1
    RDK.setParam("orden1",ORDEN1)
    
