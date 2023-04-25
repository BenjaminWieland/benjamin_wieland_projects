# Analyze an Apache log report
# Import the log file
import json
with open ("apache_logs", "r") as fh:
    #apache_logs = fh.read()
    logs_list = []
    for line in fh:
        line = line.strip()
        logs_list.append(line)

# Get first line and status code
first_line = logs_list[0].split(" ")
http = first_line[8]

# Extract status codes and count them
status_codes = []
for i in logs_list:
    i = i.split(" ")
    status_codes.append(i[8])

status_200 = len([i for i in status_codes if i == "200"])
status_404 = len([i for i in status_codes if i == "404"])

from collections import Counter
count_http = Counter(status_codes)

# Trouble shooting for failed status codes
list404 = []
for i in logs_list:
    i = i.split(" ")
    list404.append(i)
lines_with_404 = list(filter(lambda x : x[8] == "404", list404))

resource_list = []
for i in lines_with_404:
    resource_list.append(i[10])
count_resource_list = Counter(resource_list)
print(count_resource_list)

# Create log report with pdf
from log_pdf import PDF
import seaborn as sns
sns.set_theme()
sns_plot = sns.histplot(data = status_codes)
sns_plot.figure.savefig('status_codes.png')
sns_plot.figure.clf()

sns_plot = sns.histplot(data = resource_list)
sns_plot.figure.savefig('resource_list.png')
sns_plot.figure.clf()
plots = ["status_codes.png", "resource_list.png"]
log_report = PDF()
for plot in plots:
    log_report.print_page(plot)
log_report.output("LogReport.pdf", "F")
