import os
import requests
from os.path import join

# Setup Request for animation
request_object = requests.Session()
code_request_url = (
    'https://api.acme.codes/new?msg=DemoMessage'  # Baseline request
    '&format=png'  # request standard image response
    '&anim=staticCodeOnly'  # and no animation
)

# Send code request, get png image file in return
code_request_response = request_object.get(code_request_url)
if code_request_response.status_code != 200:
    print('Problem with api call: ' + code_request_url)
    import sys
    sys.exit()

# Save the png file in current directory
drop_image_file = join(join(os.getcwd(), 'DemoPngFromAcme.png'))
print('Saving file to: ' + drop_image_file)
with open(drop_image_file, 'wb') as file_handle:
    for chunk in code_request_response.iter_content(4096):
        file_handle.write(chunk)
print('Done.')
