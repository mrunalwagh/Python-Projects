import cv2

'''-----------------------------------------------SEND TO CLOUD------------------------------------------'''
import requests

regions = ['in']
with open('Nohelmet.jpg', 'rb') as fp:
    response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        data=dict(regions=regions),
        files=dict(upload=fp),
        headers={'Authorization': 'Token a24c9617229126b2b864601adfcf9f8330e91a32'})
jsonRes = response.json()
plate = jsonRes["results"][0]["plate"]
print(plate.upper())
i = plate.upper()
#print(i)

#result = (str(i) in str1)
#print(result)

if result == False:
    print(" Dear user = ", i)
    print(" This is the notice under Section 133 of Motor Vehicle Act against the registration number.")
    print(" You have committed a traffic violation on said date and time.")
    print(" Please pay the amount fine of 500 INR within four days to avoid any legal action.")


elif result == True:
    print("ok")
