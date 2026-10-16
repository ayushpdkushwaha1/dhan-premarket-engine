import json
import os
from datetime import datetime
from xlsx import xlsx_value
from path_finder import path

def update_config_json():
    # 1. डेटा निकालना (तुम्हारे एक्सेल लोकेशन्स के हिसाब से)
    client_id = str(xlsx_value("b2", "fix.xlsx"))
    access_token = str(xlsx_value("c10", "main.xlsx"))
    current_expiry = str(xlsx_value("c6", "main.xlsx"))
    lot_size = int(xlsx_value("c9", "main.xlsx"))
    target_csv = str(xlsx_value("b11", "main.xlsx"))
    trading_day = str(xlsx_value("h2", "ex.xlsx"))
    spot_security_id = str(xlsx_value("b3", "fix.xlsx"))

    # 2. करेंट डेट और टाइम (सिक्योरिटी चेक के लिए)
    now = datetime.now()
    
    # 3. JSON का स्ट्रक्चर बनाना (C++ इसी फॉर्मेट में पढ़ेगा)
    config_data = {
        "auth": {
            "client_id": client_id,
            "access_token": access_token
        },
        "path": {
            "root": path
        },
        "instrument": {
            "name": "NIFTY",
            "spot_security_id": spot_security_id,
            "lot_size": lot_size,
            "current_expiry": current_expiry,
            "current_expiry_day":str(xlsx_value("e6", "main.xlsx")),
            "target_csv": target_csv,
            "target_csv_with_path": path+xlsx_value("b11", "main.xlsx")
        },
        "market": {
            "trading_day": trading_day
        },
        "metadata": {
            "generated_date": now.strftime("%Y-%m-%d"),
            "generated_time": now.strftime("%H:%M:%S")
        }
    }

    # 4. JSON फाइल को सेव/अपडेट करना
    file_path = os.path.join(path, "config.json")
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(config_data, json_file, indent=4)

