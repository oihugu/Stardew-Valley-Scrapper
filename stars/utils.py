import regex
import requests as re

def request_and_cache(url, cache):
    if url in cache:
        return cache[url]
    else:
        response = re.get(url)
        cache[url] = response
        return response

def extract_cost(line):
    _text = line.find('td', {'id': 'infoboxdetail'}).text.replace('\xa0', '').replace('\n', '').replace('\t', '').replace(',', '').replace('.', '').strip()
    _text = regex.search(r'([0-9]+)g', _text)
    return _text.group(1) + 'g'


def extract_hyper_class(soup):
    wikitable = soup.find('table', {'class':"wikitable", 'id':"navbox"})
    class_header = wikitable.find('th', {'colspan':"2"})
    return class_header.text.replace('\n', '').strip()

def extract_time(line):
    time = {}

    _text = line.find('td', {'id': 'infoboxdetail'}).text.replace('\xa0', '').replace('\n', '').replace('\t', '').replace(' ', '').strip()
    r_text = regex.search(r'([0-9]+h)?([0-9]+m)?([0-9]+s)?', _text)

    for a in range(1, len(r_text)):
        if r_text[a] != None:
            time[r_text[a][-1]] = r_text[a][:-1]
    
    return time

def extract_source(data, line):
    
    if line.find('td', {'id': 'infoboxdetail'}) != None:
        possible_sources = []
        if line.find('ul') != None:
            for li in line.find_all('li'):
                li = li.text
                possible_sources.append(li if regex.search(r'(.*) for .*', li) == None else regex.search(r'(.*) for .*', li).group(1))
            return [a.strip() for a in possible_sources]
        if line.find('span', {'class': 'nametemplate'}) != None:
            for a in line.find_all('a'):
                possible_sources.append(a.text)
            for span in line.find_all('span', {'class': 'nametemplate'}):
                span = span.find('img').text
                possible_sources.append(span if regex.search(r'(.*) for .*', span) == None else regex.search(r'(.*)\(.*\)', span).group(1))
            return [a.strip() for a in possible_sources if a != '']

        info_detail = line.find('td', {'id': 'infoboxdetail'})
        return [a.strip() for a in info_detail.text.replace('\xa0', '').replace('\n', '').replace('\t', '').split('•')]
    
    return None