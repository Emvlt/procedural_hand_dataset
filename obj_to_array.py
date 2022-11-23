import pathlib
import numpy as np
import argparse

def asses_extremums(x:float, x_min:float, x_max:float):
    if x < x_min:
        x_min=x
    elif x_max < x:
        x_max=x
    return x, x_min, x_max

def translate(x:float, x_min:float):
    return x+abs(x_min)

def scale(x:float, x_max:float, scaleFactor:float):
    return int(x*scaleFactor/x_max)

def parse_to_list(file_path='base_model.obj'):
    """parse an .obj file to a list

    Args:
        file_path (str, optional): path to the .obj file. Defaults to 'test.obj'.

    Returns:
        _type_: list of vertices and their respectives _min/_max
    """
    obj_file = open(file_path)
    x_coordinates = []
    y_coordinates = []
    z_coordinates = []
    x_min, x_max = 0, 0
    y_min, y_max = 0, 0
    z_min, z_max = 0, 0
    for line in obj_file:
        if line[0]=='v':
            index1 = line.find(" ") + 1
            index2 = line.find(" ", index1 + 1)
            index3 = line.find(" ", index2 + 1)
            x, y, z = float(line[index1:index2]), float(line[index2:index3]), float(line[index3:-1])
            x, x_min, x_max = asses_extremums(x, x_min, x_max)
            y, y_min, y_max = asses_extremums(y, y_min, y_max)
            z, z_min, z_max = asses_extremums(z, z_min, z_max)
            x_coordinates.append(x)
            y_coordinates.append(y)
            z_coordinates.append(z)

    return x_coordinates, y_coordinates, z_coordinates, (x_min, x_max), (y_min, y_max), (z_min, z_max)

def parse_obj_file(file_path=pathlib.Path('base_model.obj'), mat_size = 512, save=False) -> np.uint8:
    """Parse a .obj file to a numpy array

    Args:
        file_path (str, optional): path to the .obj file. Defaults to 'test.obj'.
        mat_size (int, optional): array sizes, works well with 512. Defaults to 512.

    Returns:
        np.uint8: parsed array
    """
    x_coordinates, y_coordinates, z_coordinates, (x_min, x_max), (y_min, y_max), (z_min, z_max) = parse_to_list(file_path)
    x_diff = x_max-x_min
    y_diff = y_max-y_min
    z_diff = z_max-z_min
    d_max = max([x_diff, y_diff, z_diff])
    a = int(mat_size*y_diff/d_max)
    b = int(mat_size*z_diff/d_max)
    c = int(mat_size*x_diff/d_max)
    mat = np.zeros((mat_size,mat_size,mat_size), np.uint8)
    for x,y,z in zip(x_coordinates, y_coordinates, z_coordinates):
        x_ = scale(translate(x, x_min), x_diff, c-1)
        y_ = scale(translate(y, y_min), y_diff, a-1)
        z_ = scale(translate(z, z_min), z_diff, b-1)
        mat[mat_size-1-y_, int((mat_size-b)/2)+z_, int((mat_size-c)/2)+x_] = 1
    if save:
        np.save(file_path.rename(file_path.with_suffix('.npy')))
    return mat

def main():
    file_path = pathlib.Path(args.file_path)
    parse_obj_file(file_path)

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path', required=False, type=str, default= 'base_model.obj')
    args = parser.parse_args()
    main(args)


