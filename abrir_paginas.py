import webbrowser

def open_sites(sites, browser):
    if(browser == 'firefox'):    
        webbrowser.register('firefox', None,
        webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
    elif(browser == 'chrome'):
        webbrowser.register('chrome', None,
        webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
    for i in range(0, len(sites)):
        webbrowser.get(browser).open(sites[i])        

option = int(input('1: Facul, 2: Youtube, 3: Ambos\n'))

studies_urls = [
    'https://trello.com/b/f4XQ8h5L/pessoal',                                    #Trello
    'https://idpcafe.usp.br/idp/profile/SAML2/Redirect/SSO?execution=e1s1',     #Stoa
    'https://ae4.tidia-ae.usp.br/portal',                                       #Tidia
]

youtube_urls = [
    'https://www.youtube.com/c/FAMÍLIABUSCAPÉNOJAPÃO/videos',           #Buscapé
    'https://www.youtube.com/user/vivielucaseleo/videos',               #Rodela
    'https://www.youtube.com/channel/UC0l_MDSrdWMJDX7jZtC07jw/videos',  #Bom de Garfo
    'https://www.youtube.com/c/cadeachave/videos',                      #Cade a Chave
    'https://www.youtube.com/user/felipeneto/videos',                   #Felipe Neto
    'https://www.youtube.com/user/PlatinaKH/videos',                    #Bruno Correa
    'https://www.youtube.com/user/japaonossodecadadia/videos',          #Japão Nosso
    'https://www.youtube.com/channel/UCei3qCwmxoIVV3e2PHRgQ8g/videos'   #Silvio Marques
]

if(option == 1):    #Abrindo sites da faculdade
    open_sites(studies_urls, 'chrome')

elif(option == 2):  #Abrindo canais do Youtube
    open_sites(youtube_urls, 'firefox')
    
elif(option == 3):  #Abrindo sites da faculdade e canais do Youtube
    open_sites(studies_urls, 'chrome')
    open_sites(youtube_urls, 'firefox')
