from bs4 import BeautifulSoup
import requests
import re

response = requests.get('https://news.ycombinator.com/news')
html_text = response.text

soup = BeautifulSoup(html_text, 'html.parser')
# print(soup.prettify())

a_tags = soup.find_all(name='span', class_='titleline')
# print(a_tags)
text_list = []
link_list = []
for tag in a_tags:
    text = tag.a.getText()
    text_list.append(text)
    link = tag.a.get('href')
    link_list.append(link)

score = soup.find_all(name='span', class_='score')
points = [point.getText() for point in score]
real_points = []
for point in points:
    point = int(point.split(' ')[0])
    real_points.append(point)

# print(text_list)
# print(link_list)
# print(real_points)

highest_point_index = real_points.index(max(real_points))
hpi = highest_point_index
fstring = f"{text_list[hpi]}\n{link_list[hpi]}\n{real_points[hpi]} points"
print(fstring)


# a_tag = soup.find(name='span', class_='titleline')
# print(a_tag)
# article_upvote = soup.find(name='span', class_='score').get_text()
# text = a_tag.getText()
# link = a_tag.a.get('href')
# print(text)
# print(link)
# print(article_upvote)






# titles = [n.find(name="a").getText() for n in soup.find_all(class_="titleline")]
# links = [n.find(name="a").get("href") for n in soup.find_all(class_="titleline")]
# votes = [score.getText() for score in soup.find_all(class_="score")]
#
# print(titles)
# print(links)
# print(votes)



# def links(href):
#     return href and not re.compile('^a href').search(href)
#
# print(soup.find_all(href=links))





# all_titles = soup.select(selector=".titleline a")
# all_sitestr = soup.select(selector=".sitestr")
# all_score = soup.select(selector=".score")
#
# titles_list = [title.getText() for title in all_titles]
# sitestr_list = [site.getText() for site in all_sitestr]
# main_titles = [i for i in titles_list if not i in sitestr_list or sitestr_list.remove(i)]
# print(main_titles)
#
# score_list = [score.getText() for score in all_score]
# new_list = [i.split(" points") for i in score_list]
# digit_score_list = [int(row[0]) for row in new_list]
# print(digit_score_list)
#
# max_score = max(digit_score_list)
# max_upvote_index = digit_score_list.index(max_score)
# print(max_upvote_index)
# popular_title = main_titles[max_upvote_index]
# print(f"Popular title is: {popular_title}, that is upvodet {max_score} times.")






# with open(file='website.html', encoding='UTF-8') as file:
#     content = file.read()
#
# soup = BeautifulSoup(markup=content, features='html.parser')
# print(soup.prettify())
# print("--"*50)
#
# print(f'\n{soup.title}')
# print(soup.title.name)
# print(soup.title.string)
#
# all_anchor_tags = soup.find_all(name='a')
# print(f"\n{all_anchor_tags}")
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get('href'))
# print("--"*50)
#
# h3 = soup.select(selector='.heading')
# print(h3)

