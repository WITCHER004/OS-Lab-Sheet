import os import time

def create_zombie(): pid = os.fork()

if pid == 0:
print(f"Child (PID {os.getpid()}) exiting") os._exit(0)
else:
print(f"Parent (PID {os.getpid()}) sleeping, child should be zombie")
    time.sleep(30)
    print("Parent exiting and cleaning up child") os.wait()
    if _name_ == "_main_": create_zombie()