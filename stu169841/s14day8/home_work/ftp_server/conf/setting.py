import os
import sys
mysep = os.path.sep
init_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,init_path)
# print (init_path)
# print (sys.path)
#D:\oldboy_python14\stu169841\s14day8\home_work
#########################################################################################
Storage_path = mysep.join([init_path,"updata"])
Storage_bak_path = mysep.join([init_path,"back_updata"])
UserJson = mysep.join([init_path,"userdata"])
