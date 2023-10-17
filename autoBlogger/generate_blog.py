
from jinja2 import Environment, FileSystemLoader

# Load the template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('.template.html')

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

print(blog_content)
# Render the template with the blog content
rendered_content = template.render(blog_content)

# Save the rendered content to an HTML file
with open('daily_blog.html', 'w') as file:
    file.write(rendered_content)

print('Daily blog HTML generated successfully!')
