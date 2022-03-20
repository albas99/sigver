import os
from sigver.datasets.base import IterableDataset
from skimage.io import imread
from skimage import img_as_ubyte


class SIGCOMPCHINESE(IterableDataset):
    """ Helper class to load SigComp Chinese Dataset
    """

    def __init__(self, path='./Datasets/sigComp2011/trainingSet/Chinese', extension='png'):
        self.path = path
        self.users = [int(user) for user in os.listdir(self.path)]
        self.extension = extension

    # @property
    # def genuine_per_user(self):
    #     return
    # @property
    # def forged_per_user(self):
    #     return

    @property
    def maxsize(self):
        return 463, 1117

    def get_user_list(self):
        return self.users

    def iter_genuine(self, path):
        """ Iterate through genuine signatures """
        #
        genuine_folder = os.path.join(self.path, 'Genuine')
        # files = ['{}'.format()]
        for i in genuine_folder:
            full_path = os.path.join(genuine_folder, i)
            img = imread(full_path, as_gray=True)
            yield img_as_ubyte(img), i

    def iter_forgery(self, path):
        """ Iterate over forgeries """
        forge_folder = os.path.join(self.path, 'Forgeries')
        # files = ['{}'.format()]
        for i in forge_folder:
            full_path = os.path.join(forge_folder, i)
            img = imread(full_path, as_gray=True)
            yield img_as_ubyte(img), i
