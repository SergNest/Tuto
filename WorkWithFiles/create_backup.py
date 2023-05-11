import shutil


def create_backup(path, file_name, employee_residence):
    with open(path +'/'+file_name, 'wb') as file:
        for username, password in employee_residence.items():
            user_info_str = f"{username} {password}".encode('utf-8')
            file.write(user_info_str + b'\n')
        
        archive_name = shutil.make_archive('backup_folder', 'zip', path)
    return archive_name


print(create_backup('WorkWithFiles', 'employs', {'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'}))
