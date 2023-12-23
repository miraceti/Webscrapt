import requests, os
import json
import webbrowser

api_key = 'ViNqOAhk0LzI280WXisZ0hTwMuQC853aQCG7UVOF'
api_url = 'https://api.nasa.gov/planetary/apod'


params={
    'date' : '2023-12-23',
    'hd' : 'True',
    'api_key' : api_key

}

response = requests.get(api_url, params=params)

json_data = json.loads(response.text)

print(json_data)

#  {
#    "copyright":"Ian Griffin",
#    "date":"2023-12-23",
#    "explanation":"Colours of a serene evening sky are captured in this 8 minute exposure, made near this December's solstice from New Zealand, southern hemisphere, planet Earth. Looking south, star trails form the short concentric arcs around the rotating planet's south celestial pole positioned just off the top of the frame. At top and left of center are trails of the Southern Cross stars and a dark smudge from the Milky Way's Coalsack Nebula. Alpha and Beta Centauri make the brighter yellow and blue tinted trails, reflected below in the waters of Hoopers Inlet in the Pacific coast of the South Island's Otago Peninsula. On that short December summer night, aurora australis also gave luminous, green and reddish hues to the sky above the hills. An upper atmospheric glow distinct from the aurora excited by collisions with energetic particles, pale greenish bands of airglow caused by a cascade of chemical reactions excited by sunlight can be traced in diagonal bands near the top left.",
#    "hdurl":"https://apod.nasa.gov/apod/image/2312/DSCF6968-Enhanced-NR.jpg",
#    "media_type":"image",
#    "service_version":"v1",
#    "title":"A December Summer Night",
#    "url":"https://apod.nasa.gov/apod/image/2312/DSCF6968-Enhanced-NR1024.jpg"
# }

image_url = json_data['hdurl']#si image HD sinon 'url' seulement

webbrowser.open(image_url)