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
    'msg=fromDocumentationAcmeStandardQrCodeClient.py'  # Message to embed into the QR code
    '&format=png'  # Request return format of image png file
    '&xres=400'   # Slightly better resolution than default
    '&yres=400'   # Slightly better resolution than default
)

# Send code request, get png image file in return
code_request_response = request_object.get(code_request_url)
if code_request_response.status_code != 200:
    print('Problem with api call: ' + code_request_url)
    import sys
    sys.exit()

# Save the png file locally
d = code_request_response.headers['content-disposition']
filename = re.findall("filename=\"(.+)\"", d)[0]
drop_image_file = join(tempfile.gettempdir(), filename)
print('Saving file to: ' + drop_image_file)
with open(drop_image_file, 'wb') as file_handle:
    for chunk in code_request_response.iter_content(4096):
        file_handle.write(chunk)
print('Done.')
