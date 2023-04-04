# Функция принимает в качестве аргумента набор ссылок.
# Ссылки имеют формат ссылок на проекты на гитхабе
# (например: https://github.com/miguelgrinberg/Flask-SocketIO,
# https://github.com/miguelgrinberg/Flask-SocketIO.git).
# Функция должна обработать полученные ссылки и вывести в консоль названия самих гит-проектов.
# Стоит рассмотреть защиту от ссылок "вне формата".

# https://github.com/miguelgrinberg/Flask-SocketIO
# https://github.com/miguelgrinberg/Flask-SocketIO.git


def get_projects_names(*args):
    validate_links = [link for link in args if link.split('/')[2] == 'github.com']
    project_names_list = [link.split('/')[-1] for link in validate_links]
    for name in range(len(project_names_list)):
        if '.' in project_names_list[name]:
            project_names_list[name] = project_names_list[name].split('.')[0]
        print(project_names_list[name])


get_projects_names('https://github.com/miguelgrinberg/Flask-SocketIO.git',
                   'https://github.com/miguelgrinberg/Flask-SocketIO',
                   'https://github.com/olegJF/find_route',
                   'https://github.com/luchanos/treasury',
                   'http://noopdie.com/roundraw/draw.html?v=2')

bad_link = 'http://noopdie.com/roundraw/draw.html?v=2'
