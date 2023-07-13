# import matplotlib.pyplot as plt
# import csv
# from pprint import pprint


# class CSV2existGraph:
#     def __init__(self):
#         self.csv_file = 'humanExistdata.csv'
#         self.speed = []
#         self.dis_static = []
#         self.static_val = []
#         self.dynamic_val = []
#         self.dis_move = []
#         self.y_axis = []
#         self.swap_dict = {
#             "speed": self.speed,
#             "dis_static": self.dis_static,
#             "static_val": self.static_val,
#             "dynamic_val": self.dynamic_val,
#             "dis_move": self.dis_move
#         }
#         self.data_len = {
#             "speed": 0,
#             "dis_static": 0,
#             "static_val": 0,
#             "dynamic_val": 0,
#             "dis_move": 0
#         }

#     def execute(self):
#         with open(self.csv_file, 'r') as f:
#             rows = list(csv.reader(f))
#             for row in rows:
#                 key = row[0]
#                 data = [int(value) for value in row[1:]]
#                 self.swap_dict[key] = data
#                 self.data_len[key] = len(data)
#             self.show()

#     def show(self):
#         _, axs = plt.subplots(3, 2)
#         plt.subplots_adjust(hspace=0.4)
#         row_list = [0, 1, 0, 1, 0, 1]
#         col_list = [0, 0, 1, 1, 2, 2]
#         cnt = 0
#         for key, data in self.swap_dict.items():
#             # row = i // 2  # 012
#             # col = i % 2  # 01
#             row = row_list[cnt]
#             col = col_list[cnt]
#             self.y_axis = [i for i in range(self.data_len[key])]
#             # axs[row, col].set_ylim(0, 100)
#             # axs[row, col].set_ylim(0, 25)
#             axs[row, col].plot(self.y_axis, data)
#             axs[row, col].set_xlabel('time')
#             axs[row, col].set_ylabel(key)
#             axs[row, col].set_title(key)
#             cnt += 1
#         plt.show()


# if __name__ == "__main__":
#     csv2existgraph = CSV2existGraph()
#     csv2existgraph.execute()

import matplotlib.pyplot as plt
import csv


class CSV2existGraph:
    def __init__(self, csv_file_list):
        self.csv_file_list = csv_file_list
        self.speed = []
        self.dis_static = []
        self.static_val = []
        self.dynamic_val = []
        self.dis_move = []
        self.swap_dict = {
            "speed": self.speed,
            "dis_static": self.dis_static,
            "static_val": self.static_val,
            "dynamic_val": self.dynamic_val,
            "dis_move": self.dis_move
        }

    def execute(self):
        data = list()
        for csv_file in self.csv_file_list:
            with open(csv_file, 'r') as f:
                rows = list(csv.reader(f))
                for row in rows:
                    key = row[0]
                    data = [int(value) for value in row[1:]]
                    self.swap_dict[key] += data
        self.show()

    def show(self):
        fig = plt.figure(figsize=(10, 12))
        titles = ["speed", "dis_static",
                  "static_val", "dynamic_val", "dis_move"]
        for i in range(5):
            key = titles[i]
            data = self.swap_dict[key]
            y_axis = [i for i in range(len(data))]
            ax = fig.add_subplot(3, 2, i+1)
            ax.plot(y_axis, data)
            ax.set_xlabel('time')
            ax.set_ylabel(key)
            ax.set_title(key)
        plt.subplots_adjust(hspace=0.45)  # 调整垂直间距
        plt.show()


if __name__ == "__main__":
    csv2existgraph = CSV2existGraph()
    csv2existgraph.execute()
