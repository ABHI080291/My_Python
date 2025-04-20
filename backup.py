import shutil
import datetime
import os

def backup_files(source,destination):
    today = datetime.date.today()
    backup_files_name = os.path.join(destination,f"backup_{today}.zip")
    shutil.make_archive(backup_files_name.replace('.zip',''),'zip',source)

source = "E:\\Python\\Basic Python"
destination = "E:\\Python\\backup"

backup_files(source,destination)

