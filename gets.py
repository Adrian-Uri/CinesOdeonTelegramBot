from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if esBueno(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error en las peticiones {0} : {1}'.format(url, str(e)))
        return None


def esBueno(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    print(e)

def items():
    html= BeautifulSoup(simple_get("http://www.odeonmulticines.com/Cartelera/084/Burgos"),'html.parser')
    cadena= ""
    for span in html.find_all("span",style="font-weight: bolder; font-size: 16px;"):
        cadena=cadena+span.text+"\n"

    return cadena

