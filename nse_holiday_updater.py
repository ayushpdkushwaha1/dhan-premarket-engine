import os
import json
from datetime import datetime, date, timedelta
from curl_cffi import requests
from path_finder import current_dir

def update_nse_holidays():

    save_dir = f"{current_dir}/files"
    os.makedirs(save_dir, exist_ok=True)
    file_path = os.path.join(save_dir, "nse_holidays.json")

    current_year = datetime.now().year
    all_closed_days = set()

    # 1. पूरे साल के शनिवार और रविवार जोड़ना (1 फरवरी को छोड़कर)
    start_date = date(current_year, 1, 1)
    end_date = date(current_year, 12, 31)
    delta = timedelta(days=1)

    temp_date = start_date
    while temp_date <= end_date:
        # 1 फरवरी को कभी नहीं जोड़ना है
        if not (temp_date.month == 2 and temp_date.day == 1):
            # 5 = Saturday, 6 = Sunday
            if temp_date.weekday() in [5, 6]:
                all_closed_days.add(temp_date.strftime("%Y-%m-%d"))
        temp_date += delta

    # 2. NSE की वेबसाइट से आधिकारिक ट्रेडिंग छुट्टियां लाना
    url = "https://www.nseindia.com/api/holiday-master?type=trading"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
    }

    try:
        session = requests.Session(impersonate="chrome120")
        session.get("https://www.nseindia.com", headers=headers, timeout=10)
        res = session.get(url, headers=headers, timeout=10)

        if res.status_code == 200:
            data = res.json()
            cbm_data = data.get("CBM", [])

            for item in cbm_data:
                raw_date = item.get("tradingDate")
                try:
                    # NSE तारीख 'dd-MMM-yyyy' फॉर्मेट में देता है (उदा: 26-Jan-2026)
                    parsed_dt = datetime.strptime(raw_date, "%d-%b-%Y").date()
                    
                    # 1 फरवरी को NSE लिस्ट में भी हो तो छोड़ देना है
                    if not (parsed_dt.month == 2 and parsed_dt.day == 1):
                        all_closed_days.add(parsed_dt.strftime("%Y-%m-%d"))
                except Exception:
                    continue
        else:
            print(f"NSE API रिस्पॉन्स एरर: {res.status_code}")
    except Exception as e:
        print(f"इंटरनेट फ़ेच नहीं हो पाया: {e}")

    # 3. तारीखों को क्रम में सेट करके सेव करना
    sorted_days = sorted(list(all_closed_days))
    
    payload = {
        "year": current_year,
        "total_closed_days": len(sorted_days),
        "closed_days": sorted_days
    }

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=4)

    return file_path

update_nse_holidays()