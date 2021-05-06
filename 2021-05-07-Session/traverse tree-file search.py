# import json

# directory = []

# with open('directory.json') as f:
#     directory = json.load(f)
directory = {".":["prime.py","guide.txt"],".idea":{"codeStyles":{".":["codeStyleConfig.xml"]},"inspectionProfiles":{".":["Project_Default.xml"]},"jsLinters":{".":["eslint.xml"]}},"assets":{".":["logo.svg"]},"boot":{"main":{".":["i18n.js","axios.js","performance.js"]}},"docs":{".":["readme.md"],"components":{".":["settings.md","calc.md"],"lang":{".":["i18n.js.md"]}}},"layouts":{"Desktop":{".":["Main.vue"]},"Mobile":{".":["Mobile.vue"]}},"pages":{".":["Calendar.vue","Error404.vue","entry.html","script.py"]},"store":{"theme":{"var":{".":["index.js"]}}}}
# print(directory)    

def traverseTree(node):
    # print(node)
    if '.' in node:
        print(node['.'])
        node.pop('.')
    for pointer in list(node.keys()):
        if pointer != '.':
            # print(pointer)
            traverseTree(node[pointer])
    

traverseTree(directory)