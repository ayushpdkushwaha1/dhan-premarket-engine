from run_python import run , run_all
from independent_fun import *
import os
try:
    if check_internet():
        run('engin.py')
    else:
       
        input("First connect to internet and then press enter to continue...")
except Exception as e:
    print(f"error in code {e}")
    input("error location in ignition.py / line no 5 to 12 \n press enter to continue...")





if check_internet():
    try:
        from audio import end_audio, play_won
        from independent_fun import update_expiry_days
        update_expiry_days()
        
        from config_generator import update_config_json
        update_config_json()
        
        end_audio()
        run_all("slow_ltp_update.py")
        play_won()
        print("done everything")
        
    except Exception as e:
        print(f"error: {e}")
        input("Press Enter to continue...")
