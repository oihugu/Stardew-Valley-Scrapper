import regex

def extract_cost(line):
    _text = line.find('td', {'id': 'infoboxdetail'}).text.replace('\xa0', '').replace('\n', '').replace('\t', '').strip()
    print(_text)
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