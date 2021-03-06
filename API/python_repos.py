import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print(f"Kod sanu:{r.status_code}")
response_dict = r.json()

print(response_dict['total_count'])
repo_dicts = response_dict['items']
print(f'liczba repo {len(repo_dicts)}')



names, plot_dicts = [], []

for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value':repo_dict['stargazers_count'],
        'lable':repo_dict['description'],
        'xlink':repo_dict['html_url']
        }
    plot_dicts.append(plot_dict)
my_style = LS('#333366', base_style=LCS)

my_confing = pygal.Config()
my_confing.x_label_rotation = 45
my_confing.show_legend = False
my_confing.title_font_size = 24
my_confing.major_label_font_size = 18
my_confing.truncate_label = 15
my_confing.show_y_guides = False
my_confing.width = 1000
chart = pygal.Bar(my_confing, style=my_style)
chart.force_uri_protocol = 'http'
chart.title = 'Najwieksza liczba gwiazdek'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')


