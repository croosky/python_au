source_md_file=open("source_leetcode_data.txt")
title= source_md_file.readline().split(". ")[1][:-1]
link = source_md_file.readline()
code=source_md_file.read()
source_md_file.close()
md_file=open("intervals.md")
line = md_file.readline()
formated_titles = []
if line:
    md_file.readline()
    line=md_file.readline()
    while line[0]=='+':
        formated_titles.append(line)
        line = md_file.readline()
    previous_part = md_file.read()
else:
    previous_part = ""
md_file.close()

md_file=open("intervals.md","w")
md_file.write("# Intervals\n\n")
for formated_title in formated_titles:
    md_file.write(formated_title)
new_title=title.lower().replace(' ','-')
md_file.write("+ [{}](#{})\n\n{}## {}\n\n{}\n```python\n{}\n```\n\n".format(title,new_title,previous_part,title,link,code))
md_file.close()

