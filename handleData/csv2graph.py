import matplotlib.pyplot as plt
import csv
from pprint import pprint


class CSV2Graph:
    def __init__(self, csv_file_list):
        self.csv_file_list = csv_file_list
        self.heart_rate = []
        self.breath_rate = []
        self.bodysign_val = []
        self.distance = []
        self.y_axis = []
        self.swap_dict = {
            "heart_rate": self.heart_rate,
            "breath_rate": self.breath_rate,
            "bodysign_val": self.bodysign_val,
            "distance": self.distance
        }
        self.data_len = {
            "heart_rate": 0,
            "breath_rate": 0,
            "bodysign_val": 0,
            "distance": 0
        }

    def execute(self):
        for csv_file in self.csv_file_list:
            with open(csv_file, 'r') as f:
                rows = list(csv.reader(f))
                for row in rows:
                    key = row[0]
                    data = [int(value) for value in row[1:]]
                    self.swap_dict[key] += data
                    self.data_len[key] += len(data)
        self.show()

    def show(self):
        _, axs = plt.subplots(2, 2)
        plt.subplots_adjust(hspace=0.4)
        i = 0
        for key, data in self.swap_dict.items():
            row = i // 2
            col = i % 2
            self.y_axis = [i for i in range(self.data_len[key])]
            if (row == 0 or row == 1) and col == 0:
                axs[row, col].set_ylim(0, 100)
            elif row == 0 and col == 1:
                axs[row, col].set_ylim(0, 25)
            axs[row, col].plot(self.y_axis, data)
            axs[row, col].set_xlabel('time')
            axs[row, col].set_ylabel(key)
            axs[row, col].set_title(key)
            i += 1
        plt.show()


if __name__ == "__main__":
    csv2graph = CSV2Graph()
    csv2graph.execute()
