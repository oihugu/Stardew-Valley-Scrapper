from .cooking import * 
import regex

# Extract the text that are before some image, placing the text in the key of an dictionary and the image name as the value
# This is very useful for lines in the infobox that contains the image and the price for example, or itens that regenerates health or energy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
def extract_text_before_image(line):
    elements = line.find_all('td')
    ap = {}
    for i, a in enumerate(elements):
        if a.find('img') != None:
            index_temp = i
            image_ = a.find('img')['alt'].split('.')[0]

            text = elements[index_temp+1].text.strip()
            text = ' '.join(text.split())  # remove espaços extras

            if len(text.split()) == 1:
                ap[image_] = text
    return ap

# Utilizes dynamicaly other functions to extract the data from the infobox
def extract_food_dynamic(data, line):
    section = line.find('td', {'id': 'infoboxsection'}).text.replace('\n', '')

    if section == 'Ingredients':
        return ectract_ingredients(line)
    
    elif section == 'Buff(s)':
        return extract_buffs(line)
    
    elif section in ['Energy / Health', 'Qi Seasoning']:
        ext = extract_text_before_image(line)
        if section == 'Qi Seasoning' and data['name'] in ext.keys():
            ext['Price'] = ext[data['name']]
            del ext[data['name']]
        return ext 

    elif section == 'Recipe Source(s)':
        return extract_recipe_source(line)

    else:
        return line.find('td', {'id': 'infoboxdetail'}).text.replace('\xa0', '').replace('\n', '').replace('\t', '')

def extract_dynamic(data, line):
    if 'Source' not in data['lines'].keys():
        return line.find('td', {'id': 'infoboxdetail'}).text.replace('\xa0', '').replace('\n', '').replace('\t', '')
    
    elif data['lines']['Source'] == 'Cooking':
        return extract_food_dynamic(data, line)
    
    else:
        return line.find('td', {'id': 'infoboxdetail'}).text.replace('\xa0', '').replace('\n', '').replace('\t', '')