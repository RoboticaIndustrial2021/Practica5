from robolink import *    # RoboDK API      
from robodk import*        # Robot toolbox

RDK = Robolink() 

robot = RDK.Item('Kawasaki RS03N') 	#adquirir todos los parámetros del robot 
if not robot.Valid(): 
    quit() 
reference = robot.Parent()  # devuelve el artículo 
robot.setPoseFrame(reference)#establece el marco de referencia de un robot 
pose_ref=robot.Pose()  #devuelve la posición actual del robot con matriz
b=Pose_2_TxyzRxyz(pose_ref) # devuelve la posición actual del robot 

frameletras = RDK.Item("FrameLetrasKawa",ITEM_TYPE_FRAME) 
robot.setPoseFrame(frameletras)

tarletras = RDK.Item("LetrasKawa",ITEM_TYPE_TARGET) 
tarletras = tarletras.Pose()


robot.setPoseFrame(frameletras)
ORDEN1 = 0
robot.setSpeed(10,10)
RDK.setParam("orden1",ORDEN1)
while (ORDEN1 < 3):
    robot.MoveJ(tarletras)
    robot.MoveJ(tarletras*transl(0,50,0))
    robot.MoveJ(tarletras*transl(100,0,50))
    ORDEN1+= 1
    RDK.ShowMessage("Valor de orden {}".format(ORDEN1),False)
    RDK.setParam("orden1",ORDEN1)
    
