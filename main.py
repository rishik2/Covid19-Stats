import requests
import os, sys
from datetime import date
from PIL import Image, ImageFont, ImageDraw 
import time

country_code = ['IN', 'US', 'CN']
country_name = ['India', 'USA', 'China']
golbal_ = 'global'
compare_ = 'compare'




def cases_in_country():
    index = 0
    for country in country_name:
       
#Code for saving the image
        graph_req = requests.get('https://corona.dnsforfamily.com/graph.png?c={}'.format(country_code[index])) 

        graph = open( '{}'.format(country) + '.png', 'wb')
        graph.write(graph_req.content)
        graph.close()


#using pillow to edit images
        earth_image = Image.open("Earth.jpg")
        graph_image = Image.open('{}'.format(country) + '.png')


        resized_im = graph_image.resize((round(graph_image.size[0]*0.7), round(graph_image.size[1]*0.7))) #resizing the image
        earth_image.paste(graph_image,(200,300)) #pasting graph image on earth image


        title_font = ImageFont.truetype('NoticiaText-Bold.ttf', 70) #For displaying title on the earth image
        title_text = "Graph Of Covid-19 Cases in {}".format(country)
        image_editable = ImageDraw.Draw(earth_image)
        x,y = 260 ,30
        image_editable.text((x,y), title_text, (255, 160, 0), font=title_font)


        earth_image.save( "Result/'Cases {}'.format(country)" + '.jpg')
        earth_image.show()

        index +=1
        time.sleep(5)


def cases_globally(global_= 'global'):
    graph_req = requests.get('https://corona.dnsforfamily.com/graph.png?c={}'.format(global_)) 

    graph = open( 'Global.png', 'wb')
    graph.write(graph_req.content)
    graph.close()

    earth_image = Image.open("Earth.jpg")
    graph_image = Image.open('Global.png')


    resized_im = graph_image.resize((round(graph_image.size[0]*0.7), round(graph_image.size[1]*0.7))) #resizing the image
    earth_image.paste(graph_image,(200,300)) #pasting graph image on earth image


    title_font = ImageFont.truetype('NoticiaText-Bold.ttf', 70) #For displaying title on the earth image
    title_text = "Graph Of Covid-19 Cases {}".format('Globally')
    image_editable = ImageDraw.Draw(earth_image)
    x,y = 260 ,30
    image_editable.text((x,y), title_text, (255, 160, 0), font=title_font)


    earth_image.save( "Result/'Cases Global" + '.jpg')
    earth_image.show()


def cases_compare(compare_='compare'):
    graph_req = requests.get('https://corona.dnsforfamily.com/graph.png?c={}'.format(compare_)) 

    graph = open( 'Compare.png', 'wb')
    graph.write(graph_req.content)
    graph.close()

    earth_image = Image.open("Earth.jpg")
    graph_image = Image.open('Compare.png')


    resized_im = graph_image.resize((round(graph_image.size[0]*1.5), round(graph_image.size[1]*1.5))) #resizing the image
    earth_image.paste(resized_im,(400,300)) #pasting graph image on earth image


    title_font = ImageFont.truetype('NoticiaText-Bold.ttf', 70) #For displaying title on the earth image
    title_text = "{} Graph Of Covid-19 Cases".format('Comparison')
    image_editable = ImageDraw.Draw(earth_image)
    x,y = 260 ,30
    image_editable.text((x,y), title_text, (255, 160, 0), font=title_font)


    earth_image.save( "Result/'Cases Comparison" + '.jpg')
    earth_image.show()


'''for i in range(1):
    cases_globally()
    time.sleep(5)
    cases_compare()
    time.sleep(5)
    cases_in_country()'''

cases_in_country()
    

