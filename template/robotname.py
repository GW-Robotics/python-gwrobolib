from subsystems import ExampleSubsystem
#from subsystems import SensorStick    # SEAS Innovation Challenge subsystems
from time import sleep

import multiprocessing

def worker():
    print "Robot in running"
    return

p = multiprocessing.Process(target=worker)
p.start()
p.join()

#Example Subsystem
example_subsystem = ExampleSubsystem()

while (True):
    # Insert subsystem commands here
    sleep(.1)
