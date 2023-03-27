import regex

# Extract the text that are before some image, placing the text in the key of an dictionary and the image name as the value
# This is very useful for lines in the infobox that contains the image and the price for example, or itens that regenerates health or energy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
def extract_text_before_image(line):
    elements = line.find_all('td')
    ap = []
    for i, a in enumerate(elements):
        if a.find('img') != None:
            index_temp = i
            image_ = a.find('img')['alt'].split('.')[0]

            text = elements[index_temp+1].text.strip()
            text = ' '.join(text.split())  # remove espaços extras

            if len(text.split()) == 1:
                ap.append([image_, text])
    return ap


# Extract the ingredients of a recipe in a infobox line, returning a list of lists with the name of the ingredient and the quantity
def ectract_ingredients(line):
    detail = []
    for a in (line.find('td', {'id': 'infoboxdetail'})):
        if len(a) > 1:
            _text = a.text.replace('\xa0', '').replace('\n', '').replace('\t', '').strip()
            _text = regex.search(r'(.*)\(([0-9])\)', _text)
            detail.append([_text[1], _text[2]])
    return detail