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

tarletras = RDK.Item("Letras") 
tarletras = tarletras.Pose()


#obtener parametros de otro python desde la estacion
esperaorden = RDK.getParam("orden1")
while (esperaorden < 2):
    esperaorden = RDK.getParam("orden1")
    pass

robot.setPoseFrame(frameletras)
robot.MoveJ(tarletras*roty(-pi))
RDK.RunProgram("WeldOn(1)")

robot.MoveJ(tarletras*transl(100,50,0)*roty(-pi))
robot.MoveJ(tarletras*transl(0,50,50)*roty(-pi))
RDK.RunProgram("WeldOn(0)")
