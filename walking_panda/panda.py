from math import pi, sin, cos, floor
from random import random

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor


class WalkingPanda(ShowBase):

    def __init__(self, no_rotate=False, scale=1, pose=False, friends=1, color=False, music=False):
        ShowBase.__init__(self)

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Add the spinCameraTask procedure to the task manager.
        if no_rotate == False:
            self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})

        self.pandaActor.setScale(0.005*scale, 0.005*scale, 0.005*scale)
        self.pandaActor.reparentTo(self.render)
        if pose == False:
            # Loop its animation.
            self.pandaActor.loop("walk")
        else:
            self.pandaActor.pose("walk",0)

        for i in range(friends):
            placeholder = render.attachNewNode("Panda-Placeholder")

            if color == True:
                placeholder.setColor(random(), random(), random())

            j = floor(i/4)
            placeholder.setPos(scale*(i%4)*3,scale*j*5,0)
            self.pandaActor.instanceTo(placeholder)

        if music == True:
            bamboo = self.loader.loadSfx("walking_panda/Bamboo Forest Sounds.mp4")
            bamboo.play()


    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)

        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont
