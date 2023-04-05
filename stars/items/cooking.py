import regex

# Extract the ingredients of a recipe in a infobox line, returning a list of lists with the name of the ingredient and the quantity
def ectract_ingredients(line):
    ingredients = {}
    for a in (line.find('td', {'id': 'infoboxdetail'})):
        if len(a) > 1:
            _text = a.text.replace('\xa0', '').replace('\n', '').replace('\t', '').strip()
            _text = regex.search(r'(.*)\(([0-9])\)', _text)
            ingredients[_text[1]] = _text[2]
    return ingredients


# Extract Buffs from a line in the infobox, returning a dict with the buff name and the buff value
def extract_buffs(line):
    buffs = {}
    
    _text = line.text.replace('Buff(s)','').replace('\xa0', '').replace('\n', '').replace('\t', '').replace(' ', '').strip()
    for item in regex.findall(r'([A-z]+)\(([+-][0-9]+)\)', _text):
        buffs[item[0]] = item[1]
    return buffs

def extract_time(line):
    time = {}

    _text = line.find('td', {'id': 'infoboxdetail'}).text.replace('\xa0', '').replace('\n', '').replace('\t', '').replace(' ', '').strip()
    r_text = regex.search(r'([0-9]+h)?([0-9]+m)?([0-9]+s)?', _text)

    for a in range(1, len(r_text)):
        if r_text[a] != None:
            time[r_text[a][-1]] = r_text[a][:-1]
    
    return time

def extract_recipe_source(line):
    multiple_sources = []
    _text = line.text.replace('Recipe Source(s)', '').replace('\xa0', '').replace('\t', '').strip()
    
    while '\n\n' in _text:
        _text = regex.sub(r'\n\n', '\n', _text)
    
    for i, source in enumerate(_text.split('\n')):
        recipe_source = {}
        
        if source != '':
            
            if regex.search(r'(.*)\(([A-z]+).*[+-].*([0-9][+-]).*\)', source): # From a friend
                r_text = regex.search(r'(.*)\(([A-z]+).*[+-].*([0-9][+-]).*\)', source)
                recipe_source['Font'] = 'Friendship'
                recipe_source['Source'] = r_text.group(1)
                recipe_source['Vehicle'] = r_text.group(2)
                recipe_source['When'] = r_text.group(3)
            
            if "The Queen of Sauce" in source.strip():
                source = _text.split('\n')[i+1].strip()
                r_text = regex.search(r'([0-9]+) (.*), Year ([0-9]+)', source)
                recipe_source['Font'] = 'The Queen of Sauce'
                recipe_source['Day'] = r_text.group(1)
                recipe_source['Season'] = r_text.group(2)
                recipe_source['Year'] = r_text.group(3)

            if 'Stardrop Saloon' in source.strip():
                source = source.strip()
                r_text = regex.search(r'Stardrop Saloon for .*"([0-9]+)".*', source)
                recipe_source['Font'] = 'Stardrop Saloon'
                recipe_source['Price'] = r_text.group(1) + 'g'

            if 'Island Trader' in source.strip():
                itens = {}
                source = source.strip()
                r_text = regex.search(r'Island Trader for (.*)', source)
                r_text = r_text.group(1)
                
                for item in regex.findall(r'([A-z]+ ?[A-z]+? ?[A-z]+?) ?\(([0-9]+)\)', _text):
                    itens[item[0]] = item[1]

                recipe_source['Font'] = 'Island Trader'
                recipe_source['Itens'] = itens

            if recipe_source != {}:
                multiple_sources.append(recipe_source)

    return multiple_sources
