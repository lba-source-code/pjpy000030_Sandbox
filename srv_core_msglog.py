"""DSSi comment: stantdard package"""
from colorama import Fore, Back, Style

"""DSSi comment: custom package"""

"""DSSi comment: msg log"""
class Cl_msglog:

    def mt_msglog_start(self, msg="ini", description="init"):
        print(Back.CYAN + f'\nDSSi log START {msg}: {description}\n')
    
    def mt_msglog(self, msg="ini", description="init"):
        print(Back.MAGENTA + f'\nDSSi log {msg}: {description}\n')

    def mt_msglog_error(self, msg="ini", description="init"):
        print(Back.RED + f'\nDSSi log ERROR {msg}: {description}\n')

    def mt_msglog_finished(self, msg="ini", description="init"):
        print(Back.GREEN + f'\nDSSi log FINISH {msg}: {description}\n')
