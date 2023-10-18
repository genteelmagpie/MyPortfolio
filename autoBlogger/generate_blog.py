
from jinja2 import Environment, FileSystemLoader
import re
from os.path import join
from os.path import join, exists
from TheGlobalModules.clearscreen import clear


# Load the template
env = Environment(loader=FileSystemLoader(
    r'D:\GM\Coding\PythonProjects\MyPortfolio\autoBlogger'))
template = env.get_template('template.html')
folPath = r"D:\GM\Coding\PythonProjects\MyPortfolio\autoBlogger"

clear()


filePath = "./autoBlogger/blog_content.txt"

tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'img']


def processLine(line):

    try:
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
    except IndexError:
        print(f" Got an index error with the line: \n\n {line}")


def sanitize_title_for_filename(title):
    """Sanitizes a title name to a file name so that it can be used in Windows.

    Args:
      title: The title name to sanitize.

    Returns:
      A sanitized file name.
    """

    # Remove all non-alphanumeric characters.
    title = re.sub(r"[^\w\s]", "", title)

    # Replace all spaces with underscores.
    title = title.replace(" ", "_")

    # Convert the title to lowercase.
    title = title.lower()

    return f"{title}.html"


with open(filePath, 'r', encoding='utf-8', errors='raise') as file:

    data = [i for i in file.read().split("\n")]
    content = [i for i in data[3:] if i]
    blogContent = {}
    bodyPart = {}
    body = []
    stopSplitting = False

    for each in data:
        if data.index(each) <= 2:
            colNum = each.count(":")
            if colNum != 1:
                print(f" Something is wrong with {each}. There is more than one colon in the item.")
            key, value = each.strip().split(':')
            blogContent[key] = value

    # Generate paragraph part of the blog.

    for each in content:
        # print(f" Working with {each[:15]}")
        if ':' in each:
            key, value = processLine(each)
            bodyPart[key] = value
        else:
            bodyPart['p'] = each.strip()

        # copy the bodyPart dictionary before appending it to the body list**
        body.append(bodyPart.copy())
        bodyPart.clear()

    blogContent['bodyList'] = body


# Render the template with the blog content
rendered_content = template.render(blogContent)

# Save the rendered content to an HTML file
filePath = join(folPath, 'generated',
                sanitize_title_for_filename(blogContent['title']))
with open(filePath, 'w') as file:
    file.write(rendered_content)

print('Daily blog HTML generated successfully!')
