from add_edit.output_excel import OutputData, define_path

user_name = input('Please input username: ')
print_file = OutputData(define_path(), user_name)
print_file.output_data()

