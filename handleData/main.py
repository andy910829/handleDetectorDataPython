import json
from draw import Draw
from pprint import pprint

class Main:
    def __init__(self):
        self.json_file = "detectordata-master/board.json"
        self.csv_file_dict = dict()
        self.csv_file_cnt = 0

    def read_json(self):
        self.csv_file_cnt = int(input("輸入要讀取的csv檔案數量:"))
        with open(self.json_file) as f:
            self.csv_file_dict = json.load(f)
        self.get_csv_psth()

    def get_csv_psth(self):
        for _,csv_files in self.csv_file_dict.items():
            self.read_csv(csv_files)

    def read_csv(self,csv_files):
        data_csv_list = list()
        cnt = 0
        for csv_file in csv_files:
            if cnt < self.csv_file_cnt:
                csv_file_list = csv_file.split("/")[-2:]
                string = "detectordata-master/"
                string += '/'.join(csv_file_list)
                data_csv_list.append(string)
                cnt += 1
            else:
                Draw(data_csv_list).execute()
                pprint(f"當前檔案為{data_csv_list}")
                check = input("是否繼續讀取csv檔案?(y/n)")
                if check == "y":
                    cnt = 0
                    data_csv_list.clear()
                else:
                    break



 




if __name__ == '__main__':
    main = Main()
    main.read_json()