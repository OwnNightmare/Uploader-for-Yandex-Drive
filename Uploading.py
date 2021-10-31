from YADriveAPI import YaUploader
from YADriveAPI import Token


os_type = 'unknown'
while os_type not in ['Win', 'Windows', 'Unix', 'Linux']:
    os_type = input('Вид вашей ОС ("Win" - Windows, "Unix"- Unix, Linux): ').capitalize()
file_path = input('Путь до файла на компьютере: ')
if os_type in ['Win', 'Windows']:
    split_path = file_path.split('\\')
else:
    split_path = file_path.split('/')
file_name = split_path[-1]
user_token = input('Yandex токен: ')
drive_path = input('Путь для файла на ЯндексДиске: ')

uploader = YaUploader(token=user_token)
response = uploader.upload_file_to_drive(f'{drive_path}/{file_name}', f'{file_path}')
print(response)
