# https://en.wikipedia.org/wiki/MIT_License
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import requests
from os.path import join
from time import sleep

# Setup Request for animation
request_object = requests.Session()
new_anim_request_url = (
    'https://api.acme.codes/new?msg=DemoMessage'  # Baseline request
    '&gif=0'  # Suppress gif for speed
    '&fbx=0'  # Suppress fbx for speed
    '&mp4=1'
    '&xres=400'  # since you're a developer...
    '&yres=400'  # ...let's make the resolution better than default
    # Below: Optional: provide a custom published image to the animation
    # '&img1=https://some.image/somehere/on/the/internet.png'
)

# Send anim request, get order # in return
order_request_response = request_object.get(new_anim_request_url)
if order_request_response.status_code != 200:
    print('Problem with api call: ' + new_anim_request_url)
    import sys
    sys.exit()
new_order_data = order_request_response.json()
print ('The new order number is: ' + new_order_data['orderNumber'])

# Query the api to know when it is complete
progress_url = ('https://api.acme.codes/orders/' +
                new_order_data['orderNumber'] +
                '/progress'
                )
percent_complete = 0
while percent_complete < 100:
    sleep(2)  # Anims take time, be reasonable
    progress_response = request_object.get(progress_url)
    progress_info = progress_response.json()
    print(str(progress_info['progress']) +
          '% complete, currently in stage "' +
          progress_info['stage'] + '"'
          )
    percent_complete = progress_info['progress']
print(str(progress_info['progress']) + '% complete')

# Grab the mp4 file and save it in current directory
mp4_request = request_object.get(progress_info['mp4'])
drop_image_file = join(join(os.getcwd(), 'DemoMp4FromAcme.mp4'))
print('Saving file to: ' + drop_image_file)
with open(drop_image_file, 'wb') as file_handle:
    for chunk in mp4_request.iter_content(4096):
        file_handle.write(chunk)
print ('Done.')
