import os
import subprocess
import inspect
from utils import *
from results import Results

class Runner:
    @classmethod
    def run_cmd(cls, cmd):
        logging.debug('Executing: ' + str(cmd))

        cmd_obj = subprocess.Popen([cmd], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stack = inspect.stack()
        fname = os.path.basename(stack[1][1])
        line = str(stack[1][2])
        caller = stack[1][3]
        Results.add_step(fname + '(' + line + '): ' + caller + '(): ' + cmd)
        res = '\n'.join(cmd_obj.communicate())
        return (res.strip())