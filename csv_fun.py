import os
import pandas as pd
from path_finder import current_dir


# --- 1. CSV POSITION FINDER FUNCTION (RETURNS ROW & COL NUMBERS) ---
def csv_position(value, filename):
    """CSV फाइल में किसी भी वैल्यू की पोजीशन (Row Number, Column Number) ढूंढने के लिए।

    रिटर्न: (row_index, column_index) का टुपल (Tuple) या वैल्यू न मिलने पर
    None
    """
    file_path = f"{current_dir}/files/{filename}"
    if not os.path.exists(file_path):
        return None

    df = pd.read_csv(file_path)

    for col_name in df.columns:
        matched_rows = df[df[col_name] == value].index
        if not matched_rows.empty:
            row_idx = int(matched_rows[0])
            # कॉलम के नाम से उसका नंबर (Index) पता करना
            col_idx = int(df.columns.get_loc(col_name))
            return (row_idx, col_idx)

    return None


# --- 2. VALUE BY POSITION FUNCTION (USING ROW & COL NUMBERS) ---
def csv_value(row_index, column_index, filename):
 
    file_path = f"{current_dir}/files/{filename}"
    if not os.path.exists(file_path):
        return None

    df = pd.read_csv(file_path)

    try:
        # .iat का यूज़ करके सीधे Row और Column के नंबर से वैल्यू उठाना
        value = df.iat[int(row_index), int(column_index)]

        if pd.isna(value):
            return None

        if isinstance(value, (int, float)):
            return value
        return str(value)
    except:
        return None
    


def csv_header_value(column_index, filename):
    file_path = f"{current_dir}/files/{filename}"
    if not os.path.exists(file_path):
        return None

    df = pd.read_csv(file_path)

    try:
       
        header_name = df.columns[int(column_index)]
        return str(header_name)
    except:
        return None




def csv_value_to_value(search_value, target_column, filename):
  
    file_path = f"{current_dir}/files/{filename}"
    if not os.path.exists(file_path):
        return None

    df = pd.read_csv(file_path)

    # 1. पूरी फाइल में वो रो (Row) ढूंढना जहाँ हमारी search_value मौजूद है
    matched_row_index = None

    for col in df.columns:
        # अगर वैल्यू मैच हो जाती है, तो उसका रो इंडेक्स निकाल लो
        matched_indices = df[df[col] == search_value].index
        if not matched_indices.empty:
            matched_row_index = matched_indices[0]  # पहला मैच मिलते ही लॉक कर लो
            break

    # 2. अगर वैल्यू पूरी फाइल में कहीं नहीं मिली
    if matched_row_index is None:
        return None

    try:
        # 3. उसी रो नंबर और तुम्हारे मांगे गए हेडर (target_column) से वैल्यू उठाना
        res_val = df.at[matched_row_index, target_column]

        if pd.isna(res_val):
            return None

        # सही डेटा टाइप में वापस करना
        if isinstance(res_val, (int, float)):
            return res_val
        return str(res_val)
    except:
        return None
    





# --- 3. GLOBAL VALUE UPDATE FUNCTION ---
def csv_update(old_value, new_value, filename):

    file_path = f"{current_dir}/files/{filename}"
    if not os.path.exists(file_path):
        return False
        
    df = pd.read_csv(file_path)
    
    is_updated = False
    for col in df.columns:
        mask = df[col] == old_value
        if mask.any():
            df.loc[mask, col] = new_value
            is_updated = True
            
    if is_updated:
        df.to_csv(file_path, index=False)
        return True
        
    return False




def csv_create(name):
    """एक बिल्कुल खाली (Blank) .csv फ़ाइल क्रिएट करने के लिए।"""
    file_path = f"{current_dir}/files/{name}"

    # 'w' मोड में फ़ाइल खोलकर बिना कुछ लिखे बंद करने से खाली फ़ाइल बन जाती है
    with open(file_path, "w", encoding="utf-8") as f:
        pass

    return True


# --- इस्तेमाल करने का तरीका ---
# csv_create("my_blank_file.csv")