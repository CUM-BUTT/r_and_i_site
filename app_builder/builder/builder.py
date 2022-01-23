import datetime
import shutil
from pathlib import Path
import json
from PIL import Image
from PIL.JpegImagePlugin import JpegImageFile
from django.core.files.uploadedfile import InMemoryUploadedFile


class Builder:
    template_project_path: Path
    new_project_path: Path
    image_path: Path
    sudo_pass: str

    """
    {
    'url': 'https://www.youtube.com/', 'mail': 'cum_butt@mail.ru', 
    'name': 'randi_app', 'app_id': 'randi_id', 
    'promo_code': '1488',
    }
    """
    app_data: dict
    image: JpegImageFile

    def __init__(self, app_data: dict, image: InMemoryUploadedFile):
        self.app_data = app_data
        self.image: JpegImageFile = Image.open(image)
        self.new_project_path = Path('expo/apps') / app_data['name'] / f'{datetime.datetime.now()}'

    def SetImageToApp(self):
        with open(self.new_project_path / 'image', 'wb') as f:
            self.image.save(f)

    def SetConfigToApp(self):
        with open(self.new_project_path, 'w') as f:
            json.dump(self.app_data, f,)

    def MakeTemplateCopy(self):
        shutil.copy(self.template_project_path, self.new_project_path)

    def Build(self,):
        self.new_project_path.mkdir()

        self.MakeTemplateCopy()
        self.SetConfigToApp()
        self.SetImageToApp()
