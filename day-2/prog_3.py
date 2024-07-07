# Write a Python program that reads JSON file containong NASA APOD data and prints the keys: "explanation","Title"
# Use this link to copy your json data (do not use request module, just save the JSON to the variable then do the json operation)
# Json Data url: https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY

import json

nasa_apod_data = {
    "date": "2024-07-07",
    "explanation": "Why are these clouds multi-colored? A relatively rare phenomenon in clouds known as iridescence can bring up unusual colors vividly -- or even a whole spectrum of colors simultaneously. These polar stratospheric clouds also, known as nacreous and mother-of-pearl clouds, are formed of small water droplets of nearly uniform size. When the Sun is in the right position and, typically, hidden from direct view, these thin clouds can be seen significantly diffracting sunlight in a nearly coherent manner, with different colors being deflected by different amounts. Therefore, different colors will come to the observer from slightly different directions. Many clouds start with uniform regions that could show iridescence but quickly become too thick, too mixed, or too angularly far from the Sun to exhibit striking colors. The featured image and an accompanying video were taken late in 2019 over Ostersund, Sweden.",
    "hdurl": "https://apod.nasa.gov/apod/image/2407/IridescentClouds_Strand_1500.jpg",
    "media_type": "image",
    "service_version": "v1",
    "title": "Iridescent Clouds over Sweden",
    "url": "https://apod.nasa.gov/apod/image/2407/IridescentClouds_Strand_960.jpg"
}

print("Title:", nasa_apod_data["title"])
print("Explanation:", nasa_apod_data["explanation"])