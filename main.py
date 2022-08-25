#########################################Задание-1###############################################
import requests

def requests_hero():
    intelligence = 0
    heroes_list = ['Hulk', 'Captain America', 'Thanos']
    url = "https://akabab.github.io/superhero-api/api"
    response = requests.get(url + '/all.json').json()
    for heroes in response:
        if heroes['name'] in heroes_list and heroes['powerstats']['intelligence'] > intelligence:
            intelligence = heroes['powerstats']['intelligence']
            most_intelligence_hero = heroes['name']
    print(f'самый умный супергерой - {most_intelligence_hero}')


#########################################Задание-2###############################################
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, file_path: str, file_list):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        for files in file_list:
            href = self.get_upload_link(disk_file_path=file_path + files).get("href", "")
            response = requests.put(href, data=open(files, 'rb'))
            if response.status_code == 201:
                print("Success")

if __name__ == '__main__':
    requests_hero()

    path_to_file = "netology/"
    token = ""
    file_list = ["test.txt", "test1.txt", "test2.txt"]
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file, file_list)