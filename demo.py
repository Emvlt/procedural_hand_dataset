import obj_to_array
import matplotlib.pyplot as plt
import pathlib
import time
import numpy as np
import argparse

def main():
    numpy_file_path = pathlib.Path(args.file_path).with_suffix('.npy')
    if numpy_file_path.is_file():
        print('base_model.npy already exists, Loading saved matrix')
        parsed_array = np.load(numpy_file_path)
    else:
        print(f'Parsing {args.file_path}')
        t0 = time.time()
        parsed_array = obj_to_array.parse_obj_file(args.file_path,512)
        print(f'Parsed. Elapsed time : {time.time()-t0:.2f} seconds')
        fig, axes = plt.subplots(1,3)
        for i in range(3):
            axes[i].imshow(parsed_array.sum(i))
        plt.show()

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path', required=False, type=str, default= 'base_model.obj')
    args = parser.parse_args()
    main(args)