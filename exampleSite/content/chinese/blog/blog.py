
# 把这些都注释掉
# with open('blog.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         title = row['time']
#         date = row['time']
#         image_webp = row['image_webp']
#         image = row['image']
#         author = 'AIGCX'
#         description = 'This is meta description'
#         external_link = row['external_link']
#         content = '---\ntitle: ' + row['title'] + '\ndate: ' + date + '\nimage_webp: images/blog/' + image_webp + '\nimage: images/blog/' + image + '\nauthor: ' + author + '\ndescription: ' + description + '\nexternal_link: ' + external_link + '\n---'
#         with open(title + '.md', 'w') as new_file:
#             new_file.write(content)


 
import csv
import os

with open('blog.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row['title']
        date = row['date']  # Edited line: changed 'time' to 'date'
        image_webp = row['image_webp']
        image = row['image']
        author = 'AIGCX'
        description = 'This is meta description'
        external_link = row['external_link']
        content = '---\ntitle: ' + row['title'] + '\ndate: ' + date + '\nimage_webp: images/blog/' + image_webp + '\nimage: images/blog/' + image + '\nauthor: ' + author + '\ndescription: ' + description + '\nexternal_link: ' + external_link + '\n---'
        with open(date + '.md', 'w') as new_file:  # Edited line: changed 'time' to 'date'
            new_file.write(content)
