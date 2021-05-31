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

import re
import requests
import tempfile
from os.path import join

# Setup Request for animation
request_object = requests.Session()
code_request_url = (
    'https://api.acme.codes/new?'  # Creation endpoint
    'msg=ThisDemonstratesImageQRCode&'  # Message to embed into QR code 
    'anim=Still&'  # Request a standard (non animated) code
    'format=png&'  # Request direct return format of image png
    'xres=800&' 
    'yres=800'
    # imgScaleStill below can be used to scale img, but with increasing
    # risk to scanability.
    # '&imgScaleStill=0.33',
)

with open('ImageFileOnYourComputer.png', 'rb') as fh:
    code_request_response = requests.post(
        url=code_request_url,
        files={'ufile': fh}
    )

    if code_request_response.status_code != 200:
        print('Problem with api call: ' + code_request_url)
        print(code_request_response.text)
        import sys
        sys.exit(1)

# Save the png file in current directory
disp_header = code_request_response.headers['content-disposition']
filename = re.findall("filename=\"(.+)\"", disp_header)[0]
drop_image_file = join(tempfile.gettempdir(), filename)
print('Saving file to: ' + drop_image_file)
with open(drop_image_file, 'wb') as file_handle:
    for chunk in code_request_response.iter_content(4096):
        file_handle.write(chunk)
print('Done.')
