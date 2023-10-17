
from jinja2 import Environment, FileSystemLoader
import re
from os.path import join


# Load the template
env = Environment(loader=FileSystemLoader(
    r'D:\GM\Coding\PythonProjects\MyPortfolio\autoBlogger'))
template = env.get_template('template.html')
folPath = r"D:\GM\Coding\PythonProjects\MyPortfolio\autoBlogger"


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


# Read blog content from the text file
with open('./autoBlogger/blog_content.txt', 'r') as file:
    blog_content = {}
    lines = file.readlines()
    content_started = False
    content_lines = []
    stopSplitting = False
    for lno, line in enumerate(lines):

        if line.strip():

            try:
                if not stopSplitting:
                    key, value = line.strip().split(': ')
                    blog_content[key] = value
                else:
                    value = line.strip()
            except ValueError as e:
                key = 'content'
                stopSplitting = True
                content_started = True
                print(e)
                continue

            if content_started and line.strip():
                content_lines.append(line.strip())

    blog_content['content'] = content_lines

print(blog_content.keys())
# Render the template with the blog content
rendered_content = template.render(blog_content)

# Save the rendered content to an HTML file
filePath = join(folPath, 'generated',
                sanitize_title_for_filename(blog_content['title']))
with open(filePath, 'w') as file:
    file.write(rendered_content)

print('Daily blog HTML generated successfully!')
