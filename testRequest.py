import requests
import json

imageUrl = "www.firebase.com"
# payload = {'imageUrl': imageUrl, 'objectData': {"object1": [[893, 276], [752, 300], [745, 485], [880, 548], [1020, 501], [1046, 313]], "object2": [[766, 495], [759, 622], [796, 713], [983, 704], [1008, 535], [990, 514], [880, 552]], "object3": [[761, 566], [694, 593], [691, 678], [768, 647], [757, 622]], "object4": [[997, 625], [984, 707], [908, 711], [889, 856], [1075, 881], [1103, 725], [1080, 633]], "object5": [[764, 648], [633, 705], [630, 862], [758, 960], [886, 876], [901, 720], [890, 714], [796, 718]]}}

url = "http://0.0.0.0:8080/classifier"

# r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)
