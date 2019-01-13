import subprocess
import time

from modules import cbpi
from modules.core.hardware import ActorBase
from modules.core.props import Property

@cbpi.actor
class Nexa433(ActorBase):
    
    plug = Property.Text("Nexa433", True, "1")
    
    def on(self, power=100):
        try:
            print self.plug
            command = "/home/pi/craftbeerpi3/modules/plugins/Nexa433/actor-on.sh " + str(self.plug)
            subprocess.call(command, shell=True)
        except Exception as e:
            self.api.notify("Error Nexa433 plugin", type="danger", timeout=None)
            self.api.app.logger.error("Error Nexa433 plugin")

    def off(self):
        try:
            command = "/home/pi/craftbeerpi3/modules/plugins/Nexa433/actor-off.sh " + str(self.plug)
            subprocess.call(command, shell=True)
        except Exception as e:
            self.api.notify("Error Nexa 433 plugin", type="danger", timeout=None)
            self.api.app.logger.error("Error Nexa433 plugin")
