from bleach import Bleach
bleach = Bleach()

import re

def prepareEntry(entryJSON, log):
    content = ''
    if 'content' in entryJSON:
        content = entryJSON['content'][0].value
    elif 'description' in entryJSON:
        content = entryJSON['description']
    else:
        content = 'unreadable... ' + str(entryJSON)
    content = bleach.linkify(content)
    tags = []
    if 'tags' in entryJSON:
        for tag in entryJSON['tags']:
            if 'term' in tag:
                tags.append({'tag': tag['term'], 'name': tag['term']})
    return {'entry': content, 'tags': tags, 'title': entryJSON['title'], 'link': entryJSON['link']}
    #return {'entry': str(entryJSON)}