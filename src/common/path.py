from os.path import join, dirname, abspath

BASE_PATH = dirname(dirname(abspath(__file__)))


def project_path(*args):
    return join(BASE_PATH, *args)

