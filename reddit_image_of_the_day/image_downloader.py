import sys, argparse, random, shutil, subprocess, requests
import os
#Settings
client_id = 'a2994972b62d932' #imgur required client-id
headers = {'User-Agent': 'n00b wallpaper bot v0.4',
       'Autorization': 'Client-ID '+client_id}
subreddits = ['http://www.reddit.com/r/wallpapers/.json',
          'http://www.reddit.com/r/wallpaper/.json',
          'https://imgur.com/r/wallpapers.json']
img_file = os.path.join(os.getcwd(),'static') 
url_prefix = 'https://i.imgur.com/'
temp_suffix = '_temp'
img_exts = ['jpg','png']
hide_over_18 = True
#End Settings

def getimg(post):
    return post['data']['url']

def check_ext(img_url):
    for ext in img_exts:
        if img_url.endswith(ext):
            return True
    return False

def not_over_18(post):
    return not post['data']['over_18']

def download_file(url, local_file):
    img_name = "image_of_day"
    r = requests.get(url, stream=True, headers=headers)
    with open(local_file, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=1024):
            fd.write(chunk)
    r.raise_for_status() #if error downloading (404 etc) this will cause an exception
    ext  = url.split(".")[-1]
    if ext not in img_exts:
        print "Invalid file extension. Exiting."
        return False
    img_name = img_name+"."+ ext
    shutil.move(img_file+temp_suffix,os.path.join(img_file,img_name))
    #subprocess.call(["fbsetbg", img_file]) #change fbsetbg to preferred command
    return (True,img_name) 

def imgur(reddit, json_obj, hide_over_18):
    posts = json_obj['data']
    looking = True
    finding = 5 #will try to find up to this many images that satisfy hide_over_18 requirement

    while(looking and finding > 0):
        rand_url_pos = random.randrange(0,len(posts))
        rand_ext = posts[rand_url_pos]['ext']
        rand_url = posts[rand_url_pos]['hash']
        nsfw = posts[rand_url_pos]['nsfw']
        if hide_over_18 and nsfw:
            finding -= 1
        else:
            looking = False
    result, img_name =  download_file(url_prefix+rand_url+rand_ext, img_file+temp_suffix)
    if result:
        return(True,img_name)
    return (False, img_name)

def reddit(reddit, json_obj):
    img_urls = []
    posts = json_obj['data']['children']
    if hide_over_18:
        posts = list(filter(not_over_18,posts))
    img_urls += list(filter(check_ext,list(map(getimg,posts))))
    rand_url = img_urls[random.randrange(0,len(img_urls))]
    result, img_name = download_file(rand_url, img_file+temp_suffix)
    if result:
        return(True,img_name)
    return (False, img_name)

def parse_args(args):
    """
    parser = argparse.ArgumentParser(description='usage: bg_script.py [-h] [--imgur|--reddit|--random]')
    parser.add_argument('--imgur', help='Downloads a random image from imgur only.',
                        action="store_true")
    parser.add_argument('--reddit', help='Downloads a random image from reddit only.',
                        action="store_true")
    parser.add_argument('--random', help='Downloads a random image from a random source.',
                        action="store_true")
    args = parser.parse_args()
    """
    if args.has_key('imgur') and args['imgur']:
        return 2
    elif args.has_key('reddit') and args['reddit']:
        return random.randrange(0,1)
    elif args.has_key('random') and args['random']:
        return random.randrange(0,len(subreddits))
    else:
        print "Please pass a dictionary with a key amongst reddit, imgur or random. The value must be set to True."
        sys.exit(2)
    return


# Main
#args is dictionary
def download(args):
    subreddit = parse_args(args)
    f = requests.get(subreddits[subreddit], headers=headers)
    json_obj = f.json()

    if subreddit==0:
        print('Downloading image from reddit.')
        return reddit(subreddit, json_obj)
    elif subreddit==1:
        print('Downloading image from reddit.')
        return reddit(subreddit, json_obj)
    elif subreddit==2:
        print('Downloading image from imgur.')
        return imgur(subreddit, json_obj,hide_over_18)
    else:
        print('Error in subreddits array!')
        return False
if __name__=="__main__":
    args = {'reddit':True}
    download(args)

