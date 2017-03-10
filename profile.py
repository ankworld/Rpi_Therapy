import configparser
import os


class Profile(object):
    def __init__(self):
        self.path = os.path.dirname(
            os.path.abspath(__file__)) + "/config/profile/"
        self.cfg = configparser.ConfigParser()
        if os.path.isdir(self.path):
            pass
        else:
            os.mkdir(self.path, 0o777)

    def add(self, section, spd):
        self.cfg['profile'] = {}
        self.cfg['profile']['section1'] = section[0]
        self.cfg['profile']['section2'] = section[1]
        self.cfg['profile']['speed'] = spd

    def write_config(self):
        i = 0
        while os.path.exists(self.path + "profile%s.ini" % i):
            i += 1
        with open(self.path + 'profile%s.ini' % i, 'w') as config_file:
            self.cfg.write(config_file)

    """
    :arg file = abspath
    """

    def read_config(self, file):
        self.cfg.read(file)
        list_config = [self.cfg['profile']['section1'],
                       self.cfg['profile']['section2'],
                       self.cfg['profile']['speed']]
        return list_config

    """
    load all file in path = config/profile
    :return list of file(abspath) in config/profile
    """

    def load_file(self):
        list_file = []
        for file in os.listdir(self.path):
            list_file.append(self.path + file)
        list_file.sort()
        return list_file
