'''
Ultimate accuracy test (UAT)
Goal: easen the accuracy testing via human-visual and aritificially aided tests.

0. Upload the UAT to your github.

1. Implement easy to use visual inspecting tool for assesing the accuracy of depth map
    a) Provide easy to access validation data
    b) Provide method to upload and use tested data
    c) Create the accessable view of comparison
    d) Implement segmented view (if applicable)

2. Implement the tool and metrics to validate the data
    a) Import already used techniques
    b) Search and add new techniques

'''

import shutil
from pathlib import Path
import glob
import matplotlib.pyplot as plt
import cv2

def data_selector(original_path, destination_path, select_interval, format='png'):
'''
    Function for selecting and extracting only the required ammount of data

Input: 
    original_path:      Path to the original folder
    destination_path:   Path to the destination folder
    select_interval:    Every n-th file is selected
    format:             The extention of the files
Output:
    printed message of the result of the operation
'''

    original_files = original_path.glob(f'**/*.{format}')
    copy_iterator = 0
    sum_iterator = 0
    for original_file in original_files:
        if sum_iterator % select_interval == 0:
            destination_file = destination_path/original_file.name
            shutil.copy(original_file, destination_file)
            copy_iterator += 1
        sum_iterator += 1
    print(f'Selected {copy_iterator} of {sum_iterator} files')


def view_samples(images)
    '''
        Function for viewing the images

    Input: 
        images: list of images to display
    Output:
        images are plotted 
    '''

    arrangement_dict = {
        1:  (1, 1),
        2:  (2, 1),
        3:  (2, 2),
        4:  (2, 2),
        5:  (3, 2),
        6:  (3, 2),
        7:  (4, 2),
        8:  (4, 2),
        9:  (3, 3),
        10: (4, 3),
        11: (4, 3),
        12: (4, 3),
    }

    plt.close()
    figure = plt.figure(figsize=(10,7))

    images_count = len(images)
    rows, columns = arrangment_dict.get(images_count)

    for iterator, image in enumerate(images):
        fig.add_subplot(rows, columns, iterator+1)
        plt.imshow(image)
        plt.axis('off')

if __name__ == '__main__':
    images_path = Path(r'D:\test\test_data')
    #test the view samples (initial test required)

