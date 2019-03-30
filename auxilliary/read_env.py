import xml.etree.cElementTree as ET
from auxilliary.environment import Environment

class ReadEnv:
    """
    This is the Class ReadEnv.
    It contains a universal Method to read the WorkEnv.xml File and returns the stored Values
    """

    def __init__(self):
        my_ENV = Environment()
        my_ENV = my_ENV.WorkEnv
        self.tree = ET.parse(my_ENV)

    def read_env(self):
        """
        This Method reads the WorkEnv.xml and returns a tuple of the Entries.
        The order is defined in environment.Environment.set_wdir():
            - 0. wdir path
            - 1. idir path
            - 2. tdir path
            - 3. odir path
            - 4. WorkEnv.xml path
            - 5. backgroundimage path
            - 6. GammaCommands.xml path
        :return: tuple of WorkEnv.xml
        """
        doc = self.tree
        root = doc.getroot()
        my_list = list()

        for i in range(0,len(root.getchildren())):
            my_list.append(root[i].text)

        my_tuple = tuple(my_list)
        #return my_list
        return my_tuple

if __name__ == '__main__':
    t = ReadEnv()
    print(t)
    t.read_env()

