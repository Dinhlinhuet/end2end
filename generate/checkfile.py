import pickle
from matplotlib import pyplot as plt

def checkfile(filename):
    images, labels = pickle.load(open(filename,'rb'))
    for i in range(len(labels)):
        # plt.imshow(images[i])
        # plt.show()
        # print('labels', len(labels[i]))
        print(labels[i])
    # print(labels)

# filename = '/media/warrior/Ubuntu/corp_workspace/hw_data/datajohn/dataloader_grayscale/latin_number.pkl'
filename = '/media/warrior/Ubuntu/corp_workspace/data_gen/dev/images.pkl'
checkfile(filename)