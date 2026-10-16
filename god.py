from csv_fun import *
from independent_fun import *
from day import *
from download_fun import *
from expiry_finder import *
from filter_csv import *
from path_finder import *
from run_python import *
from xlsx import *
from path_finder import current_dir
from dhan_engin import *
from day2 import wait_time

import subprocess

import os, subprocess










def check_and_update_expiry():

    old_expiry = xlsx_value("c6", "main.xlsx")
    expiry_filename = xlsx_value("b5", "main.xlsx")

    if old_expiry is None or is_date_greater(date(), old_expiry):

        row = 0
        while True:
            current_csv_date = csv_value(row, 0, expiry_filename)

            if current_csv_date is None:
                break

            if is_date_greater(current_csv_date, date()):
                # 1. सबसे पहले b11 में जो पुरानी एडिटेड फ़ाइल का नाम है, उसे डिलीट करो
                old_edited_file = xlsx_value("b11", "main.xlsx")
                if old_edited_file:
                    file_delete(old_edited_file)

                # 2. बाक़ी का पुराना एक्सेल अपडेट का काम
                xlsx_update("c6", current_csv_date, "main.xlsx")
                file_delete(xlsx_value("b7", "main.xlsx"))

                csv_date_file_name = f"{date()}_expiry.csv"

                csv_date(
                    xlsx_value("c6", "main.xlsx"),
                    csv_date_file_name,
                    xlsx_value("b4", "main.xlsx"),
                )

                xlsx_update("b7", csv_date_file_name, "main.xlsx")
                xlsx_update("d7", date(), "main.xlsx")
                xlsx_update(
                    "e6", f"NIFTY {format_my_date(current_csv_date)}", "main.xlsx"
                )

                # 3. नया काम: नई प्रो-फ़िल्टर्ड फ़ाइल का नाम सेट करो और फ़ंक्शन रन करो
                new_edited_filename = f"{date()}_edited_expiry.csv"

                # तुम्हारी प्रो-फ़िल्टर वाली फ़ंक्शन को यहाँ कॉल किया (Raw फ़ाइल से प्रो फ़ाइल बनेगी)
                filter_csv_edited_pro(csv_date_file_name, new_edited_filename)

                # एक्सेल के b11 में इस नई फ़ाइल का नाम अपडेट कर दो
                xlsx_update("b11", new_edited_filename, "main.xlsx")

                # 4. यह तुम्हारी आख़िरी लाइन थी, जो अब नई अपडेटेड b11 फ़ाइल से वैल्यू उठाएगी
                xlsx_update(
                    "c9",
                    csv_value(3, 7, xlsx_value("b7", "main.xlsx")),
                    "main.xlsx",
                )
                return True

            row += 1

    return False





def reminder(number_by_hundred_remainder):
    sl = number_by_hundred_remainder%100
    return sl


def nifty_workprice(price_of_nifty_or_any_thing_is_that):
    # तुम्हारे बनाए हुए reminder() फंक्शन का इस्तेमाल यहाँ होगा
    nifty_reminder = reminder(price_of_nifty_or_any_thing_is_that)

    if 00.00 <= nifty_reminder <= 50.00:
        workprice = price_of_nifty_or_any_thing_is_that - nifty_reminder
    else:
        workprice = price_of_nifty_or_any_thing_is_that - nifty_reminder + 50

    return workprice



def call_itm_price(price,how_much):
    x = nifty_workprice(price)
    output = ((x-((how_much-1)*50)))
    return output


def call_otm_price(price,how_much):
    x = nifty_workprice(price)
    output = ((x+(how_much*50)))
    return output

def put_itm_price(price,how_much):
    x = nifty_workprice(price)
    output = ((x+(how_much*50)))
    return output

def put_otm_price(price,how_much):
    x = nifty_workprice(price)
    output = ((x-((how_much-1)*50)))
    return output




def display_name(strike_price, option_type):
    x = xlsx_value("e6", "main.xlsx")
    option_type = option_type.upper()

    
    if option_type in ["CALL", "C", "CL", "CLL", "CA", "L"]:
        output = x + " " + str(int(strike_price)) + " CALL"

    elif option_type in ["PUT", "PU", "PT", "UT", "T", "U", "P"]:
        output = x + " " + str(int(strike_price)) + " PUT"

    return output


def find_security_id(name): 
    security_id=csv_value_to_value(name,"SECURITY_ID",xlsx_value('b7','main.xlsx'))
    security_id = int(security_id)
    return security_id





