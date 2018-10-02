# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility
# source should be the source page from something like https://mailman.ic.ac.uk/mailman/admin/animesoc-list/members/list
# Make sure to adjust the max number of members per page to higher than the current number of members
import re

regex = r"<a href=\".+options\/animesoc-list\/.+\">(.*)<\/a><br>"
source = open("source.txt", "r")
contents = source.read()
output = open("emails.txt", "w")

matches = re.finditer(regex, contents, re.MULTILINE)

for matchNum, match in enumerate(matches):
    print (match.group(1))
    output.write(match.group(1) + "\n")

source.close()
output.close()
