from audio import start_audio , holidayss
start_audio()
from independent_fun import is_today_holiday
if is_today_holiday():
    suru_ho_jao = input("Today is a holiday,\n Still do you want to continue? Write (Yes) and press enter \n Otherwise press enter to exit: ")
    if suru_ho_jao.lower() == "yes":
        from run_python import run
        run("ignition.py")
    else:
        from audio import end_audio
        end_audio()
        holidayss()
        exit()
else:
    from run_python import run
    run("ignition.py")
    

