import firelink

websites = ("Facebook", "Google", "Youtube")


def main():
    for website in websites:
        print(website)
    
    choice = input("Choose a webiste to open: ")
    if choice == "Facebook":
        firelink.firefox(firelink.facebook_link)
    elif choice == "Google":
        firelink.firefox(firelink.google_link)
    elif choice == "Youtube":
        firelink.firefox(firelink.youtube_link)
    else:
        pass


main()