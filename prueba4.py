def main():
    print( "hola" )
    try:
        with open("praas.txt", "r") as a:
             print(a.read().split("\n"))
    except:
        print(NameError)



if __name__ == "__main__":
    main()