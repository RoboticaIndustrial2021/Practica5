from robolink import *    # RoboDK API      
from robodk import*        # Robot toolbox

RDK = Robolink() 

robot = RDK.Item('KUKA KR 10 R1100 sixx') 	#adquirir todos los parámetros del robot 
if not robot.Valid(): 
    quit() 
reference = robot.Parent()  # devuelve el artículo 
robot.setPoseFrame(reference)#establece el marco de referencia de un robot 
pose_ref=robot.Pose()  #devuelve la posición actual del robot con matriz
b=Pose_2_TxyzRxyz(pose_ref) # devuelve la posición actual del robot 

frameletras = RDK.Item("FrameLetrasKuka",ITEM_TYPE_FRAME) 
robot.setPoseFrame(frameletras)

tarletras = RDK.Item("LetrasKuka") 
tarletras = tarletras.Pose()


#obtener parametros de otro python desde la estacion
esperaorden = RDK.getParam("orden1")
while (esperaorden < 2):
    esperaorden = RDK.getParam("orden1")
    pass
robot.setSpeed(50,20)
robot.setPoseFrame(frameletras)
robot.MoveJ(tarletras)

a1 = tarletras*transl(0,150,0)
a2 = tarletras*transl(100,150,50)
a3 = tarletras*transl(150,0,0)
robot.MoveL(a1)
robot.MoveL(a2)
robot.MoveL(a3)
robot.MoveC(a1,a2)
