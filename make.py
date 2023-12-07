from os import listdir
from bs4 import BeautifulSoup

if __name__ == '__main__':
    file_name = listdir('templates')
    for name in file_name:
        if name == 'base.html':
            continue
        soup = BeautifulSoup(open(f'templates/{name}', encoding='utf-8'))
        title = soup.select('title')
        if len(title)>0:
            title = title[0]
        else:
            title = ''
        next_rel = soup.select('[rel="next"]')
        if len(next_rel)>0:
            next_rel = next_rel[0]
        else:
            next_rel = ''
        prev_rel = soup.select('[rel="prev"]')
        if len(prev_rel)>0:
            prev_rel = prev_rel[0]
        else:
            prev_rel = ''
        book = soup.select('.book')
        if len(book)>0:
            book=book[0]
        else:
            book = ''
        p1 = "{% extends 'base.html' %}\n"
        p2 = f"{{% block head %}}\n{title}\n{next_rel}\n{prev_rel}\n{{% endblock %}}\n"
        p3 = f"{{% block body %}}\n{book}\n{{% endblock %}}"
        with open(f'templates/{name}', "w", encoding='utf-8') as f:
            f.write(p1)
            f.write(p2)
            f.write(p3)
