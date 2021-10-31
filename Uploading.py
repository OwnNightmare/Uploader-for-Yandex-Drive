from YADriveAPI import YaUploader
from YADriveAPI import Token


user_token = input('Введите ваш токен: ')
file_path = input('Введите путь до файла на компьютере: ')
drive_path = input('Путь для файла на ЯндексДиске: ')
split_path = file_path.split('\\')
file_name = split_path[-1]
print(drive_path)
print(file_name)

uploader = YaUploader(token=Token)
uploader.upload_file_to_drive(f'{drive_path}/{file_name}', f'{file_path}')

# ya.upload_file_to_drive('Education/type.txt', 'typ.txt')
# print('Hi')