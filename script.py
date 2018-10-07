from jinja2 import Environment, FileSystemLoader
import csv
from collections import namedtuple

def renderPage(
        templateFile='', targetFile='', dataFile='',
        contentFile='', title='', description='', 
        stylesheet='"../css/style.css"'):
    """
    Function to generate a webpage using the landing.html template.
    """
    env = Environment(
        loader=FileSystemLoader('templates/'),
        autoescape=False)
    
    template = env.get_template(templateFile)

    if len(dataFile) > 0:
        sections = []

        with open(dataFile) as f:
            for row in csv.reader(f, delimiter = '|'):
                sections.append(row)

        Section = namedtuple('Section', sections[0])

        sections = [Section(i[0], i[1], i[2], i[3]) for i in sections[1:]]

        page = template.render(
            title=title, description=description,
            stylesheet=stylesheet, sections=sections)
    else:
        content = ""

        with open(contentFile) as f:
            content += f.read()

        page = template.render(
            title=title, description=description,
            stylesheet=stylesheet, content=content)

    with open(targetFile, 'w') as f:
        f.write(page)
    
    return 0

# Home Page
renderPage(
    templateFile='main.html',
    targetFile='index.html',
    title="James Holt | Home",
    description='Homepage for James Holt',
    stylesheet='css/style.css',
    contentFile='content/home.html')

# Articles Landing Page
renderPage(
    templateFile='landing.html',
    targetFile='articles/index.html', 
    title="James Holt | Articles",
    description="All articles by James Holt.",
    dataFile='data/articles.csv')

# Resources Page
renderPage(
    templateFile='main.html',
    targetFile='resources/index.html',
    title="James Holt | Resources",
    stylesheet='"../css/style.css"',
    contentFile='content/resources.html')

# Contacts Page
renderPage(
    templateFile='main.html',
    targetFile='contact/index.html',
    title="James Holt | Contact",
    stylesheet='"../css/style.css"',
    contentFile='content/contact.html')

# Retention Rate Simulation
renderPage(
    templateFile='main.html',
    targetFile='articles/retention-rate-simulation/index.html',
    title='James Holt | Articles',
    stylesheet='"../../css/style.css"',
    contentFile='content/retention_rate_simulation.html')