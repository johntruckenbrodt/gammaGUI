import xml.etree.cElementTree as ET
from auxilliary.environment import Environment

class ReadEnv:
    """
    This is the Class of ReadEnv. This Class contain a universal Method to Read the WorkEnv.xml File and returns a tuple of the Values
    """

    def __init__(self):
        my_ENV = Environment()
        my_ENV = my_ENV.WorkEnv
        self.tree = ET.parse(my_ENV)

    def read_env(self):
        """
        This Function roots the WorkEnv.xml File and returns a tuple. The Order is defined in environment.Environment.set_wdir()
            - 0. wdir
            - 1. idir
            - 2. tdir
            - 3. odir
            - 4. WorkEnv.xml path
            - 5. backgroundimage path
            - 6. GammaCommands.xml path
        :return: WorkEnv tuple
        """
        doc = self.tree
        root = doc.getroot()
        my_list = list()

        for i in range(0,len(root.getchildren())):
            my_list.append(root[i].text)

        my_tuple = tuple(my_list)

        # print(my_list)
        # print(my_tuple)
        # print(len(root.getchildren()))
        #return my_list
        return my_tuple

if __name__ == '__main__':
    t = ReadEnv()
    print(t)
    t.read_env()

