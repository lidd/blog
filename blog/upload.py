import json
import datetime
import os
import uuid

from django.http import HttpResponse

from my_blog import settings


def upload_image(files, dir_name):
    allow_suffix = ['jpg', 'png', 'jpeg', 'bmp']
    file_suffix = files.name.split(".")[-1]
    if file_suffix not in allow_suffix:
        return {'error': 1, 'message': 'Illegal image type!'}
    relative_path_file = upload_makedir(dir_name)
    path = os.path.join(settings.MEDIA_ROOT, relative_path_file)
    if not os.path.exists(path):
        os.makedirs(path)
    file_name = str(uuid.uuid1()) + "." + file_suffix
    path_file = os.path.join(path, file_name)
    file_url = settings.MEDIA_URL + relative_path_file + file_name
    open(path_file, 'wb').write(files.file.read())
    return {'error': 0, 'url': file_url}


def image_upload(request, dir_name):
    result = {"error": 1, "message": "upload error!"}
    files = request.FILES.get("imgFile", None)
    if files:
        result = upload_image(files, dir_name)
    return HttpResponse(json.dumps(result), content_type="application/json")


def upload_makedir(dir_name):
    today = datetime.datetime.today()
    dir_name += '/%d/%d' % (today.year, today.month)
    if not os.path.exists(settings.MEDIA_ROOT + '/' + dir_name):
        os.makedirs(settings.MEDIA_ROOT + '/' + dir_name)
    return dir_name
