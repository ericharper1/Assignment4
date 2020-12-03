import csv
import re
import sys


# pattern = re.compile(r'ab')
# m = pattern.findall('ab ab ab ab')

# n = ''
# for i in m:
#     n += i + ', '

# print(n)

if len(sys.argv) == 1:
    sys.stdout.write("Usage: %s <access.log> <accesslog.csv>\n" % sys.argv[0])
    sys.exit(0)

log_file_name = sys.argv[1]
csv_file_name = sys.argv[2]

pattern = re.compile(
    r'.\[(?P<datetime>\S+ \+[0-9]{4})]."(?P<httpverb>\S+) (?P<url>\S+) (?P<httpver>\S+)" (?P<status>[0-9]+) (?P<size>\S+) "(?P<referer>.*)" "(?P<useragent>.*)" (?P<latencytime>[0-9]+.[0-9]+)')
file = open(log_file_name, 'r')

with open(csv_file_name, 'w') as out:
    f = open(csv_file_name, 'w')
    f.write("time,verb,url,httpver,status,size,referer,useragent,latency\n")

    for line in file:
        m = pattern.findall(line)
        n = ''
        for i in m:
            for j in i:
                j = j.replace(",", " ")
                n += "'" + j + "'"
                if j != i[-1]:
                    n += ","
        if n:
            f.write(n + '\n')
