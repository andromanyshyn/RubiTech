# Функция принимает в качестве аргумента набор ссылок.
# Ссылки имеют формат ссылок на проекты на гитхабе
# (например: https://github.com/miguelgrinberg/Flask-SocketIO,
# https://github.com/miguelgrinberg/Flask-SocketIO.git).
# Функция должна обработать полученные ссылки и вывести в консоль названия самих гит-проектов.
# Стоит рассмотреть защиту от ссылок "вне формата".

# https://github.com/miguelgrinberg/Flask-SocketIO
# https://github.com/miguelgrinberg/Flask-SocketIO.git


def get_projects_names(*args):
    validated_links = []
    for link in args:
        if link.startswith('https://github.com/'):
            link = link.split('/')[-1]
            link = link.replace('.git', '') if '.git' in link else link
            validated_links.append(link)
            print(link)


get_projects_names('https://github.com/miguelgrinberg/Flask-SocketIO.git',
                   'https://github.com/miguelgrinberg/Flask-SocketIO',
                   'https://github.com/olegJF/find_route',
                   'https://github.com/luchanos/treasury',
                   'http://noopdie.com/roundraw/draw.html?v=2')

bad_link = 'http://noopdie.com/roundraw/draw.html?v=2'
