import pandas as pd
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname("..")))
from definitions import ROOT_DIR

# open the json file
with open(ROOT_DIR + "/mopscrapper/mop_details_spider.json", "r") as f:
    data = json.load(f)

df = pd.DataFrame(data)
print(df)

df.info()
