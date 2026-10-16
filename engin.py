from god import *
########### dont touch this areas this is very important for the expiry dates and csv files and dhan auto update dhan tokan id or access token ############


if date_compare(date(), xlsx_value("e2", "main.xlsx")):
    run('en_update.py')
check_and_update_expiry()


run('dhan_engin.py')
######## the areas end here ############




