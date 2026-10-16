from datetime import datetime, timedelta

# --- 1. CURRENT VALUE FUNCTIONS ---


def date():

    return datetime.now().strftime("%Y-%m-%d")




# --- 2. ADDITION FUNCTIONS ---


def date_add(start_date_str, days_to_add):
    dt = datetime.strptime(start_date_str, "%Y-%m-%d")
    new_dt = dt + timedelta(days=int(days_to_add))
    return new_dt.strftime("%Y-%m-%d")


def time_add(start_time_str, hours_to_add):
    dt = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
    new_dt = dt + timedelta(hours=int(hours_to_add))
    return new_dt.strftime("%Y-%m-%d %H:%M:%S")


# --- 3. COMPARISON FUNCTIONS (RETURNS TRUE OR FALSE) ---


def is_date_greater(date_str1, date_str2):
    d1 = datetime.strptime(date_str1, "%Y-%m-%d")
    d2 = datetime.strptime(date_str2, "%Y-%m-%d")
    return d1 > d2


def is_time_greater(time_str1, time_str2):
    t1 = datetime.strptime(time_str1, "%Y-%m-%d %H:%M:%S")
    t2 = datetime.strptime(time_str2, "%Y-%m-%d %H:%M:%S")
    return t1 > t2


def is_date_equal(date_str1, date_str2):
    d1 = datetime.strptime(date_str1, "%Y-%m-%d")
    d2 = datetime.strptime(date_str2, "%Y-%m-%d")
    return d1 == d2
def is_date_not_equal(date_str1, date_str2):
    d1 = datetime.strptime(date_str1, "%Y-%m-%d")
    d2 = datetime.strptime(date_str2, "%Y-%m-%d")
    return d1 != d2


def is_time_equal(time_str1, time_str2):
    t1 = datetime.strptime(time_str1, "%Y-%m-%d %H:%M:%S")
    t2 = datetime.strptime(time_str2, "%Y-%m-%d %H:%M:%S")
    return t1 == t2


# --- 2. ADDITION FUNCTIONS ---


def date_compare(date_str1, date_str2):

    d1 = datetime.strptime(date_str1, "%Y-%m-%d")
    d2 = datetime.strptime(date_str2, "%Y-%m-%d")
    return d1 >= d2


def time_compare(time_str1, time_str2):

    t1 = datetime.strptime(time_str1, "%Y-%m-%d %H:%M:%S")
    t2 = datetime.strptime(time_str2, "%Y-%m-%d %H:%M:%S")
    return t1 >= t2







def format_my_date(date_str):
    """'2026-06-24' जैसी तारीख को '24 JUN' में बदलने के लिए।"""
    # 1. पहले टेक्स्ट को असली डेट ऑब्जेक्ट में बदलो
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")

    # 2. अब इसे अपनी पसंद के फॉर्मेट में कन्वर्ट करो (%b महीने का छोटा नाम कैपिटल में देगा)
    return date_obj.strftime("%d %b").upper()





def timex():
  
    now = datetime.now()
    return now.strftime("%H:%M:%S") + f".{now.strftime('%f')[:3]}"


def time_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
