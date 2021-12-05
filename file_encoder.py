import pyAesCrypt
import os


def encryption(file, password):

    buffer_size = 1024 * 1024

    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )
    os.remove(file)

def walking_by_dirs(dir, password):

    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        else:
            walking_by_dirs(path, password)


password = input("Enter Your Password: ")
walking_by_dirs(r"path name", password)