from main.add_insert_block_data import AddBlockData, get_folder_name
from extract_data.print_ffpe_db import PrintFFPEDb
folder, file, user_name = get_folder_name()
add_data = AddBlockData(folder, file, user_name)
add_data.add_ffpe()
print_data = PrintFFPEDb(folder, file, user_name)
print_data.print_file(research = False)
print_data.print_file(research = True)
print('Data files have been created in pccm_db/main/DB/data_output folder')
