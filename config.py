import re

parameters = {'SERIALIZATION_LANGUAGE':'json',
          'PROJECT_PATH':'sample',
          'PROJECT_URL':'https://thebertaproject.wordpress.com/',
          'DATA_PATH':'sample/data/',
          'MENU_PATH':'sample/data/Menu.json',
              'BROWSER':'Firefox'
}

def pageobject_parser(url, driver):
    """Stablish the rule to instantiate new page object, and return
    the module path and the page object's name.
    The use of this method is not mandatory. You can skip the use of this method and hardcode the pageobjects that must be returned."""
    try:
        url = re.search('^\/(.*?)(\/|$)', url).group(3)
        module = url
        page = url.capitalize()
    except AttributeError:
        page = 'MainPage'
        module = 'mainpage'
    page = page.replace('-','')
    if "wpadmin" in module:
        module = "wpadmin"
        page = "Wpadmin"
    return (parameters['PROJECT_PATH']+'.code.'+ module, page)

