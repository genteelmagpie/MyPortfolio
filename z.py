from os.path import join, exists
from TheGlobalModules.clearscreen import clear
from time import sleep
clear()

filePath = "./autoBlogger/blog_content.txt"

tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'img']


def processLine(line):

    if line.count(":") == 1:
        lineParts = [i for i in line.split(":") if i]
        key = lineParts[0].strip().lower()
        value = lineParts[1].strip()
        return key, value
    else:
        lineParts = [i for i in line.split(":") if i]
        if lineParts[0].lower().strip() in tags:
            key = lineParts[0].strip().lower()
            colIndex = line.find(":")
            value = line[colIndex + 1:].strip()
            return key, value
        else:
            return 'p', line.strip()


with open(filePath, 'r', encoding='utf-8', errors='raise') as file:

    data = [i for i in file.read().split("\n")]
    content = [i for i in data[3:] if i]
    blogContent = {}
    bodyPart = {}
    body = []
    stopSplitting = False

    for each in data:
        if data.index(each) <= 2:
            key, value = each.strip().split(': ')
            blogContent[key] = value

    # Generate paragraph part of the blog.

    for each in content:

        if ':' in each:
            key, value = processLine(each)
            bodyPart[key] = value
        else:
            bodyPart['p'] = each.strip()

        # copy the bodyPart dictionary before appending it to the body list**
        body.append(bodyPart.copy())
        bodyPart.clear()

    blogContent['body'] = body

print(body)
