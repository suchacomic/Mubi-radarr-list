from bs4 import BeautifulSoup
import requests
from omdbapi.movie_search import GetMovie
from tqdm import tqdm

url = "https://mubi.com/showing"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
omdb_api_key = 'your api key'

movie_title = []
movies = []
#movie_period = []


division = soup.findAll('div', {'class': 'css-14yfd4f e1n7piqx4'})
for heading in division:
	movie_name = heading.find('h2')
	movie_year = heading.find("span", {"class":"css-0 e1n7piqx10"})
	movie_title.append(movie_name.text.title())
	#movie_period.append(movie_year.tex[-4:])

division2 = soup.findAll('div', {'class': 'css-14yfd4f etvj1lh3'})
for heading2 in division2:
	movie_name2 = heading2.find('h2')
	movie_year2 = heading2.find("span", {"class":"css-0 etvj1lh8"})       
	movie_title.append(movie_name2.text.title())
	#movie_period.append(movie_year2.text[-4:])

#querying omdb 
for i in tqdm(movie_title):
	movie_search = GetMovie(title=i, api_key=omdb_api_key)
	results = movie_search.get_data('Title','Released', 'imdbID')
	results['imdb_id'] = results.pop('imdbID')
	results['title'] = results.pop('Title')
	results['year'] = results.pop('Released')
	movies.append(results)

with open('listfile', 'w') as f:
	f.write('\u005B')
	for items in movies:
		f.write('%s' % items + '\u002C' + '\n')
	f.close()
with open('listfile', 'a') as file:
	file.write('\u005D')    
	file.close()
