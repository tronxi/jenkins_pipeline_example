import subprocess
import os

def stop_local_single_service(service):
    proc = subprocess.Popen(["pgrep", "-f", service], stdout=subprocess.PIPE)
    output = proc.communicate()[0].decode("utf-8").strip()
    exit_code = proc.returncode
    if exit_code == 0 and output:
        pid_list = output.splitlines()
        for pid in pid_list:
            if int(pid) != os.getpid():
                print("parando " + pid)
                subprocess.Popen(f"kill -9 {pid}", shell=True)
    else:
        print("process not found")

print("parando")
stop_local_single_service("process.py")
print("fin")

