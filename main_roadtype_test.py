import os
from test import *
import sys   
from RoadNetwortLable_by_each_road_roadtype import *
from concat_all_label_image_roadtype import *
from GT_post_processing_roadtype import *
from shp2txt_transform_roadtype import *
from mapcompare_roadtype import *
from mapcompare_roadtype_OSM import *
sys.path.append('topology_construction') 
from topology_construction.transform_graph_main_roadtype import *

import glob
import PIL
from PIL import Image
import pandas as pd
import numpy as np
PIL.Image.MAX_IMAGE_PIXELS = None
import datetime

def main():
    print("Hello World")
    #test()
    with open("time_log_roadtype_test.txt","w") as log_f:
        for year in [2017]:
            for county in ['xixiangxian']:
                now_time = datetime.datetime.now()
                shp2txt_transform_roadtype(year,county)
                now_time = datetime.datetime.now()
                log_f.write(county+'   ' +str(year) +'  '+'shp2txt_transform'+ '  '+str(now_time))
                log_f.write('\n')
                mapcompare_roadtype('../temp_output_d500/GraphSamplingToolkit-main',county, 'xyx', 'LCR', year,'d500')
                now_time = datetime.datetime.now()
                log_f.write(county+'   ' +str(year) +'  '+'d500_mapcompare'+ '  '+str(now_time))
                log_f.write('\n')

                mapcompare_roadtype_OSM('../temp_output_OSM/GraphSamplingToolkit-main',county, 'xyx', 'LCR', year+1,'OSM')
                now_time = datetime.datetime.now()
                log_f.write(county+'   ' +str(year) +'  '+'OSM_mapcompare'+ '  '+str(now_time))
                log_f.write('\n')

                print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
                print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
                print(str(county),str(year),'done')
                print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
                print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')


if __name__=="__main__":
    main()