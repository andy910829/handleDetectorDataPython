from csv2existgraph import CSV2existGraph
from csv2graph import CSV2Graph
import csv

class Draw:
    def __init__(self,csv_file_list):
        self.csv_file_list = csv_file_list

    def execute(self):
        with open(self.csv_file_list[0], 'r') as f:
            rows = list(csv.reader(f))
            if len(rows) == 4:
                try:
                    self.csv2graph = CSV2Graph(self.csv_file_list)
                    self.csv2graph.execute()
                except:
                    pass
            else:
                try:
                    self.csv2existgraph = CSV2existGraph(self.csv_file_list)
                    self.csv2existgraph.execute()
                except:
                    pass

if __name__ == "__main__":
    draw = Draw(['detectordata-master/labby3/48edc3a5-7155-443a-b2a3-c44954a94529.csv', 'detectordata-master/labby3/4a29d62b-3f1f-44b8-a146-74d2bd987ef4.csv', 'detectordata-master/labby3/86c24f02-741b-4a93-a5f1-37cb52c10ac4.csv', 'detectordata-master/labby3/06a2d298-11f6-4c1b-aab1-2a6d32d6dee3.csv', 'detectordata-master/labby3/6cf2ad3d-1189-4d77-bddf-1d83cd85e33c.csv', 'detectordata-master/labby3/fbc00378-976f-4c6d-8958-fb103628477f.csv', 'detectordata-master/labby3/ba9ce1a6-e541-4ca0-99ab-15943974edf2.csv'])
    draw.execute()