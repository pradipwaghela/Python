import requests

url="https://unsplash.com/ngetty/v3/search/images/creative?fields=display_set%2Creferral_destinations%2Ctitle&page_size=28&phrase=dog&sort_order=best_match&graphical_styles=photography&exclude_nudity=true&exclude_editorial_use_only=true"
jsn=requests.get(url)
print(jsn)