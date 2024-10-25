from colorama import Fore
import time
import requests
import urllib.request
import argparse
READY_MODE = True
APITOKEN = 'BBM8PIkcakU0nIPom5mRni5Q/jVtzVhn1KsLNySSNdTewn5Tkre/IZJP0UXCSKhoU6arGSsY08g=' 

# enter image link then scan score will be on left bottom of text 0 to 100 
urllib.request.urlretrieve('enter link here', "person.jpg")
image_file = 'person.jpg' 

def search_by_face(image_file):
    if READY_MODE:
     print(Fore.LIGHTYELLOW_EX + '''                                                                                            
 ''')                                                                                                                                                                                                                                                                                                                                                                              
    print(Fore.LIGHTWHITE_EX + '''
██████╗ ██╗███████╗███████╗     ██████╗ ███████╗    ██╗██████╗  ██████╗ ███╗   ██╗
██╔══██╗██║██╔════╝██╔════╝    ██╔═══██╗██╔════╝    ██║██╔══██╗██╔═══██╗████╗  ██║
██████╔╝██║███████╗█████╗      ██║   ██║█████╗      ██║██████╔╝██║   ██║██╔██╗ ██║
██╔══██╗██║╚════██║██╔══╝      ██║   ██║██╔══╝      ██║██╔══██╗██║   ██║██║╚██╗██║
██║  ██║██║███████║███████╗    ╚██████╔╝██║         ██║██║  ██║╚██████╔╝██║ ╚████║
╚═╝  ╚═╝╚═╝╚══════╝╚══════╝     ╚═════╝ ╚═╝         ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
          ''')
    print(Fore.LIGHTBLACK_EX + '''#ShakinBiscuit80
                              ''')                                 

    
    print(Fore.LIGHTWHITE_EX + "Scanning Face... Please Wait")
    site='https://facecheck.id'
    headers = {'accept': 'application/json', 'Authorization': APITOKEN}
    files = {'images': open(image_file, 'rb'), 'id_search': None}
    response = requests.post(site+'/api/upload_pic', headers=headers, files=files).json()

    if response['error']:
        return f"{response['error']} ({response['code']})", None

    id_search = response['id_search']
    print(response['message'] + ' id_search='+id_search)
    json_data = {'id_search': id_search, 'with_progress': True, 'status_only': False, 'demo': READY_MODE}

    while True:
        response = requests.post(site+'/api/search', headers=headers, json=json_data).json()
        if response['error']:
            return f"{response['error']} ({response['code']})", None
        if response['output']:
            return None, response['output']['items']
        print(f'{response["message"]} progress: {response["progress"]}%')
        time.sleep(1)

error, urls_images = search_by_face(image_file)

if urls_images:
    for im in urls_images:      # Iterate search results
        score = im['score']     # 0 to 100 score how well the face is matching found image
        url = im['url']         # url to webpage where the person was found
        image_base64 = im['base64']     # thumbnail image encoded as base64 string
        print(f"{score} {url} {image_base64[:32]}...")

    input(Fore.LIGHTBLACK_EX + ''' Press Enter To Exit ''')
 
    print(Fore.LIGHTBLACK_EX +'''          
                ██████╗  ██████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗███████╗   
               ██╔════╝ ██╔═══██╗██╔═══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝   
               ██║  ███╗██║   ██║██║   ██║██║  ██║██████╔╝ ╚████╔╝ █████╗     
               ██║   ██║██║   ██║██║   ██║██║  ██║██╔══██╗  ╚██╔╝  ██╔══╝     
               ╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝██████╔╝   ██║   ███████╗██╗
                ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝
                                                                ''')
    
    input('-h', '--scan', READY_MODE='FILE CONTAINING LIST OF TARGET')
    
