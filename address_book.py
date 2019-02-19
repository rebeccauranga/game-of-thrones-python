#Dictionaries
# aka HashMap, HashTables, Map, Object

places = {
    'farm burger': '1234 piedmont',
    'naan stop': '1235 piedmont'
}

# what is the address of farm burger? 
places['farm burger']
# go get me the thing with 'farm burger' on the left hand side of the colon

friends = {
    'Europe': {
        'paris': ['frankie', 'grace'],
        'berlin': ['bobbie']
    },
    'Asia': ['my cousin', 'my other cousin', 'their friend'],
    'US': {
        'angela': {
            'pets': {
                'sebby': {
                    'toys': [
                        'mousey',
                        'purple mousey',
                        'tote bag'
                ]
            }, 
            'emmy': {
                'hobbies': [
                    'sleeping'
                    ]
                }
            }
        }
    }
}

#how to access the list of sebby's toys? 

toys = friends['US']['angela']['pets']['sebby']['toys']
for item in toys: 
    print("%s is one of sebby's fave toys" % (item,))