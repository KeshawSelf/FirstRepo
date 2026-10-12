distances = {
  "Voyager 1":"163",
  "Voyager 2":"136",
  "Pioneer 10":"80 AU",
  "New Horizons":"58",
  "Pioneer 11":"44 AU",
}

def main() :
        
    spacecraft = input("Enter a spacecraft: ")
    try :
        au = float(distances[spacecraft])
        m = convert(au)
        print(f"{m} m")
    except ValueError :
        print(f"Can't convert '{distances[spacecraft]}' to float")
    except KeyError :
        print(f"Can't find '{spacecraft}' in the dictionary")
    

def convert(au) :
    return au * 149597870700

main()
