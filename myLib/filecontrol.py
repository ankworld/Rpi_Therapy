import datetime as dt

class configHandle(object):

    def save(self, string):
        fo = open("config/Motor.conf", mode='w',
                  buffering=-1, encoding="UTF-8")
        fo.write(string)
        fo.close()
        pass

    def load(self):
        fo = open("config/Motor.conf", mode='r',
                  buffering=-1, encoding="UTF-8")
        multiLine = fo.readlines()
        print(multiLine)
        fo.close()
        pass


class logging(object):

    def save(self):
        now = dt.datetime.now()
        string = "[ " + str(now) + " ]"
        print(string)

        ##############################################
        # Open a file
        fo = open("foo.txt", "a+")

        # Write a file
        fo.write(string + "\n")

        # Read a file
        # str = fo.readline()
        # print(str)

        # Close opened file
        fo.close()
        ###############################################
        pass
