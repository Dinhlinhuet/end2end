import pickle
from matplotlib import pyplot as plt

images, labels = pickle.load(open('/media/warrior/Ubuntu/'
                                 'corp_workspace/hw_data/datajohn/dataloader_grayscale/latin_number.pkl','rb'))
for i in range(10):
    plt.imshow(images[i])
    plt.show()
    print('labels', len(labels[i]))