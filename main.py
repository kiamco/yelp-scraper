
import bs4 as bs
import urllib.request as url
import sys

print(sys.argv[1])

pageNum = int(sys.argv[2]) * 10

source = url.urlopen(f'https://www.yelp.com/search?find_desc=free+wifi&find_loc={sys.argv[1]}&ns=1&start={pageNum}')
page_soup = bs.BeautifulSoup(source, 'html.parser')

mains = page_soup.find_all("div", {"class": "lemon--div__373c0__1mboc container__373c0__ZB8u4 hoverable__373c0__3CcYQ margin-t3__373c0__1l90z margin-b3__373c0__q1DuY padding-t3__373c0__1gw9E padding-r3__373c0__57InZ padding-b3__373c0__342DA padding-l3__373c0__1scQ0 border--top__373c0__3gXLy border--right__373c0__1n3Iv border--bottom__373c0__3qNtD border--left__373c0__d1B7K border-color--default__373c0__3-ifU"})


#Try 1 attribute first - Busines Name


# main = mains[1]



# busname = main.find("p",{"class":"lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--black-extra-light__373c0__2OyzO text-align--right__373c0__1f0KI text-size--small__373c0__3NVWO"}).text
# print("phone_Name:" + busname)

#Try second attribute - Ratings

# ratings = main.find("span", {"class": "lemon--span__373c0__3997G text__373c0__2Kxyz priceRange__373c0__2DY87 text-color--black-extra-light__373c0__2OyzO text-align--left__373c0__2XGa- text-bullet--after__373c0__3fS1Z"}).text

# print(ratings)
#Set loop over 1 attribute

# for main in mains:
#     try:
#         busname = main.find("a").text
#         print("Rest_Name:" + busname)
#     except:
#         print(None)

#Save in a file
filename = "yelp_wifi.csv"

f = open(filename, "w")

header = "Rest_Name, Rest_Ratings, Rest_Noreviews, Rest_Price"

f.write(header)

for main in mains:
    try:
        busname = main.find("a",{"class":"lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE"}).text
        print("Rest_Name:" + busname)
    except AttributeError:
        busname = "no name"
        print("Rest_Name:" + busname)

    try:
        ratings = main.find("span", {"class": "lemon--span__373c0__3997G display--inline__373c0__20f31 border-color--default__373c0__Y1Kuj"}).div.get('aria-label')
        print("Rest_Ratings:" + ratings)
    except AttributeError:
        print(None)
    try:
        noreviews = main.find("span", {"class": "lemon--span__373c0__3997G text__373c0__2Kxyz reviewCount__373c0__2r4xT text-color--black-extra-light__373c0__2OyzO text-align--left__373c0__2XGa-"}).text
        print("Rest_Noreviews:" + noreviews)
    except AttributeError:
        noreviews = "no reviews"
        print("Rest_Noreviews:" + noreviews)

    try:
        price = main.find("span", {"class": "lemon--span__373c0__3997G text__373c0__2Kxyz priceRange__373c0__2DY87 text-color--black-extra-light__373c0__2OyzO text-align--left__373c0__2XGa- text-bullet--after__373c0__3fS1Z"}).text
        print("Rest_Price:" + price)
    except AttributeError:
        price = "no price"
        print("Rest_Price:" + price)
    
    
    try:
        phone = main.find("p",{"class":"lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--black-extra-light__373c0__2OyzO text-align--right__373c0__1f0KI text-size--small__373c0__3NVWO"}).text
        print("phone:" + phone if "(" in phone else "phone:no phone")
    except AttributeError:
        phone = "no phone number" 
        print("phone:" + phone)
        
    try:
        address = main.find("span",{"class":"lemon--span__373c0__3997G raw__373c0__3rcx7"}).text
        print("Address:" + address)
    except AttributeError:
        address = "no phone number"
        print("Address:" + address)

    try:
        wifi = main.find("p",{"class":"lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--black-regular__373c0__2vGEn text-align--left__373c0__2XGa- text-weight--semibold__373c0__2l0fe text-size--inherit__373c0__2fB3p"}).text
        print("wifi: " + "yes")
    except AttributeError:
        wifi = "unknown"
        print("wifi:" + wifi)
        


    f.write("\n" + busname + "," + ratings + "," + noreviews + "," + price + "," + phone)
    
f.close()