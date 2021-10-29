import requests
from pprint import pprint

Token = 'AQAAAAA6yPHbAADLWyR9_imZMk2rtk6TUiscs0M'


class YandexDisk:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_files_list(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(url=url, headers=headers)
        return response.json()

    def get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': True}
        response = requests.get(url=upload_url, params=params, headers=headers)
        pprint(response.json())
        return response.json()

    def upload_file_to_drive(self, disk_file_path, filename):
        response = self.get_upload_link(disk_file_path=disk_file_path)
        url = response.get('href', '')
        response = requests.put(url=url, data=open(filename, 'rb'))


ya = YandexDisk(token=Token)
ya.upload_file_to_drive('Education/type.txt', 'typ.txt')