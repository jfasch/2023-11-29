import sys
import csv
import datetime
import matplotlib.pyplot as plt

filename = sys.argv[1]

f = open(filename, encoding='utf-16')
rdr = csv.reader(f, delimiter='\t')

timestamps = []
mpleft_1s = []
mpleft_2s = []

for lineno, row in enumerate(rdr):
    if lineno == 0:
        continue

    timestamp_str = row[1]
    mpleft_1 = float(row[2])
    mpleft_2 = float(row[3])

    # parse as "01.03.2022 11:10:48"
    dt = datetime.datetime.strptime(timestamp_str, '%d.%m.%Y %H:%M:%S')

    timestamps.append(dt.timestamp())
    mpleft_1s.append(mpleft_1)
    mpleft_2s.append(mpleft_2)

plt.plot(timestamps, mpleft_1s)
plt.plot(timestamps, mpleft_2s)

plt.show()
