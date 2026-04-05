from datetime import datetime
from colorama import Fore, init
import inspect
import os
import re

init(autoreset=True)

class Logger:
    def __init__(self, debug=False):
        self._debug = debug

        self._Colors = {
            'alert': Fore.LIGHTYELLOW_EX,
            'fail': Fore.LIGHTRED_EX,
            'success': Fore.LIGHTGREEN_EX,
            'debug': Fore.WHITE,
            'border': Fore.BLACK,
            'timestamp': Fore.LIGHTMAGENTA_EX,
        }

        self._Icons = {
            'alert': '[!]',
            'fail': '[X]',
            'success': '[✓]',
            'debug': ':::'
        }

        self.__logfile = f"{self._get_caller_info()[0][:-3]}.log"
    
    def _get_caller_info(self):
        for frame in inspect.stack():
            if frame.filename != __file__:  # skip log.py
                filename = os.path.basename(frame.filename)
                line_no = frame.lineno
                return filename, line_no

    def _log(self, message):
        with open(self.__logfile, 'a') as f:
            print(message)

            ANSI_ESCAPE = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
            filename, lineno = self._get_caller_info()

            f.write(f"{filename} | Line: {lineno} | {ANSI_ESCAPE.sub('', message)} \n")
            

    def _timestamp(self):
        dateobj = datetime.now()
        return "{}[{}{}{}] ".format(self._Colors['border'], self._Colors['timestamp'], dateobj.strftime("%H:%M:%S"), self._Colors['border'])

    def warn(self, *args):
        message = ' '.join(str(arg) for arg in args)
        self._log("{}{}{} {}".format(self._timestamp(), self._Colors['alert'], self._Icons['alert'], message))
    
    def fail(self, *args):
        message = ' '.join(str(arg) for arg in args)
        self._log("{}{}{} {}".format(self._timestamp(), self._Colors['fail'], self._Icons['fail'], message))
    
    def success(self, *args):
        message = ' '.join(str(arg) for arg in args)
        self._log("{}{}{} {}".format(self._timestamp(), self._Colors['success'], self._Icons['success'], message))
    
    def debug(self, *args):
        if self._debug:
            message = ' '.join(str(arg) for arg in args)
            self._log("{}{}{} {}".format(self._timestamp(), self._Colors['debug'], self._Icons['debug'], message))

