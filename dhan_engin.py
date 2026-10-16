import sys
import time
import pyotp
from day import *
from xlsx import *
from dhanhq import DhanLogin, DhanContext, dhanhq


# dhan को पहले None रखो ताकि कभी फेल होने पर ImportError न आए
dhan = None

if is_date_not_equal(date(), xlsx_value('e10', 'main.xlsx')):
    dhan_login = DhanLogin(str(xlsx_value('b2', 'fix.xlsx')))
    
    # 🔁 कुल 5 प्रयासों का लूप (4 सामान्य + 1 बैकऑफ प्रयास)
    max_retries = 5
    for attempt in range(1, max_retries + 1):
        try:
            # हर बार फ्रेश TOTP जनरेट होगा
            current_totp = pyotp.TOTP(xlsx_value('b4', 'fix.xlsx')).now()
            access_token_data = dhan_login.generate_token(
                str(xlsx_value('b5', 'fix.xlsx')), 
                current_totp
            )
            
            # अगर टोकन मिल गया तो अंदर का काम करो और लूप से बाहर निकलो
            if isinstance(access_token_data, dict) and 'accessToken' in access_token_data:
                xlsx_update('e10', date(), 'main.xlsx')
                xlsx_update('d10', date(), 'main.xlsx')
                xlsx_update('c10', access_token_data['accessToken'], 'main.xlsx')
                
                dhan_context = DhanContext(str(xlsx_value('b2', 'fix.xlsx')), access_token_data['accessToken'])
                dhan = dhanhq(dhan_context)
                print(f"सफलता! {attempt} प्रयास में टोकन बन गया।")
                break  # सफलता मिलते ही लूप तुरंत रुक जाएगा
            else:
                msg = access_token_data.get('message', access_token_data) if isinstance(access_token_data, dict) else access_token_data
                print(f"प्रयास {attempt}/{max_retries} फेल हुआ: {msg}")

        except Exception as e:
            print(f"प्रयास {attempt}/{max_retries} में एरर आया: {e}")

        # अगर 5वां (आखिरी) प्रयास नहीं है, तभी टाइमर चलाकर इंतज़ार करो
        if attempt < max_retries:
            # 4 प्रयास फेल होने के बाद 5वें के लिए 45 सेकंड, बाकी के लिए 10 सेकंड
            wait_seconds = 45 if attempt == 4 else 10

            for sec in range(wait_seconds, 0, -1):
                sys.stdout.write(f"\rअगला प्रयास {sec} सेकंड में... ")
                sys.stdout.flush()
                time.sleep(1)
            sys.stdout.write("\r" + " " * 35 + "\r")  # टाइमर लाइन साफ करें
            sys.stdout.flush()
    else:
        # 5 प्रयास पूरे फेल होने पर बिना रुके तुरंत अलर्ट
        print("अरे भाई, 5 बार कोशिश कर ली पर धन लॉगिन नहीं हुआ!")

else:
    # अगर कंडीशन मैच नहीं हुई, तो एक्सेल से पुराना टोकन उठाकर कनेक्ट करो
    dhan_context = DhanContext(str(xlsx_value('b2', 'fix.xlsx')), xlsx_value('c10', 'main.xlsx'))
    dhan = dhanhq(dhan_context)
