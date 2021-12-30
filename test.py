### The Code compiles all the research grants/fellowships/scholarships. Once verified, they could be categorised into the three types. This code gives all the output in the form of a csv sheet. This code can be integrated into the other code to get all the results on a single google sheet.
### Check for the csv file in the same folder as the code.
### Author : Jinay Dagli
from bs4 import BeautifulSoup
import requests
import pandas as pd
import urllib3
import fileinput

###India Bio Science
html_text = requests.get('https://indiabioscience.org/grants/').text
soup = BeautifulSoup(html_text, 'lxml')
grants = soup.find_all('li',class_="title-regular")
table = []
for grant in grants:
    grant_name = grant.find("a",class_="occupy silent-hover underline-hover").text.replace('  ','')
    descrp = grant.find("div",class_="prose prose-type prose-small")
    if descrp != None:
        descrp = grant.find("div",class_="prose prose-type prose-small").p.text
    elif descrp == None:
        descrp = "Please check link"
    link = grant.header.h3.a['href']
    table.append((grant_name,descrp,link))

###National Geographic

html_text2 = requests.get('https://www.nationalgeographic.org/funding-opportunities/grants/').text
soup2 = BeautifulSoup(html_text2, 'lxml')
grants2 = soup2.find_all('div',class_="media-description")
for grant in grants2:
    grant_name = grant.find("h3",class_="ng-promo-title-large").text
    descrp = grant.find("p").text
    link = grant.div.a['href']
    table.append((grant_name,descrp,link))

###DRDO Projects/Funds [Included in India Science & Technology Website]

# html_text3 = requests.get('https://www.drdo.gov.in/er-forms-for-projects').text
# soup3 = BeautifulSoup(html_text3, 'lxml')
# grants3 = soup3.find_all('tr')
# for grant in grants3:
#     #print(grant)
#     grant_name = grant.find("td")
#     if(grant_name != None):
#         grant_name = grant_name.text
#     descrp = "-"
#     link = grant.find("td",class_="views-field views-field-field-forms-projects-document")
#     if(link == None):
#         link = ""
#     else:
#         link = grant.a['href']
#     #print(link)
#     if(link != ""):
#         table.append((grant_name,descrp,link))

# html_text4 = requests.get('https://dae.gov.in/node/1035').text
# soup4 = BeautifulSoup(html_text4, 'lxml')
# grants4 = soup4.find_all('p')
# for grant in grants4:
#     print(grant)
#     grant_name = grant
#     if(grant_name != None):
#         grant_name = grant_name.find("u")
#         if(grant_name != None):
#             grant_name = grant_name.text
#             descrp = "Please check the link"
#             link = grant.find("a")
#             table.append((grant_name,descrp,link))
#             # print(link)

###CSIR [Council of Scientific and Industrial Research] - Covered in IndiaScience and Technology

# html_text5 = requests.get('https://csirhrdg.res.in/').text
# soup5 = BeautifulSoup(html_text5, 'lxml')
# grants5 = soup5.find_all('ul',class_="dropdown-menu")
# A = []
# i = 0
# for grant in grants5:
#     #print(grant)
#     grant_name = grant.find_all('li')
#     A.append(grant_name)
#     i = i + 1
#     if(i>3):
#         break
# for i in A[3]:
#     grant_name = i.a.text
#     descrp = " "
#     link = 'https://csirhrdg.res.in' + i.a['href']
#     # html_text5n = requests.get(link).text
#     # soup5n = BeautifulSoup(html_text5n,'lxml')
#     # desc = soup5n.find_all('p')
#     # for des in desc:
#     #     des = des.text
#     #     if(des!=None):
#     #         descrp = descrp + des
#     #     if(len(descrp)>=10000):
#     #         break
#     #     break
#     table.append((grant_name,descrp,link))

# html_text6 = requests.get('https://dst.gov.in/fellowship-opportunities-researchers',verify=False).text
# soup6 = BeautifulSoup(html_text6, 'lxml')
# grants6 = soup6.find_all('div',class_="field-content")
# for grant in grants6:
#     #print(grant)
#     grant_name = grant.find_all("p")
#     #print(grant_name)
#     if (grant_name != None):
#         grant_name = grant_name[0].find_all("strong")
#     print(grant_name)
    # if(grant_name!=None):
    #     grant_name = grant_name.text
    # descrp = grant.find("p")
    # if(descrp!=None):
    #     descrp = descrp.text
    # link = grant.p
    # if(link!=None):
    #     link = link.a
    #     if(link!=None):
    #         link = link['href']
    # table.append((grant_name,descrp,link))

###Deutsche Forschungsgemeinschaft (DFG – German Research Foundation)

html_text7 = requests.get('https://www.dfg.de/en/research_funding/programmes/index.html').text
soup7 = BeautifulSoup(html_text7, 'lxml')
grants7 = soup7.find_all('li',class_="bab-element-foerderprogramm-eintrag")
for grant in grants7:
    grant_name = grant.find("span").text
    link = 'https://www.dfg.de/en/research_funding/programmes/' + grant.a['href']
    html_text7n = requests.get(link).text
    soup7n = BeautifulSoup(html_text7n,'lxml')
    descrp = soup7n.find("div",class_="row bab-modul-fliesstext").find("p")
    if(descrp!=None):
        descrp = descrp.text
    table.append((grant_name,descrp,link))

# html_text8 = requests.get('https://main.icmr.nic.in/').text
# soup8 = BeautifulSoup(html_text8, 'lxml')
# grants8 = soup8.find_all('li')
# print(grants8)
# #grant8 = grants8.find_all('ul')
# for grant in grants8:
#     grant_name = grant.find("li")
#     if(grant_name!=None):
#         grant_name = grant_name.find("a")
#     print(grant_name)
#     descrp = "Please check link"
#     link = grant.li.a['href']
#     table.append((grant_name,descrp,link))

###Indo-US Science and Technology Forum

html_text9 = requests.get('https://www.iusstf.org/program-portfolio/visitations-and-fellowships').text
soup9 = BeautifulSoup(html_text9, 'lxml')
grants9 = soup9.find_all('div',class_="filter")
for grant in grants9:
    grant_name = grant.find("div",class_="back face center").find("h2").text
    descrp = grant.find("div",class_="back face center").find("p").text
    descrp = descrp + ": The program is envisaged to "
    link = grant.a['href']
    html_text9n = requests.get(link).text
    soup9n = BeautifulSoup(html_text9n,'lxml')
    grant9n = soup9n.find("div",class_="row sectin-3-divide")
    if(grant9n!=None):
        grant9n = grant9n.find("div",class_="col-md-12")
    if(grant9n!=None):
        grant9n = grant9n.find("li")
    if(grant9n!=None):
        grant9n = grant9n.text
        descrp = descrp + grant9n
    table.append((grant_name,descrp,link))


###  Ministry of Environment, Forest and Climate Change [Included in India Science and Technology]
# urllib3.disable_warnings()
# html_text10 = requests.get('https://moef.gov.in/en/e-citizen/fellowships-and-awards/',verify=False).text
# soup10 = BeautifulSoup(html_text10, 'lxml')
# grants10 = soup10.find_all("td")
# for grant in grants10:
#     grant_name = grant.find("a")
#     # if(grant_name!=None):
#     #     grant_name = grant_name.find("a")
#     if(grant_name!=None):
#         grant_name = grant_name.text
#     # if(grant_name!=None):
#     #     print(grant_name)
#     descrp = "Please check the link"
#     link = grant.a
#     if(link!=None):
#         link = link['href']
#         # html_text10n = requests.get(link).text
#         # soup10n = BeautifulSoup(html_text10n,'lxml')
#         # descrp = soup10n.find('div',class_="tabindex").find('p')
#         # print(descrp)
#         # if(descrp!=None):
#         #     descrp = descrp.text
#     if(grant_name!=None):
#         table.append((grant_name,descrp,link))

### University Grants Commission [Not Revised after 2017-18]

# html_text11 = requests.get('https://www.ugc.ac.in/ugc_schemes/').text
# soup11 = BeautifulSoup(html_text11, 'lxml')
# grants11 = soup11.find_all('div',class_="national_box mb15")
# for grant in grants11[1:]:
#     grant_name = grant.find("h5").text.replace("  ","").replace("\n","")
#     #print(grant_name)
#     descrp = ""
#     link = grant.p.a['href']
#     if(link[0]=="/"):
#         link = 'https://www.ugc.ac.in' + link
#     html_text11n = requests.get(link).text
#     soup11n = BeautifulSoup(html_text11n,'lxml')
#     descrp = soup11n.find('font',class_="text")
#     if(descrp!=None):
#         descrp = descrp.text
#     table.append((grant_name,descrp,link))

### National Science Foundation

html_text12 = requests.get('https://beta.nsf.gov/funding/opportunities?f%5B0%5D=student_educator_eligibility%3Apostdoc').text
soup12 = BeautifulSoup(html_text12, 'lxml')
grants12 = soup12.find_all('div',class_="funding-search-teaser__details")
for grant in grants12:
    grant_name = grant.find("h2").find("span").text
    descrp = grant.find("div",class_="funding-search-teaser_text").text.replace("  ","").replace("\n","")
    link = 'https://beta.nsf.gov' + grant.h2.a['href']
    table.append((grant_name,descrp,link))

list = ['0','1','2','3','4','5','6','7','8','9','10']

def gotolink(link):
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'lxml')
    descrp = soup.find('div', class_='csir_body').text
    return descrp

def entryodd(link):
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'lxml')
    grants = soup.find_all('tr', class_="odd")
    for grant in grants:
        grant_name = grant.find("td", class_="views-field views-field-title").find("a").text
        org = grant.find("td", class_="views-field views-field-field-ministries").text
        grant_name = grant_name + ' by ' + org
        descrp = ""
        link = grant.td.a
        if (link != None):
            link = "https://www.indiascienceandtechnology.gov.in" + link['href']
            descrp = gotolink(link)
        if ((grant_name, descrp, link) not in table):
            table.append((grant_name, descrp, link))

def entryeven(link):
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'lxml')
    grants = soup.find_all('tr', class_="even")
    for grant in grants:
        grant_name = grant.find("td", class_="views-field views-field-title").find("a").text
        org = grant.find("td", class_="views-field views-field-field-ministries").text
        grant_name = grant_name + ' by ' + org
        descrp = ""
        link = grant.td.a
        if (link != None):
            link = "https://www.indiascienceandtechnology.gov.in" + link['href']
            descrp = gotolink(link)
        if ((grant_name, descrp, link) not in table):
            table.append((grant_name, descrp, link))

### Programmes and Schemes ###

for i in list:
    linkreq = "https://www.indiascienceandtechnology.gov.in/listingpage/all-programmes-schemes?page=" + i
    entryodd(linkreq)
    entryeven(linkreq)

#### Fellowships and Scholarship Programmes for Graduate Students ####


for i in list:
    linkreq = "https://www.indiascienceandtechnology.gov.in/nurturing-minds/scholarships/graduation?page=" + i
    html_text14 = requests.get(linkreq).text
    soup14 = BeautifulSoup(html_text14,'lxml')
    grants14 = soup14.find_all('div', class_="views-field views-field-title")
    for grant in grants14:
        grant_name = grant.find('span', class_="field-content").find("a").text
        # print(grant_name)
        descrp = ""
        link = grant.span.a
        if (link != None):
            link = "https://www.indiascienceandtechnology.gov.in" + link['href']
            descrp = gotolink(link)
        if ((grant_name, descrp, link) not in table):
            table.append((grant_name, descrp, link))

#### Fellowships and Scholarship Programmes for Post-Graduate Students ####

for i in list:
    linkreq = "https://www.indiascienceandtechnology.gov.in/nurturing-minds/scholarships/post-graduation?page=" + i
    html_text15 = requests.get(linkreq).text
    soup15 = BeautifulSoup(html_text15,'lxml')
    grants15 = soup15.find_all('div', class_="views-field views-field-title")
    for grant in grants15:
        grant_name = grant.find('span', class_="field-content").find("a").text
        # print(grant_name)
        descrp = ""
        link = grant.span.a
        if (link != None):
            link = "https://www.indiascienceandtechnology.gov.in" + link['href']
            descrp = gotolink(link)
        if ((grant_name, descrp, link) not in table):
            table.append((grant_name, descrp, link))

#### Fellowships and Scholarship Programmes for PhD Scholars ####

for i in list:
    linkreq = "https://www.indiascienceandtechnology.gov.in/nurturing-minds/scholarships/phd?page=" + i
    html_text16 = requests.get(linkreq).text
    soup16 = BeautifulSoup(html_text16,'lxml')
    grants16 = soup16.find_all('div', class_="views-field views-field-title")
    for grant in grants16:
        grant_name = grant.find('span', class_="field-content").find("a").text
        # print(grant_name)
        descrp = ""
        link = grant.span.a
        if (link != None):
            link = "https://www.indiascienceandtechnology.gov.in" + link['href']
            descrp = gotolink(link)
        if ((grant_name, descrp) not in table):
            table.append((grant_name, descrp, link))

#### Fellowships and Scholarship Programmes for Post-Doctoral Fellows ####

for i in list:
    linkreq = "https://www.indiascienceandtechnology.gov.in/nurturing-minds/scholarships/post-doctoral?page=" + i
    html_text17 = requests.get(linkreq).text
    soup17 = BeautifulSoup(html_text17,'lxml')
    grants17 = soup17.find_all('div', class_="views-field views-field-title")
    for grant in grants17:
        grant_name = grant.find('span', class_="field-content").find("a").text
        # print(grant_name)
        descrp = ""
        link = grant.span.a
        if (link != None):
            link = "https://www.indiascienceandtechnology.gov.in" + link['href']
            descrp = gotolink(link)
        if ((grant_name, descrp) not in table):
            table.append((grant_name, descrp, link))

#### Fellowships and Scholarship Programmes for Women Scholars ####

for i in list:
    linkreq = "https://www.indiascienceandtechnology.gov.in/nurturing-minds/scholarships/women?page=" + i
    html_text18 = requests.get(linkreq).text
    soup18 = BeautifulSoup(html_text18,'lxml')
    grants18 = soup18.find_all('div', class_="views-field views-field-title")
    for grant in grants18:
        grant_name = grant.find('span', class_="field-content").find("a").text
        # print(grant_name)
        descrp = ""
        link = grant.span.a
        if (link != None):
            link = "https://www.indiascienceandtechnology.gov.in" + link['href']
            descrp = gotolink(link)
        if ((grant_name, descrp) not in table):
            table.append((grant_name, descrp, link))

#### Fellowships and Scholarship Programmes for Faculty & Scientists ####

for i in list:
    linkreq = "https://www.indiascienceandtechnology.gov.in/nurturing-minds/scholarships/faculties-scientists?page=" + i
    html_text19 = requests.get(linkreq).text
    soup19 = BeautifulSoup(html_text19,'lxml')
    grants19 = soup19.find_all('div', class_="views-field views-field-title")
    for grant in grants19:
        grant_name = grant.find('span', class_="field-content").find("a").text
        # print(grant_name)
        descrp = ""
        link = grant.span.a
        if (link != None):
            link = "https://www.indiascienceandtechnology.gov.in" + link['href']
            descrp = gotolink(link)
        if ((grant_name, descrp) not in table):
            table.append((grant_name, descrp, link))

### AICTE [Student Development Schemes] ###

html_text18 = requests.get('https://www.aicte-india.org/schemes/students-development-schemes').text
soup18 = BeautifulSoup(html_text18, 'lxml')
grants18 = soup18.find_all('div',class_="scheme_start")
for grant in grants18:
    grant_name = grant.find("h5")
    if(grant_name!=None):
        grant_name = grant_name.text
    descrp = grant.find("p")
    if(descrp!=None):
        descrp = descrp.text
    link = grant.li
    # if(link!=None):
    #     link = link.li
    if(link!=None):
        link = link.a
    if(link!=None):
        link = link['href']
    else:
        link = "None"
    table.append((grant_name,descrp,link))

#### Research Grants [Institutional] ####

for i in list:
    linkreq = "https://www.indiascienceandtechnology.gov.in/funding-opportunities/research-grants/institutional?page=" + i
    html_text18 = requests.get(linkreq).text
    soup18 = BeautifulSoup(html_text18,'lxml')
    grants18 = soup18.find_all('tr')
    for grant in grants18:
        grant_name = grant.find('h4').find("a").text
        # print(grant_name)
        descrp = ''
        link = grant.h4.a
        if (link != None):
            link = "https://www.indiascienceandtechnology.gov.in" + link['href']
            html_text18n = requests.get(link).text
            soup18n = BeautifulSoup(html_text18n,'lxml')
            descrp = soup18n.find('div',class_ = 'csir_body').text
        if ((grant_name, descrp, link) not in table):
            table.append((grant_name, descrp, link))


#### Research Grants [International] ####

for i in list:
    linkreq = "https://www.indiascienceandtechnology.gov.in/funding-opportunities/research-grants/international?page=" + i
    html_text19 = requests.get(linkreq).text
    soup19 = BeautifulSoup(html_text19,'lxml')
    grants19 = soup19.find_all('span',class_="field-content")
    for grant in grants19:
        grant_name = grant.find('h4').find("a").text
        # print(grant_name)
        descrp = ''
        link = grant.h4.a
        if (link != None):
            link = "https://www.indiascienceandtechnology.gov.in" + link['href']
            html_text19n = requests.get(link).text
            soup19n = BeautifulSoup(html_text19n, 'lxml')
            descrp = soup19n.find('div', class_='csir_body').text
        if ((grant_name, descrp, link) not in table):
            table.append((grant_name, descrp, link))

#### Research Grants [Individual] ####

for i in list:
    linkreq = "https://www.indiascienceandtechnology.gov.in/funding-opportunities/research-grants/individual?page=" + i
    html_text20 = requests.get(linkreq).text
    soup20 = BeautifulSoup(html_text20,'lxml')
    grants20 = soup20.find_all('span',class_="field-content")
    for grant in grants20:
        grant_name = grant.find('h4').find("a").text
        # print(grant_name)
        descrp = ''
        link = grant.h4.a
        if (link != None):
            link = "https://www.indiascienceandtechnology.gov.in" + link['href']
            html_text20n = requests.get(link).text
            soup20n = BeautifulSoup(html_text20n, 'lxml')
            descrp = soup20n.find('div', class_='csir_body').text
        if ((grant_name, descrp, link) not in table):
            table.append((grant_name, descrp, link))

### AICTE [Faculty Development Schemes] ###

html_text19 = requests.get('https://www.aicte-india.org/schemes/staff-development-schemes').text
soup19 = BeautifulSoup(html_text19, 'lxml')
grants19 = soup19.find_all('div',class_="scheme_start")
for grant in grants19:
    grant_name = grant.find("h5")
    if(grant_name!=None):
        grant_name = grant_name.text
    descrp = grant.find("p")
    if(descrp!=None):
        descrp = descrp.text
    link = grant.li
    # if(link!=None):
    #     link = link.li
    if(link!=None):
        link = link.a
    if(link!=None):
        link = link['href']
    else:
        link = "None"
    table.append((grant_name,descrp,link))

### AICTE [Research And Innovation Development Schemes] ###

html_text20 = requests.get('https://www.aicte-india.org/schemes/research-innovations-development-schemes').text
soup20 = BeautifulSoup(html_text20, 'lxml')
grants20 = soup20.find_all('div',class_="scheme_start")
for grant in grants20:
    grant_name = grant.find("h5")
    if(grant_name!=None):
        grant_name = grant_name.text
    descrp = grant.find("p")
    if(descrp!=None):
        descrp = descrp.text
    link = grant.li
    # if(link!=None):
    #     link = link.li
    if(link!=None):
        link = link.a
    if(link!=None):
        link = link['href']
    else:
        link = "None"
    table.append((grant_name,descrp,link))

### AICTE [Institutional Development Schemes] ###

html_text21 = requests.get('https://www.aicte-india.org/schemes/institutional-development-schemes').text
soup21 = BeautifulSoup(html_text21, 'lxml')
grants21 = soup21.find_all('div',class_="scheme_start")
for grant in grants21:
    grant_name = grant.find("h5")
    if(grant_name!=None):
        grant_name = grant_name.text
    descrp = grant.find("p")
    if(descrp!=None):
        descrp = descrp.text
    link = grant.li
    # if(link!=None):
    #     link = link.li
    if(link!=None):
        link = link.a
    if(link!=None):
        link = link['href']
    else:
        link = "None"
    table.append((grant_name,descrp,link))

df = pd.DataFrame(table,columns=['Grant Name','Description', 'More Info'])
df.index = df.index + 1
#df.drop_duplicates(['Grant Name'],inplace=True)
df.to_csv('test.csv',index=True,encoding='utf-8')
