#python 

# Install sysv_ipc module firstly if you don't have this
import sysv_ipc as ipc
from ctypes import *

class pxtup(Structure):
    _fields_ = [('pid1', c_int),
                ('spd1', c_int)]
def main():
    path = "/tmp"
    key = ipc.ftok(path, 2333)
    shm = ipc.SharedMemory(key, 0, 0)
    ip1 = pxtup()
    
    #I found if we do not attach ourselves
    #it will attach as ReadOnly.
    shm.attach(0,0)  
    
    ip1 = shm.read(32)
    print(ip1)
    shm.detach()
    pass

if __name__ == '__main__':
    main()