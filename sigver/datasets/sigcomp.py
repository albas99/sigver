import os
from sigver.datasets.base import IterableDataset
from skimage.io import imread
from skimage import img_as_ubyte


class SIGCOMPCHINESE(IterableDataset):
    """ Helper class to load SigComp Chinese Dataset
    """

    def __init__(self, path='./Datasets/sigComp2011/trainingSet/Chinese' extension='.png'):
        self.path = path
        self.users = list(range(1, 10+1))
        self.extension = extension

    @property
    def genuine_per_user(self):
        return 24
    @property
    def forged_per_user(self):
        return 12

    @property
    def maxsize(self):
        return 463, 1117

    def get_user_list(self):
        return self.users

    def iter_genuine(self, user):
        """ Iterate through genuine signatures """
        #
        genuine_folder = os.path.join(self.path, 'Genuine')
        files = ['{}_{}{}'.format(user, img, extension) for img in range(1, 24)]
        for i in genuine_folder:
            full_path = os.path.join(genuine_folder, i)
            img = imread(full_path, as_gray=True)
            yield img_as_ubyte(img), i

    def iter_forgery(self, user):
        """ Iterate over forgeries """
        forge_folder = os.path.join(self.path, 'Forgeries')
        files = ['{}_{}{}'.format(user, img, extension) for img in range(1, 12)]
        for i in forge_folder:
            full_path = os.path.join(forge_folder, i)
            img = imread(full_path, as_gray=True)
            yield img_as_ubyte(img), i
