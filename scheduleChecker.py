from selenium import webdriver
from bs4 import BeautifulSoup
import datetime
from datetime import date
import time

def currenttimes(url):
    currentDay = str(date.today())
    mydate = datetime.datetime.now()
    date1 = currentDay[8:10] + str(mydate.strftime(" %b"))  
    f = "%d %b"
    date1 = (datetime.datetime.strptime(date1,f) )

    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(1)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')

    scrapeResult = []
    spans = soup.find_all('span',{'class' : 'date'})
    for i in spans:
        res = str(i)
        res = res.replace('<span class="date" data-bind="text: startDateFormatted">', '')
        res = res.replace('</span>', '')
        scrapeResult.append(res)
    browser.close()
    finalRes = []
    for j in scrapeResult:
        temp = str(j)
        temp = temp.replace('January', 'Jan')
        temp = temp.replace('February', 'Feb')
        temp = temp.replace('March', 'Mar')
        temp = temp.replace('April', 'Apr')
        temp = temp.replace('June', 'Jun')
        temp = temp.replace('July', 'Jul')
        temp = temp.replace('August', 'Aug')
        temp = temp.replace('September', 'Sep')
        temp = temp.replace('October', 'Oct')
        temp = temp.replace('November', 'Nov')
        temp = temp.replace('December', 'Dec')
        if len(temp) == 11:
            temp = '0' + temp       
        withoutTime = str(temp[0:6])
        g = "%d %b"
        date2 = (datetime.datetime.strptime(withoutTime,g) )
        if date1 < date2:
            finalRes.append(temp)
    return(finalRes)

def scrapeF1website(urls):
    finalRes = []
    for url in urls:
        browser = webdriver.Chrome()
        browser.get(url)
        #time.sleep(1)
        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')

        scrapeResult = []
        spans1 = soup.find_all('span',{'class' : 'f1-timetable--day'})
        for i in spans1:
            res = str(i)
            res = res.replace('<span class="f1-timetable--day">', '')
            res = res.replace('</span>', '')
            scrapeResult.append(res)
        scrapeResult = [scrapeResult[0], scrapeResult[2]]

        spans2 = soup.find_all('span',{'class' : 'f1-timetable--month f1-bg--gray2 f1-label f1-color--gray5'})
        temp = []
        for j in spans2:
            res = str(j)
            res = res.replace('<span class="f1-timetable--month f1-bg--gray2 f1-label f1-color--gray5">', '')
            res = res.replace('</span>', '')
            temp.append(res)
        scrapeResult[0] += ' '
        scrapeResult[0] += temp[0]
        scrapeResult[1] += ' '
        scrapeResult[1] += temp[2]

        spans3 = soup.find_all('span',{'class' : 'start-time'})
        temp = []
        for j in spans3:
            res = str(j)
            res = res.replace('<span class="start-time">', '')
            res = res.replace('</span>', '')
            temp.append(res)
        scrapeResult[0] += ' '
        scrapeResult[0] += temp[0]
        scrapeResult[1] += ' '
        scrapeResult[1] += temp[2]
        finalRes += (scrapeResult)
        browser.close()
    for idx,val in enumerate(finalRes):
        if idx % 2 == 0:
            temp = finalRes[idx]
            finalRes[idx] = finalRes[idx+1]
            finalRes[idx+1] = temp
    return finalRes

def scrapeF1():
    res1 = currenttimes("https://poules.com/gb/pools/poules-com/formule-1-2021/schedule?brand=1&language=en-gb&culture=nl-NL&ui-culture=nl-NL")
    urls = ["https://www.formula1.com/en/racing/2021/EmiliaRomagna.html", "https://www.formula1.com/en/racing/2021/Portugal.html", "https://www.formula1.com/en/racing/2021/Spain.html", "https://www.formula1.com/en/racing/2021/Monaco.html", "https://www.formula1.com/en/racing/2021/Azerbaijan.html", "https://www.formula1.com/en/racing/2021/Canada.html", "https://www.formula1.com/en/racing/2021/France.html", "https://www.formula1.com/en/racing/2021/Austria.html", "https://www.formula1.com/en/racing/2021/Great_Britain.html", "https://www.formula1.com/en/racing/2021/Hungary.html", "https://www.formula1.com/en/racing/2021/Belgium.html", "https://www.formula1.com/en/racing/2021/Netherlands.html", "https://www.formula1.com/en/racing/2021/Italy.html", "https://www.formula1.com/en/racing/2021/Russia.html", "https://www.formula1.com/en/racing/2021/Singapore.html", "https://www.formula1.com/en/racing/2021/Japan.html", "https://www.formula1.com/en/racing/2021/United_States.html", "https://www.formula1.com/en/racing/2021/Mexico.html", "https://www.formula1.com/en/racing/2021/Brazil.html", "https://www.formula1.com/en/racing/2021/Australia.html", "https://www.formula1.com/en/racing/2021/Saudi_Arabia.html", "https://www.formula1.com/en/racing/2021/United_Arab_Emirates.html"]
    res2 = scrapeF1website(urls)

    if res1 == res2:
        print("Schedule is correct")
    else:
        print("Schedule is not correct")
        print("Dates occuring in one but not in the other are:")
        print(set(res1) ^ set(res2))

scrapeF1()