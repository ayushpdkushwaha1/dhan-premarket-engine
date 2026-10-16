import requests
from path_finder import current_dir

# --- 1. स्पेसिफिक CSV डाउनलोड करने का फंक्शन ---
def download_csv(custom_filename):
    url = "https://images.dhan.co/api-data/api-scrip-master-detailed.csv"
    final_path = f"{current_dir}/files/{custom_filename}"

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0"
        }
        
        # स्ट्रीम मोड में डाउनलोड (बिना क्रोमियम खोले)
        response = requests.get(url, headers=headers, stream=True, timeout=60)
        
        if response.status_code == 200:
            with open(final_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024 * 1024): # 1MB चंक्स
                    if chunk:
                        f.write(chunk)
            return True
        return False
    except Exception:
        return False


# --- 2. यूनिवर्सल डाउनलोड फंक्शन (किसी भी लिंक के लिए) ---
def download_anything(url, custom_filename_your_current_dir_auto_detect):
    final_path = f"{current_dir}/files/{custom_filename_your_current_dir_auto_detect}"

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0"
        }
        
        # स्ट्रीम मोड में डाउनलोड
        response = requests.get(url, headers=headers, stream=True, timeout=120)
        
        if response.status_code == 200:
            with open(final_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        f.write(chunk)
            return True
        return False
    except Exception:
        return False