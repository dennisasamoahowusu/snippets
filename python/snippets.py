import numpy as np
import matplotlib.pyplot as plt


def read_floats_from_file_into_list(input_file):
    with open(input_file) as f:
        data = f.read().splitlines()
        data = [float(i) for i in data]
    return data


# import numpy as np
def convert_list_to_numpy_array(list):
    return np.asarray(list)


# import numpy as np
# import matplotlib.pyplot as plt
def plot_scatter_two_lists(list1, list2, list1_label, list2_label):
    x = np.asarray(list1).reshape(-1, 1)
    y = np.asarray(list2).reshape(-1, 1)
    plt.scatter(x, y)
    plt.xlabel(list1_label)
    plt.ylabel(list2_label)
    plt.title('ECE Outputs')
    fig_size = plt.rcParams["figure.figsize"]
    fig_size[0] = 12
    fig_size[1] = 12
    plt.rcParams["figure.figsize"] = fig_size
    plt.show()
