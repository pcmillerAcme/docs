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

# Setup Request for animation
request_object = requests.Session()
code_request_url = (
    'https://api.acme.codes/new?msg=ThisDemonstratesImageQRCode' +
    '&anim=Still' +
    '&format=png' +
    '&xres=800' +
    '&yres=800'
    # imgScaleStill below can be used to scale img, but with increasing
    # risk to scanability.
    # Image will be scaled, but also 'snapped to' the tile borders of the code.
    # See documentation.
    # '&imgScaleStill=0.33',
)

with open('C:\\Users\\YourFileOnYourComputer.png', 'rb') as fh:
    r = requests.post(
        url=code_request_url,
        files={'ufile': fh}
    )

    if r.status_code != 200:
        print('Problem with api call: ' + code_request_url)
        print(r.text)
        import sys
        sys.exit()

# Save the png file in current directory
drop_image_file = join(join(os.getcwd(), 'DemoPngWithImageFromAcme.png'))
print('Saving file to: ' + drop_image_file)
with open(drop_image_file, 'wb') as file_handle:
    for chunk in r.iter_content(4096):
        file_handle.write(chunk)
print('Done.')
