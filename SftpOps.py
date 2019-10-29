import pysftp
import os
from os import listdir


def Transfer_All_File(dirPath, ftpDir="/tmp/ValTeamPain001", privateKey="C:/Users/Lakshmi.Mokara/Downloads/sftpKey"):
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    with pysftp.Connection(host="ip-10-87-16-103.eu-west-1.compute.internal", username="ec2-user", private_key=privateKey, cnopts=cnopts) as sftp:
        # Folder, in which the files are present to upload
        localFilePath = dirPath
        sftp.cwd(ftpDir)  # Destination directory in ftp site
        src_files = os.listdir(localFilePath)
        for file_name in src_files:
            full_file_name = os.path.join(localFilePath, file_name)
            sftp.put(full_file_name)
        sftp.close()


def Transfer_Single_File(filePath, ftpDir="/tmp/ValTeamPain001", privateKey="C:/Users/Lakshmi.Mokara/Downloads/sftpKey"):
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    with pysftp.Connection(host="ip-10-87-16-103.eu-west-1.compute.internal", username="ec2-user", private_key=privateKey, cnopts=cnopts) as sftp:
        # Folder, in which the files are present to upload
        localFilePath = filePath
        sftp.cwd(ftpDir)  # Destination directory in ftp site
        sftp.put(localFilePath)
        sftp.close()
