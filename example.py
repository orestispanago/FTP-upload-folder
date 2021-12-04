from FTPClient import FTPClient
import datetime
import os

ftp_ip = "YourFTPIP"
ftp_user = "YourFTPUsername"
ftp_password = "YourFTPPassword"
ftp_share = "YourFTPShare"


def make_dirs_if_not_exist(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


now = datetime.datetime.now()
local_folder = now.strftime("%Y/%m/%d")
make_dirs_if_not_exist(local_folder)

with open(f'{local_folder}/myfile.txt', 'w') as fp:
    pass

with FTPClient(ftp_ip, ftp_user, ftp_password, ftp_share) as ftp_client:
    ftp_client.upload_folder(local_folder)
