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

"""DSSi comment: runtime log"""

"""DSSi comment: global variable"""
gv_msglog = Cl_msglog()

"""DSSi comment: define services"""

def fn_usefuloperators():
    gv_msglog.mt_msglog_start('fn_usefuloperators')
    return

"""DSSi call service"""
fn_usefuloperators()