"""DSSi comment: stantdard package"""

"""DSSi comment: custom package"""
from srv_core_msglog import Cl_msglog

"""DSSi comment: global variable"""
gv_msglog = Cl_msglog()

"""DSSi comment: define services"""

def fn_usefuloperators():
    gv_msglog.mt_msglog_start('fn_usefuloperators')

    return gv_msglog.mt_msglog_finished('fn_usefuloperators')

"""DSSi call service"""
fn_usefuloperators()