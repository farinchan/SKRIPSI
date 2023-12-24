import matplotlib.pyplot as plt
import numpy as np
import json
 
# Opening JSON file
with open('db.json', 'r') as openfile:
 
    # Reading from json file
    json_object = json.load(openfile)
 
print(type(json_object))
lenght = len(json_object["person1"])

angry = 0
disgust = 0
fear = 0
happy = 0
sad=0
surprise = 0
neutral = 0

fig, ax = plt.subplots()

fruits = ["angry", "disgust", "fear", "happy", "sad", "surprise", "neutral"]
for db in json_object["person1"] :
    angry += db["emotion"]["angry"]
    disgust += db["emotion"]["disgust"]
    fear += db["emotion"]["fear"]
    happy += db["emotion"]["happy"]
    sad += db["emotion"]["sad"]
    surprise += db["emotion"]["surprise"]
    neutral += db["emotion"]["neutral"]
    

counts = [angry, disgust, fear, happy, sad, surprise, neutral]    
print(counts)
bar_labels = ['red', 'blue', 'red', 'orange', 'grey', '_grey', '_grey']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange', 'tab:grey', 'tab:grey', 'tab:grey']

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')

plt.show()