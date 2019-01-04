import subprocess
import time

from modules import cbpi
from modules.core.hardware import ActorBase
from modules.core.props import Property

@cbpi.actor
class shellscript(ActorBase):
    
    plug = Property.Select(label="Plug", options=[1,2,3,4,5])
    
    def on(self, power=100):
        try:
            print self.plug
            command = "/home/pi/actor-on.sh " + str(self.plug)
            subprocess.call(command, shell=True)
        except Exception as e:
            self.api.notify("Error Shellscript plugin", type="danger", timeout=None)
            self.api.app.logger.error("Error Shellscript plugin")

    def off(self):
        try:
            command = "/home/pi/actor-off.sh " + str(self.plug)
            subprocess.call(command, shell=True)
        except Exception as e:
            self.api.notify("Error Shellscript plugin", type="danger", timeout=None)
            self.api.app.logger.error("Error Shellscript plugin")
