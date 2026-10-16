from god import *

file_delete(xlsx_value('b2','main.xlsx'))
file_delete(xlsx_value('b3','main.xlsx'))
file_delete(xlsx_value('b4','main.xlsx'))
file_delete(xlsx_value('b5','main.xlsx'))


date_created = date()
date_expired = date_add(date_created, 7)
csv_main = f"{date_created}_main.csv"
csv_filtered = f"{date_created}_filtered.csv"
csv_filtered_edited = f"{date_created}_filtered_edited.csv"
expiry = f"{date_created}_expiry_dates.csv"


download_csv(csv_main)
filter_csv(csv_main, csv_filtered)
filter_csv_edited(csv_filtered, csv_filtered_edited)
get_expiry_dates(csv_filtered_edited, expiry)


xlsx_update('a2','main_csv','main.xlsx')
xlsx_update('b2',csv_main,'main.xlsx')
xlsx_update('d2',date_created,'main.xlsx')
xlsx_update('e2',date_expired,'main.xlsx')


xlsx_update('a3','filtered_csv','main.xlsx')
xlsx_update('b3',csv_filtered,'main.xlsx')
xlsx_update('d3',date_created,'main.xlsx')
xlsx_update('e3',date_expired,'main.xlsx')


xlsx_update('a4','filtered_edited_csv','main.xlsx')
xlsx_update('b4',csv_filtered_edited,'main.xlsx')
xlsx_update('d4',date_created,'main.xlsx')
xlsx_update('e4',date_expired,'main.xlsx')


xlsx_update('a5','expiry_dates_csv','main.xlsx')
xlsx_update('b5',expiry,'main.xlsx')
xlsx_update('d5',date_created,'main.xlsx')
xlsx_update('e5',date_expired,'main.xlsx')


try:
    from nse_holiday_updater import update_nse_holidays
    update_nse_holidays()
except Exception:
    from audio import  fass
    print("NSE holiday update failed. Please update your code and try again. \n         file name\n (nse_holiday_updater.py) \nwhere the function \n update_nse_holidays() \nis located.")
    fass()


