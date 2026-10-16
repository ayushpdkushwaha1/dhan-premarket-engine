import pandas as pd
from path_finder import current_dir
import os


def filter_csv_edited(old_filename, new_filename):
    old_file_path = f"{current_dir}/files/{old_filename}"
    new_file_path = f"{current_dir}/files/{new_filename}"

    df = pd.read_csv(old_file_path)

    # 1. फ़िल्टर की कंडीशंस (NSE, OPTIDX/INDEX, और NIFTY)
    valid_exch = df["EXCH_ID"] == "NSE"
    valid_instr = df["INSTRUMENT"].isin(["OPTIDX", "INDEX"])
    valid_underlying = df["UNDERLYING_SYMBOL"] == "NIFTY"

    filtered_df = df[valid_exch & valid_instr & valid_underlying].copy()

    # 2. जो कॉलम्स तुमने डिलीट करने को बोले हैं, उनकी लिस्ट
    columns_to_remove = [
        "INSTRUMENT_TYPE",
        "ISIN",
        "SERIES",
        "BRACKET_FLAG",
        "COVER_FLAG",
        "ASM_GSM_FLAG",
        "ASM_GSM_CATEGORY",
        "BUY_SELL_INDICATOR",
        "BUY_CO_MIN_MARGIN_PER",
        "BUY_CO_SL_RANGE_MAX_PERC",
        "BUY_CO_SL_RANGE_MIN_PERC",
        "BUY_BO_SL_RANGE_MAX_PERC",
        "BUY_BO_SL_RANGE_MIN_PERC",
        "EXPIRY_FLAG",
        "TICK_SIZE",
        "BUY_BO_MIN_MARGIN_PER",
        "BUY_BO_PROFIT_RANGE_MAX_PERC",
        "BUY_BO_PROFIT_RANGE_MIN_PERC",
        "MTF_LEVERAGE",
        "SM_FREEZE_QTY",
        "SM_UPPER_LIMIT",
        "SM_LOWER_LIMIT",
        "UNDERLYING_SECURITY_ID",
    ]

    # सिर्फ वही कॉलम्स हटाओ जो फाइल में मौजूद हैं
    existing_cols_to_remove = [
        col for col in columns_to_remove if col in filtered_df.columns
    ]
    filtered_df.drop(columns=existing_cols_to_remove, inplace=True)

    # 3. 'Unnamed' नाम वाले किसी भी खाली कॉलम को हटाना
    unnamed_cols = [col for col in filtered_df.columns if "Unnamed" in str(col)]
    filtered_df.drop(columns=unnamed_cols, inplace=True)

    # 4. नई साफ-सुथरी फाइल सेव करना
    filtered_df.to_csv(new_file_path, index=False)

    return True


def filter_csv(old_filename, new_filename):
    """यह फंक्शन डेटा को फ़िल्टर करेगा, लेकिन कोई भी असली कॉलम डिलीट नहीं करेगा।"""
    old_file_path = f"{current_dir}/files/{old_filename}"
    new_file_path = f"{current_dir}/files/{new_filename}"

    df = pd.read_csv(old_file_path, low_memory=False)

    # 1. फ़िल्टर की कंडीशंस सेम रहेंगी
    valid_exch = df["EXCH_ID"] == "NSE"
    valid_instr = df["INSTRUMENT"].isin(["OPTIDX", "INDEX"])
    valid_underlying = df["UNDERLYING_SYMBOL"] == "NIFTY"

    filtered_df = df[valid_exch & valid_instr & valid_underlying].copy()

    # 2. 'Unnamed' नाम वाले सिर्फ कचरा/खाली कॉलम्स को हटाना (असली कॉलम्स को नहीं छुएगा)
    unnamed_cols = [col for col in filtered_df.columns if "Unnamed" in str(col)]
    filtered_df.drop(columns=unnamed_cols, inplace=True)

    # 3. फ़ाइल सेव करना
    filtered_df.to_csv(new_file_path, index=False)

    return True


# --- यहाँ नया फंक्शन जोड़ा है जो सिर्फ दी हुई डेट का डेटा अलग करेगा ---
def csv_date(date, new_file_name, old_file_name):
    """तुम्हारी दी हुई डेट की सारी रोज़ को फ़िल्टर करके नई फ़ाइल में सेव करेगा।"""
    old_file_path = f"{current_dir}/files/{old_file_name}"
    new_file_path = f"{current_dir}/files/{new_file_name}"

    df = pd.read_csv(old_file_path)

    # जो डेट तुम इनपुट दोगे, उसे 'SM_EXPIRY_DATE' वाले कॉलम में मैच करना
    date_filtered_df = df[df["SM_EXPIRY_DATE"].astype(str) == str(date)]

    # नई फ़ाइल में सिर्फ उस डेट का डेटा सेव करना
    date_filtered_df.to_csv(new_file_path, index=False)

    return True







def filter_csv_edited_pro(old_filename, new_filename):
    old_file_path = f"{current_dir}/files/{old_filename}"
    new_file_path = f"{current_dir}/files/{new_filename}"

    if not os.path.exists(old_file_path):
        return False

    df = pd.read_csv(old_file_path)

    # 1. पहले अपनी पुरानी कंडीशंस से डेटा फ़िल्टर कर लो (NSE, OPTIDX/INDEX, NIFTY)
    valid_exch = df["EXCH_ID"] == "NSE"
    valid_instr = df["INSTRUMENT"].isin(["OPTIDX", "INDEX"])
    valid_underlying = df["UNDERLYING_SYMBOL"] == "NIFTY"

    filtered_df = df[valid_exch & valid_instr & valid_underlying].copy()

    # 2. प्रो-लॉजिक: सिर्फ वही कॉलम्स रखो जो तुम्हें चाहिए, बाकी सब अपने आप गायब!
    keep_columns = ["SECURITY_ID", "DISPLAY_NAME"]

    # यहाँ सेफ्टी के लिए चेक कर रहे हैं कि ये दोनों कॉलम पुरानी फाइल में हैं या नहीं
    existing_keep_cols = [col for col in keep_columns if col in filtered_df.columns]

    # सिर्फ इन दोनों कॉलम का ही डेटा आगे पास होगा
    pro_df = filtered_df[existing_keep_cols]

    # 3. नई साफ़-सुथरी 2 कॉलम्स वाली फाइल सेव कर दो
    pro_df.to_csv(new_file_path, index=False)

    return True

