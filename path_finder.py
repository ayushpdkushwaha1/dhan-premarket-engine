from pathlib import Path
import os
current_dir = Path(__file__).resolve().parent
path = f"{current_dir}/files/"
def file_delete(filename):
   
    file_path = f"{current_dir}/files/{filename}"

    # चेक करना कि क्या फाइल सच में मौजूद है
    if os.path.exists(file_path):
        os.remove(file_path)
        return True

    return False






