def format_dimension_string(height,width,depth):

        
    dims = ""
    if height is not None:
        
        h = max([int(height),height])
        # if int(height) == height:
        #     h = int(height)
        # else:
        #     h = height 
        dims = '{}'.format(h)

    if width is not None: 
        if dims != "":
            dims = dims + " x "
        dims = dims + '{}'.format(max([int(width), width]))

    if depth is not None:
        if dims != "":
            dims = dims + " x "
        dims = dims + '{}'.format(max([int(depth),depth]))

    if dims != "":
        dims =  dims + " inches"
    return(dims)


def pick_best_image(images):
    prime = None
    alt = None
    doc = None

        # there can be any mix of image types 

    for i in range(0,images.count()):
        img = images[i]
        match img.image_type:
            case 'primary':
                prime=img
                break;
            case 'alternate':
                alt=img
            case 'documentation only':
                doc=img

    if prime != None:
        usethis = prime
    elif doc != None:
        usethis = doc
    else:
        usethis = alt
        
    return usethis
    

        
        


   

