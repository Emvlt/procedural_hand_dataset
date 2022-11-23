import obj_to_array
import matplotlib.pyplot as plt
import pathlib
import time
import numpy as np

def main():
    path_to_obj = 'base_model.obj'
    if pathlib.Path('base_model.npy').is_file():
        print('base_model.npy already exists, Loading saved matrix')
        parsed_array = np.load('base_model.npy')
    else:
        print(f'Parsing {path_to_obj}')
        t0 = time.time()
        parsed_array = obj_to_array.parse_obj_file(path_to_obj,512)
        print(f'Parsed. Elapsed time : {time.time()-t0:.2f} seconds')
        fig, axes = plt.subplots(1,3)
        for i in range(3):
            axes[i].imshow(parsed_array.sum(i))
        plt.show()

if __name__=='__main__':
    main()