'''
Created on 2011-11-17

@author: Drew
'''
import urllib2
import json 

def iter_dict(dict):
    for key, val in dict.items():

        print "key: " + key + "\n"
        if type (val) == type({}):
            iter_dict(val)
        elif type(val) is list:
            for l in val:
                if type(l)==type({}):
                    iter_dict(l)
                else:
                    print l
                    
        else:
            print "val: " + str(val) + "\n"

def process_listing_node(node,comments):
    for com in node['data']['children']:
        comments[com['data']['id']] = com['data']['body']
        #print com['data']['id'] + "=" + com['data']['body']        
        if  com['data']['replies'] != "":
            process_listing_node(com['data']['replies'],comments) 
            


def comments_from_listing(listing):
    # first item is the post body, the second is the list of comments
    # iterate through, find all comments, add to dict {id:comment_txt}
    comments={}
    l = listing[1]
    process_listing_node(l, comments)  
    
    print "Comments:\n"
    print comments
    
    
            
def load_url(url):
    f = urllib2.urlopen(url)
    s = f.read();
    f.close()
    p= json.loads(s)
    return p
    
def main():
    
    p= load_url("http://www.reddit.com/r/botcirclejerk/comments/lfynh/beep/.json")
    comments_from_listing(p)
    
    '''
    p= load_url("http://www.reddit.com/r/botcirclejerk.json")
    # iter_dict(p)
    # print json.dumps(p,sort_keys=True, indent=4)
    topics = p['data']['children']
    check = {}
    for t3 in topics:
        # look for topics with a lot of comments
        if t3['data']['num_comments'] > 10:
            check[t3['data']['permalink']]=t3['data']['num_comments']
    
    for k,v in check.items():
        print "checking: comments("+str(v)+") " + k
        p = load_url("http://www.reddit.com"+k+".json")
        '''
            
        

    
if __name__ == "__main__":
    main()