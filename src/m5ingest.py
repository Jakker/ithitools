#!/usr/bin/python
import sys
import os
import json
from os import walk
#from os import path

class m5_summary:
    def __init__(self):
        self.i_count = 0
        self.i_total = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.key_list = ["M5.1.1", "M5.1.2", "M5.1.3", "M5.1.4", "M5.1.5", "M5.1.6",
           "M5.2.1", "M5.2.2", "M5.2.3", "M5.3.1", "M5.3.2", "M5.4.1",
           "M5.4.2","M5.5"]
        self.sub_met = ["M5.1", "M5.1", "M5.1", "M5.1", "M5.1", "M5.1",
           "M5.2", "M5.2", "M5.2", "M5.3", "M5.3", "M5.4",
           "M5.4","M5.5"]
        self.sub_entry = [1, 2, 3, 4, 5, 6, 1, 2, 3, 1, 2, 1, 2, 0]
    
    def add_to_summary (self, f_name):
        "Parse a JSON file and add the results to the summary"
        with open(f_name) as m5_file :
            self.i_count += 1
            m5_text = m5_file.read()
            m5_data = json.loads(m5_text)
            i = 0
            while i < len(self.key_list) :
                self.i_total[i] += m5_data[0][self.key_list[i]]
                i += 1
            m5_file.close()
    
    def average(self):
        "Divide the results by the number of summaries counted"
        if (self.i_count > 1) :
            i = 0
            while i < len(self.key_list) :
                self.i_total[i] /= self.i_count;
                i += 1
            self.i_count = 1
    
    def save_as_csv(self, f_name):
        "Save the summary as a CSV file"
        csv_file = open(f_name, "w")
        i = 0
        while i < len(self.key_list):
            entry = "";
            if (self.sub_entry[i] != 0) :
                entry = str(self.sub_entry[i]);
            csv_file.write(self.sub_met[i] + ", " + entry + ", " + str(self.i_total[i]) + ",\n")
            i += 1
        csv_file.close()

# Main 

summary = m5_summary()
mypath = sys.argv[1]
for (dirpath, dirnames, filenames) in walk(mypath):
    print("Found dir:" + dirpath);
    for file_name in filenames :
        if (file_name.startswith("m5-")):
            file_path = os.path.join(dirpath, file_name)
            print("Found " + file_path)
            summary.add_to_summary(file_path)
print("Found " + str(summary.i_count) + " summaries.")
summary.average()
i = 0
while i < len(summary.key_list) :
    print("m5[" + summary.key_list[i] + "] = " + str(summary.i_total[i]))
    i += 1
summary.save_as_csv(sys.argv[2])