"""DSSi comment: stantdard package"""

"""DSSi comment: custom package"""

"""DSSi comment: msg log"""
class Cl_msglog:

    def mt_msglog_start(self, msg="ini", description="init"):
        print(f'\nDSSi log START {msg}: {description}\n')
    
    def mt_msglog_start(self, msg="ini", description="init"):
        print(f'\nDSSi log {msg}: {description}\n')

    def mt_msglog_start(self, msg="ini", description="init"):
        print(f'\nDSSi log ERROR {msg}: {description}\n')

    def mt_msglog_start(self, msg="ini", description="init"):
        print(f'\nDSSi log FINISH {msg}: {description}\n')
