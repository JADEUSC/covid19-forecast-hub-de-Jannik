# Auto-download any Github/Gitlab raw file and save it with custom name
# Jakob Ketterer, November 2020

import urllib.request
import os

if __name__ == "__main__":
    
    # url = "https://raw.githubusercontent.com/uclaml/ucla-covid19-forecasts/master/projection_result/pred_world_02-06.csv"
    url = "https://ihmecovid19storage.blob.core.windows.net/archive/2021-02-20/ihme-covid19.zip"
    file_name = "ihme-covid19.zip"
    dir_name = os.path.join("./data-raw/UCLA-SuEIR", file_name)

    urllib.request.urlretrieve(url, dir_name)
    print("Downloaded and saved forecast to", dir_name)

    # try:
    #     urllib.request.urlretrieve(url, dir_name)
    #     print("Downloaded and saved forecast to", dir_name)
    # except:
    #     print("Download failed for", file_name, ". The file probably doesn't exist.")
