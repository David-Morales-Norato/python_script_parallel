import subprocess
import os
import time


logs_folder = "logs"
if not os.path.exists(logs_folder):
  os.makedirs(logs_folder)

output_file_1 =  open(os.path.join(logs_folder, "log_script1.txt"), "w")
output_file_2 =  open(os.path.join(logs_folder, "log_script2.txt"), "w")
error_file_1 =  open(os.path.join(logs_folder, "err_script1.txt"), "w")
error_file_2 =  open(os.path.join(logs_folder, "err_script2.txt"), "w")
#subprocess.Popen(["./main_prdip.py", "config_files/config_cameraman_fsi.json"]) 
p1 = subprocess.Popen(["python", "process.py", "0", "5", "1"], stdout=output_file_1, stderr=error_file_1, bufsize=1)
p2 = subprocess.Popen(["python", "process.py", "5", "0", "-1"], stdout=output_file_2, stderr=error_file_2, bufsize=1)
processes = [p1,p2]
while True:
    
    if all(p.poll() is None for p in processes):
        print("process running.")
        time.sleep(3)
    else:
        print("running process check out log and error files to follow the results")
        break
