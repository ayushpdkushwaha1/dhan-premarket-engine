import openpyxl
from path_finder import current_dir

# 1. DATA READ KARNE KE LIYE
def xlsx_value( position_row_and_column,file_name):
    position_row_and_column = position_row_and_column.upper()
    wb = openpyxl.load_workbook(f"{current_dir}/files/{file_name}")
    kkkk = wb.active[position_row_and_column].value
    return kkkk

# 2. DATA UPDATE KARNE KE LIYE
def xlsx_update(position_row_and_column, new_value,file_name):
    wb = openpyxl.load_workbook(f"{current_dir}/files/{file_name}")
    wb.active[position_row_and_column.upper()] = new_value
    wb.save(f"{current_dir}/files/{file_name}")




def xlsx_create(name):
    """एक बिल्कुल खाली (Blank) .xlsx फ़ाइल क्रिएट करने के लिए।"""
    file_path = f"{current_dir}/files/{name}"

    # एक नया खाली वर्कबुक बनाना
    wb = openpyxl.Workbook()

    # फ़ाइल को सेव करना
    wb.save(file_path)

    return True


# --- इस्तेमाल करने का तरीका ---
# xlsx_create("my_blank_sheet.xlsx")

# --- AAPKA TESTING CODE ---
# xlsx_update("file.xlsx", 'A1','Hldgyghggjkhjk,,l;,!') #example for update xlsx file
# xlsx_value("file.xlsx", 'kb10') #example for read xlsx file
# print(xlsx_value("file.xlsx", 'A1')) #example for read xlsx file
