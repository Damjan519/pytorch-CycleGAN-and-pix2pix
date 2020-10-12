import os
import cv2

def getDawgz(_input_dir):
    '''
    Returns array of dawg images within a given directory.
    '''
    dawgz = []

    for r, _, f in os.walk(f'{_input_dir}'):
        for file in f:
            dawgz.append(os.path.join(r, file))

    return dawgz


def filterDawgz(input_dir, output_dir):
    '''
    Applies canny filter to provided array of images.
    '''
    images = getDawgz(input_dir)

    for i in images:
        image_name = i[i.rfind('/') + 1:]
        image = cv2.imread(i)
        canny = cv2.Canny(image, 60, 120)

        cv2.imwrite(f'{output_dir}/{image_name}', canny)


def resizeDawgz(x_dim, y_dim, input_dir, output_dir):
    '''
    Resizes provided array of images to desired dimensions.
    '''
    images = getDawgz(input_dir)

    for i in images:
        image_name = i[i.rfind('/') + 1:]
        image = cv2.imread(i)
        dim = (x_dim, y_dim)
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

        cv2.imwrite(f'{output_dir}/{image_name}', resized)


if __name__ == '__main__':
    image_path = '/home/iruvinov/Dev/ganMan/playground/pix-2-pix-split/datasets/dawgz/images'

    filterDawgz(f'{image_path}/orig', f'{image_path}/orig_f')
    resizeDawgz(256, 256, f'{image_path}/orig', f'{image_path}/256')
    filterDawgz(f'{image_path}/256', f'{image_path}/256_f')
