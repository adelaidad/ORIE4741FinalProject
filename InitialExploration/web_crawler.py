# The following script is made for educational pruposes only. 
# This program is not run for any commerical needs 

# credits: https://www.learndatasci.com/tutorials/ultimate-guide-web-scraping-w-python-requests-and-beautifulsoup/
# https://www.scrapingbee.com/blog/selenium-python/#full-example

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver

def modify_text(text_content):
  """
  Method returns relevant text_content obtained from the website of a tv-show
  filtering out information not related to genre or release date

  tex_content is a string which contains information scraped from a certain page 
  of Rotten Tomatoes
  """
  index = text_content.find("Genre")
  text_content = text_content[index+6: ]
  index = text_content.find("Original")
  text_content1 = text_content[:index]
  index = text_content1.find("Date")
  text_content2 = text_content[index+4:]
  text_content = text_content1 + ";" + text_content2

  text_content = text_content.replace("\n"," ")
  text_content = text_content.replace(" ","")
  return text_content

def automate_data_collection(urls, n=50):
  """
  Method which returns a list containing scraped data of the URLs array fed in

  The returned list will contain NA if no suitable website was found for the movie within
  the movie review website, Rotten Tomatoes. We utilize Selenium to get the relevant data from the 
  relevant pages.

  urls: is an array containing 4 alternative URLs which can be used to obtain the information via index 
  n : is an integer which specifies the number of movie urls to scrape from url array
  """

  #urls is a dataframe with 3 options 
  content_scrapped =[]
  real_type= []


  for i in urls[:n]:
    # print(i)
    driver=webdriver.Chrome()
    url = i[0]
    driver.get(url)
    try: #trying link 1

      if("/tv/" in url):
        h1 = driver.find_element(By.CLASS_NAME, "media-info") #checks if the link is right 
        print("IS TV!")
        real_type.append("tv")
        text_content = modify_text(h1.text)
  
      else:
        
        h1 = driver.find_element(By.ID, 'scoreboard') #checks if the link is right 
        print("IS MOVIE")
        real_type.append("m")
        text_content = h1.text

      print(text_content)
      content_scrapped.append(text_content)
      driver.quit()

    except: #link 1 does not exist, we try link 2
      url = i[1]
      driver.get(url)

      try:
        if("/tv/" in url):

          h1 = driver.find_element(By.CLASS_NAME, "media-info") #checks if the link is right 
          print("IS TV!")
          real_type.append("tv")
          text_content = modify_text(h1.text)

        else:

          h1 = driver.find_element(By.ID, 'scoreboard') #checks if the link is right 
          print("IS MOVIE")
          real_type.append("m")
          text_content = h1.text

        print(text_content)
        content_scrapped.append(text_content)
        driver.quit()

      except: #link 2 does not exist, we try link 3
        url = i[2]
        driver.get(url)

        try:

          if("/tv/" in url):

            h1 = driver.find_element(By.CLASS_NAME, "media-info") #checks if the link is right 
            print("IS TV!")
            real_type.append("tv")
            text_content = modify_text(h1.text)

          else:

            h1 = driver.find_element(By.ID, 'scoreboard') #checks if the link is right 
            print("IS MOVIE")
            real_type.append("m")
            text_content = h1.text

          print(text_content)
          content_scrapped.append(text_content)
          driver.quit()

        except: #link 3 does not exist, we try link 4
          url = i[3]
          driver.get(url)

          try:
            if("/tv/" in url):
              
              h1 = driver.find_element(By.CLASS_NAME, "media-info") #checks if the link is right 
              print("IS TV!")
              real_type.append("tv")
              text_content = modify_text(h1.text)

            else:

              h1 = driver.find_element(By.ID, 'scoreboard') #checks if the link is right 
              print("IS MOVIE")
              real_type.append("m")
              text_content = h1.text
          
            print(text_content)
            content_scrapped.append(text_content)
            driver.quit()

          except: #link 4 does not exist, we might have to obtain manually/new edge case
            content_scrapped.append("NA") 
            real_type.append("need to check!!")
      
  print(real_type)
  return content_scrapped, real_type


