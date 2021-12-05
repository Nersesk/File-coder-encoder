import pyAesCrypt
import os


def decryption(file, password):

    buffer_size = 1024 * 1024

    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )
    os.remove(file)

def walking_by_dirs(dir, password):

    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        else:
            walking_by_dirs(path, password)


password = input("Enter Your Password: ")
walking_by_dirs(r"path address", password)