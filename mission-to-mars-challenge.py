#!/usr/bin/env python
# coding: utf-8

# In[28]:


#Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[29]:


#Set the executable path
executable_path= {"executable_path": ChromeDriverManager().install()}
browser= Browser("chrome", **executable_path, headless=False)


# In[30]:


#Visit the mars nasa news site
url="https://redplanetscience.com"
browser.visit(url)
#Delay for loading the page
browser.is_element_present_by_css("div.list_text", wait_time=1)


# In[31]:


#Set up the HTML parser
html=browser.html
news_soup=soup(html, "html.parser")
slide_elem=news_soup.select_one("div.list_text")#Variable which pinpoints all the div tag with the class of list_text


# In[32]:


slide_elem.find("div", class_="content_title")


# In[33]:


#Use the parent element to find the first "a" tag ans save it as news_title
news_title=slide_elem.find("div", class_="content_title").get_text()
news_title


# In[34]:


#Use the parent element to find the paragraph text
news_p=slide_elem.find("div", class_="article_teaser_body").get_text()
news_p


# ### Featured Images

# In[35]:


#Visit URL
url="https://spaceimages-mars.com"
browser.visit(url)


# In[36]:


#Find and click the full image button
full_image_elem=browser.find_by_tag("button")[1]
full_image_elem.click()


# In[37]:


#Parse the resulting html with soup
html=browser.html
img_soup=soup(html, "html.parser")


# In[38]:


#Find the relative image url
img_url_rel=img_soup.find("img", class_="fancybox-image").get("src")
img_url_rel


# In[39]:


#Use the base URL to create an absolute URL
img_url =f"https://spaceimages-mars.com/{img_url_rel}"
img_url


# In[40]:


df= pd.read_html("https://galaxyfacts-mars.com")[0] #Scrape the first table it encounters, or the first item in the list
df.columns=["Description", "Mars", "Earth"]#Assign columns to the new DF
df.set_index("Description", inplace=True)
df


# In[41]:


df.to_html()


# In[ ]:





# # D1. Scrape High Resolution Mar´s Hemisphere Images and Titles

# In[52]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[53]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[54]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[55]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
for i in range(4):
    hemispheres={}
    browser.find_by_css('a.product-item h3')[i].click()
    element = browser.links.find_by_text('Sample').first
    img_url = element['href']
    title = browser.find_by_css("h2.title").text
    hemispheres["img_url"] = img_url
    hemispheres["title"] = title
    hemisphere_image_urls.append(hemispheres)
    browser.back()


# In[56]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[20]:


# 5. Quit the browser
browser.quit()


# In[ ]:




