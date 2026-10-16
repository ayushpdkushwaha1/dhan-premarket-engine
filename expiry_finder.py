import pandas as pd
from path_finder import current_dir


def get_expiry_dates(old_filename, new_filename):
    old_file_path = f"{current_dir}/files/{old_filename}"
    new_file_path = f"{current_dir}/files/{new_filename}"

    df = pd.read_csv(old_file_path)

    # 1. सिर्फ एक्सपायरी डेट वाला कॉलम पहचानना
    date_col = "SM_EXPIRY_DATE"
    if date_col not in df.columns and "SEM_EXPIRY_DATE" in df.columns:
        date_col = "SEM_EXPIRY_DATE"

    # 2. कॉलम से सारे डुप्लीकेट्स और खाली रोज़ (NaN) को हटाना
    expiry_series = df[date_col].dropna().drop_duplicates()

    # 3. तारीखों को डेटाफ्रेम में डालकर सही से सॉर्ट करना
    expiry_df = pd.DataFrame({date_col: expiry_series})

    # तारीखों को सही क्रम (पुराने से नया) में अरेंज करना
    expiry_df["parsed_date"] = pd.to_datetime(
        expiry_df[date_col], errors="coerce"
    )
    expiry_df = expiry_df.dropna(subset=["parsed_date"])
    expiry_df = expiry_df.sort_values(by="parsed_date")

    # --- यहाँ नया चेंज किया है ---
    # 4. '0001-01-01' वाली कचरा रोज़ (Rows) को पूरी तरह से हटाना
    expiry_df = expiry_df[expiry_df[date_col] != "0001-01-01"]

    # 5. सिर्फ वही एक कॉलम रखना और नई फाइल में सेव करना
    final_df = expiry_df[[date_col]]
    final_df.to_csv(new_file_path, index=False)

    return True


# --- इस्तेमाल करने का तरीका ---