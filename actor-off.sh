# EXAMPLE FILE
# Usage: piHomeEasy <pin number> <emitter id> <receiver id> <on|off>
#
# <pin number>  wiringPi pin number as follows:
#                 number  GPIO|GPIO  number
#                            1|2
#                 8          3|4
#                 9          5|6
#                 7          7|8         15
#                            9|10        16
#                 0         11|12         1
#                 2         13|14
#                 3         15|16         4
#                           17|18         5
#                 12        19|20
#                 9         21|22         6
#                 14        23|24        10
#                           25|26        11
# <emitter id>  Unique id of the emitter: a number between 0 and 67108863.
#                 Example: 12325262
# <receiver id> Receiver id: a number between 0 and 15, or -1 for group command.
#                 Group command is received by all receivers paired with the emi                                                                   tter id.
# <on|off>      Command to send:
#                 on  to turn on
#                 off to turn off
#
#
#
#!/bin/bash

sudo piHomeEasy 0 56123 1 off

exit 0
