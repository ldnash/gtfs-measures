#-------------------------------------------------------------------------------
# Name:        GTFS Ingest
# Purpose: To ingest a GTFS feed into a sqlite file
#
# Author:      Alex Oberg
#
# Created:     9/12/2016

# Script requries the pygtfs Python module.

# How to install pygtfs:
# Run the following in command line (Assume pip is already installed, you may need to modify Python path)
# C:\Python27\ArcGIS10.3\python.exe -m pip install -U pygtfs


#-------------------------------------------------------------------------------

import datetime
import pygtfs

start_time = datetime.datetime.now()
print('\nStart at ' + str(start_time))

# CONFIG
# Update the following paths as needed
gtfs_feed= r"C:\tasks\2016_09_12_GTFS_ingest\MBTA\MBTA_GTFS.zip"
output_sqlite = r"C:\tasks\2016_09_12_GTFS_ingest\MBTA\mbta_gtfs.sqlite"

# MAIN

#Create blank sqlite file
sched = pygtfs.Schedule(output_sqlite)

#Ingest GTFS feed into sqlite file
pygtfs.append_feed(sched, gtfs_feed)

print ("Done creating sqlite file")

end_time = datetime.datetime.now()
total_time = end_time - start_time
print ("\nEnd at {}.  Total run time {}".format(end_time, total_time))
