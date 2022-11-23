import obj_to_array
import matplotlib.pyplot as plt
import numpy as np
import time

def main():
    path_to_obj = 'base_model.obj'
    print(f'Parsing {path_to_obj}')
    t0 = time.time()
    parsed_array = obj_to_array.parseObjFile(path_to_obj,512)
    print(f'Parsed. Elapsed time : {time.time()-t0:.2f} seconds')
    fig, axes = plt.subplots(1,3)
    for i in range(3):
        axes[i].imshow(parsed_array.sum(i))
        
    plt.show()

if __name__=='__main__':
    main()