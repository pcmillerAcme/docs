
.. |br| raw:: html

   <br />


SDK
###

Software Development Kit

Here are working examples of client-side software running remotely and accessing api.acme.codes to attain animated or standard QR codes.

:ref:`Animated QR Code Creation - Python`
|br|
:ref:`Animated QR Code Creation - Web Page (Html & Javascript)`
|br|
:ref:`Animated QR Code Creation - Web Page with CDN (Html & Javascript)`
|br|
:ref:`Animated QR Code Creation with Image Upload - Python`
|br|
:ref:`Animated QR Code Creation with Image Upload - Web Page (Html & Javascript)`
|br|
:ref:`Standard QR Code Retrieval - Python`
|br|
:ref:`Standard QR Code Retrieval - Web Page Html`
|br|
|br|
|br|
|br|

.. note::  All source code on this page, executable or not, is declared free under the standard `MIT license <https://en.wikipedia.org/wiki/MIT_License>`_.
 This license is present in all downloads referenced here, but removed from the inline web page listing to aid readability.

|br|
|br|

.. _Animated QR Code Creation - Python:

Animated QR Code Creation - Python
-----------------------------------

acmeAnimationClient.py

This Python script which will make a new request for an animated QR code, check on the progress, and then download the mp4 animation when it is complete.
This script depends on the ``requests`` module, so make sure that is present or ``pip install`` the requests module on your system first.

Note the design pattern of 'request, check progress until complete, retrieve' is required since animation generation times exceed the
standard timeout periods of internet web service calls.

:download:`Download <./_static/acmeAnimationClient.py>` or :ref:`read acmeAnimationClient.py`

|br|
|br|
|br|

.. _Animated QR Code Creation - Web Page (Html & Javascript):

Animated QR Code Creation - Web Page (Html & Javascript)
---------------------------------------------------------

acmeWebAnimationClient.html |br|
acmeWebAnimationClient.js

These files define a web page which dynamically queries api.acme.codes for an animation via chained xmlhttp calls.

Note the design pattern of 'request, check progress until complete, retrieve' is required since animation generation times exceed the
standard timeout periods of internet web service calls.

:download:`Download <./_static/acmeWebAnimationClient.html>` or :ref:`read acmeWebAnimationClient.html`
|br|
:download:`Download <./_static/acmeWebAnimationClient.js>` or :ref:`read acmeWebAnimationClient.js`
|br|
|br|
or `click here <./_static/acmeWebAnimationClient.html>`_ to load and run the page in your browser now.
|br|
|br|
|br|

.. _Animated QR Code Creation - Web Page with CDN (Html & Javascript):

Animated QR Code Creation - Web Page with CDN (Html & Javascript)
-----------------------------------------------------------------

acmeWebAnimationClientCDN.html |br|
acmeWebAnimationClientCDN.js

These files define a web page which dynamically queries api.acme.codes for an animation via chained xmlhttp calls. The final product is loaded from ACME's Content Delivery Network at cdn.api.acme.codes. See the `CDN section of this documentation <https://acme.readthedocs.io/en/latest/CDN.html>`_ for more details.

:download:`Download <./_static/acmeWebAnimationClientCDN.html>` or :ref:`read acmeWebAnimationClientCDN.html`
|br|
:download:`Download <./_static/acmeWebAnimationClientCDN.js>` or :ref:`read acmeWebAnimationClientCDN.js`
|br|
|br|
or `click here to load and run the CDN demo page <./_static/acmeWebAnimationClientCDN.html>`_ in your browser now.
|br|
|br|
|br|


.. _Animated QR Code Creation with Image Upload - Python:

Animated QR Code Creation with Image Upload - Python
----------------------------------------------------

acmeAnimationClientImageUpload.py

This Python script is identical to the Animated QR Code Creation except it has the additional
step of uploading a custom image to the order. Uploading a custom image automatically triggers
a re-processing of the order, so the development code pattern is:
|br|
"get new order #, upload image to order, check progress, download mp4"
|br|
The advantage of uploading a custom image after order creation is that the image
can be uploaded privately, but the disadvantage is a second call must be made after
order creation to upload the image. This is in contrast to providing a custom image
at order creation time; in this case the advantage is that only one call must be made to
create the animation, but the disadvantage is that the image must be published over the web
in advance of order creation via the ``img1`` argument. See documentation on the ``/new`` resource.

:download:`Download <./_static/acmeAnimationClientImageUpload.py>` or :ref:`read acmeAnimationClientImageUpload.py`
|br|
|br|
|br|
|br|

.. _Animated QR Code Creation with Image Upload - Web Page (Html & Javascript):

Animated QR Code Creation with Image Upload - Web Page (Html & Javascript)
--------------------------------------------------------------------------

acmeWebAnimationClientImageUpload.html
acmeWebAnimationClientImageUpload.js

This example set is the same as the above Web Animated QR Code Creation example, but with the additional feature of
a local file selection button and upload button which updates the order's image file by the
Api's ``/orders/#/image`` resource.

:download:`Download <./_static/acmeWebAnimationClientImageUpload.html>` or :ref:`read acmeWebAnimationClientImageUpload.html`
|br|
:download:`Download <./_static/acmeWebAnimationClientImageUpload.js>` or :ref:`read acmeWebAnimationClientImageUpload.js`
|br|
|br|

or `click here acmeWebAnimationClientImageUpload.html <./_static/acmeWebAnimationClientImageUpload.html>`_ to load and run the page in your browser now.

|br|
|br|
|br|
|br|

.. _Standard QR Code Retrieval - Python:

Standard QR Code Retrieval - Python
-----------------------------------

acmeWebStandardCodeClient.py

This Python script does a direct retrieval of a standard (non-animated) QR code from api.acme.codes.
Please note that usage of this resource does not require any Api key and is free of charge within certain volume limitations. ACME reserves
the right to suppress or deny service to users utilizing high usage volumes (~10-20 per hour) without payment.
Paid for subscriptions have much higher volume limits.

:download:`Download <./_static/acmeStandardCodeClient.py>` or :ref:`read acmeStandardCodeClient.py`

|br|
|br|
|br|

.. _Standard QR Code Retrieval - Web Page Html:

Standard QR Code Retrieval - Web Page Html
------------------------------------------

acmeWebStandardCodeClient.html

This simple Html file simply defines an image on the page that uses a remote resource on api.acme.codes that
triggers a QR code to made dynamically.

Note that because only a single image file in png format is requested, the turnaround time is quite sort, and
can be handled within the scope of normal internet service calls. This is unlike requesting animations, which exceed
the timeline of standard web service calls; api requests for animations must first query for progress completion before the final
animated files are retrieved.

Obviously this is not the recommended approach to using the api.acme.codes, since the QR code image file
is being made from scratch each time the page is viewed. Since ACME should never be considered as a Content Delivery Network (CDN),
the proper approach would be to capture such images from api.acme.codes first and then store them on a CDN or web server.
However, for educational purposes of this SDK kit, the illustration shows how certain calls api.acme.codes can be easily implemented.

:download:`Download <./_static/acmeWebStandardCodeClient.html>` or :ref:`read acmeWebStandardCodeClient.html`
|br|
|br|
or `click here acmeWebStandardCodeClient.html <./_static/acmeWebStandardCodeClient.html>`_ to load and run the page in your browser now.

|br|
|br|
|br|
|br|
|br|
|br|
|br|

.. _read acmeAnimationClient.py:

read acmeAnimationClient.py
---------------------------

::

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

|br|
|br|
|br|

.. _read acmeWebAnimationClient.html:

read acmeWebAnimationClient.html
--------------------------------

::

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <script src="acmeWebAnimationClient.js"></script>
    <style>
        body, table {
        text-align: center;
        margin-left: auto;
        margin-right: auto;
        }
    </style>
    </head>
    <body>
        <h1>ACME SDK<br>Api Demo Web Page</h1>
        <br>
        This page will automatically load a dynamically created animated
        QR code from the API at api.acme.codes.<br>
        Reload to restart.<br>
        <br>
        <br>
        The order number is: <b id="orderNumber">--</b>
        <br>
        Animation Progress: <b id="orderProgress"></b><br>
        Animation Stage: <b id="orderStage"></b><br><br>
        <table>
            <tr>
                <td>
                <video id="mp4Animation"muted autoplay loop src="">
                </td>
            </tr>
        </table>
    </body>
    </html>

|br|
|br|
|br|

.. _read acmeWebAnimationClientCDN.html:

read acmeWebAnimationClientCDN.html
-----------------------------------

::

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <script src="acmeWebAnimationClientCDN.js"></script>
    <style>
        body, table {
        text-align: center;
        margin-left: auto;
        margin-right: auto;
        }
    </style>
    </head>
    <body>
        <h1>ACME SDK<br>Api Demo Web Page for CDN</h1>
        <br>
        This page will automatically load a dynamically created animated QR code
        from the API at api.acme.codes.<br><br>
        <b>Note this example shows how to load the animation file hosted on ACME's CDN network.</b><br><br>
        Reload to restart.<br>
        <br>
        <br>
        The order number is: <b id="orderNumber">--</b>
        <br>
        Animation Progress: <b id="orderProgress"></b><br>
        Animation Stage: <b id="orderStage"></b><br><br>
        <table>
            <tr>
                <td>
                <video id="mp4Animation"muted autoplay loop src="">
                </td>
            </tr>
        </table>
    </body>
    </html>
    
|br|
|br|
|br|


.. _read acmeWebAnimationClient.js:

read acmeWebAnimationClient.js
------------------------------

::

    function getQrCode()
    {
    submitAnimationRequest();
    }

    function submitAnimationRequest()
    {
    // Send request for new animation
    // and retrieve order number response
    let orderRequest = getAbstractedXmlObj();
    orderRequest.tgtUrl = (
        'https://api.acme.codes/new?msg=AcmeSDKJsApiExample&' +
        '&anim=Spin' + // Spin is a fast demo
        '&xres=450' +  // higher than default resolution
        '&yres=450' +  // higher than default resolution
        '&gif=0' +     // gif creation is slow
        '&fbx=0' +     // fbx not needed for demo
        '&mp4=1'       // mp4 is fastest / best
        );

    orderRequest.onreadystatechange = function()
        {
        if (orderRequest.readyState === 4 && orderRequest.status === 200)
            {
            let orderRequestJson = JSON.parse(orderRequest.responseText);
            document.getElementById('orderNumber').innerHTML =
                orderRequestJson.orderNumber;
            queryAndUpdateProgress();
            }
        };
    orderRequest.open('GET', orderRequest.tgtUrl);
    orderRequest.send();
    }

    function queryAndUpdateProgress()
    // Update progress until 100%
    {
    let progressRequest = getAbstractedXmlObj();
    progressRequest.tgtUrl = (
        'https://api.acme.codes/orders/' +
        document.getElementById('orderNumber').innerHTML +
        '/progress');
    progressRequest.onreadystatechange = function()
        {
        if (progressRequest.readyState === 4 && progressRequest.status === 200)
            {
            let orderProgressJson = JSON.parse(progressRequest.responseText);
            document.getElementById('orderProgress').innerHTML =
                orderProgressJson
                progress_info['mp4'].progress + "%";
            document.getElementById('orderStage').innerHTML =
                orderProgressJson.stage;
            if (orderProgressJson.progress === 100)
                {
                retrieveMp4Animation();
                }
            else
                {
                // update every 3 seconds
                setTimeout(queryAndUpdateProgress, 3000);
                }
            }
        };
    progressRequest.open('GET', progressRequest.tgtUrl);
    progressRequest.send();
    }

    function retrieveMp4Animation()
    {
    mp4Animation = document.getElementById("mp4Animation");
    mp4Animation.setAttribute("src", orderProgressJson.mp4);
    }

    document.addEventListener('DOMContentLoaded',
                              function(event)
                                {
                                // Trigger auto-updating of animated qr code
                                getQrCode();
                                }
                              );

    function getAbstractedXmlObj()
        {
        var xmlhttp;
        if (window.XMLHttpRequest)
            {xmlhttp = new XMLHttpRequest();}
        else
            {xmlhttp = new ActiveXObject('Microsoft.XMLHTTP');}
        return xmlhttp;
        }


|br|
|br|
|br|

.. _read acmeWebAnimationClientCDN.js:

read acmeWebAnimationClientCDN.js
---------------------------------

::

    let orderRequestJson = null;

    function getQrCode()
    {
    submitAnimationRequest();
    }

    function submitAnimationRequest()
    {
    // Send request for new animation
    // and retrieve order number response
    let orderRequest = getAbstractedXmlObj();

    orderRequest.tgtUrl = (
        'https://api.acme.codes/new?msg=AcmeSDKJsApiCDNExample&' +
        '&anim=Spin' + // Spin is a fast demo
        '&xres=450' +  // higher than default resolution
        '&yres=450' +  // higher than default resolution
        '&gif=0' +     // gif creation is slow
        '&fbx=0' +     // fbx not needed for demo
        '&mp4=1'  +    // mp4 is fastest / best
        '&cdn=1' +     // Request CDN delivery
        '&apiKey=6d3873dc-af01-4cc0-bbb2-0f3537b21f80'  // CDN requests requires an apiKey.
        // Note the above api key is ACME's locked test apiKey, but with CDN permissions
        );

    orderRequest.onreadystatechange = function()
        {
        if (orderRequest.readyState === 4 && orderRequest.status === 200)
            {
            orderRequestJson = JSON.parse(orderRequest.responseText);
            document.getElementById('orderNumber').innerHTML =
                orderRequestJson.orderNumber;
            queryAndUpdateProgress();
            }
        };
    orderRequest.open('GET', orderRequest.tgtUrl);
    orderRequest.send();
    }

    function queryAndUpdateProgress()
    // Update progress until 100%
    {
    let progressRequest = getAbstractedXmlObj();
    progressRequest.tgtUrl = (
        'https://api.acme.codes/orders/' +
        document.getElementById('orderNumber').innerHTML +
        '/progress');
    progressRequest.onreadystatechange = function()
        {
        if (progressRequest.readyState === 4 && progressRequest.status === 200)
            {
            let orderProgressJson = JSON.parse(progressRequest.responseText);
            document.getElementById('orderProgress').innerHTML =
                orderProgressJson.progress + "%";
            document.getElementById('orderStage').innerHTML =
                orderProgressJson.stage;
            if (orderProgressJson.progress === 100)
                {
                retrieveMp4Animation();
                }
            else
                {
                // update every 3 seconds
                setTimeout(queryAndUpdateProgress, 3000);
                }
            }
        };
    progressRequest.open('GET', progressRequest.tgtUrl);
    progressRequest.send();
    }

    function retrieveMp4Animation()
    {
    mp4Animation = document.getElementById("mp4Animation");
    mp4Animation.setAttribute("src", orderRequestJson.cdnMp4)
    }

    document.addEventListener('DOMContentLoaded',
                              function(event)
                                {
                                // Trigger auto-updating of animated qr code
                                getQrCode();
                                }
                              );

    function getAbstractedXmlObj()
        {
        var xmlhttp;
        if (window.XMLHttpRequest)
            {xmlhttp = new XMLHttpRequest();}
        else
            {xmlhttp = new ActiveXObject('Microsoft.XMLHTTP');}
        return xmlhttp;
        }

|br|
|br|
|br|


.. _read acmeStandardCodeClient.py:

read acmeStandardCodeClient.py
------------------------------

::

    import os
    import requests
    from os.path import join

    # Setup Request for animation
    request_object = requests.Session()
    code_request_url = (
        'https://api.acme.codes/new?msg=DemoMessage'  # Baseline request
        '&format=png'  # request standard image response
        '&anim=Still'  # and no animation
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

|br|
|br|
|br|

.. _read acmeWebStandardCodeClient.html:

read acmeWebStandardCodeClient.html
-----------------------------------

::

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <style>
        body, table {
        text-align: center;
        margin-left: auto;
        margin-right: auto;
        }
    </style>
    </head>
    <body>
    <h1>ACME SDK<br>Api Demo Web Page</h1>
    <br>
    This page will automatically load a dynamically created standard QR code from the API at api.acme.codes.<br>
    Reload to refresh.<br>
    <br>
    <br>
    <table>
    <tr>
    <td>
    <img src="https://api.acme.codes/new?msg=AcmeSDKJsApiExample&anim=Still&format=png">
    </td>
    </tr>
    </table>
    </body>
    </html>

|br|
|br|
|br|

.. _read acmeAnimationClientImageUpload.py:

read acmeAnimationClientImageUpload.py
--------------------------------------

::

    import os
    import requests
    from os.path import join
    from time import sleep

    ACME_API_DOMAIN = 'https://api.acme.codes'

    # Setup Request for animation
    request_object = requests.Session()
    new_anim_request_url = (
            ACME_API_DOMAIN +
            '/new?msg=DemoMessage'  # Baseline request
            '&gif=0'  # Suppress gif for speed
            '&fbx=0'  # Suppress fbx for speed
            '&mp4=1'
            '&xres=400'  # since you're a developer...
            '&yres=400'  # ...let's make the resolution better than default
            '&anim=Spin'  # Simplest demo animation
            '&startOnOrderCreation=0'  # Let's not start animation creation until after image is uploaded
    )

    # Send anim request, get order # in return
    order_request_response = request_object.get(new_anim_request_url)
    if order_request_response.status_code != 200:
        print('Problem with api call: ' + new_anim_request_url)
        import sys
        sys.exit()
    new_order_data = order_request_response.json()

    print('The new order number is: ' + new_order_data['orderNumber'])

    # Upload a local custom image to the server after order creation
    local_img_file = '/a/path/to/a/file/on/your/system/uploadMe.jpg'
    # local_img_file = 'C:\\Users\\Peter C. Miller\\Pictures\\PeterMillerAtDWA.JPG'

    image_upload_url = (ACME_API_DOMAIN +
                        '/orders/' +
                        new_order_data['orderNumber'] +
                        '/image'
                        )
    files = {'ufile': open(local_img_file, 'rb')}
    image_post_response = requests.post(image_upload_url, files=files)
    print(image_post_response)

    if image_post_response.status_code == 200:
        print('Image uploaded ok')
    else:
        print('Problem uploading image: ' +
              str(image_post_response.status_code) + '\n' +
              str(image_post_response.text))

    # Query the api to know when it is complete
    progress_url = (ACME_API_DOMAIN + '/orders/' +
                    new_order_data['orderNumber'] +
                    '/progress'
                    )
    percent_complete = 0
    progress_info = {'progress': 0}
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
    drop_image_file = join(join(os.getcwd(),
                                'DemoAnimationWithCustomImage.mp4'))
    print('Saving file to: ' + drop_image_file)
    with open(drop_image_file, 'wb') as file_handle:
        for chunk in mp4_request.iter_content(4096):
            file_handle.write(chunk)
    print('Done.')

|br|
|br|
|br|

.. _read acmeWebAnimationClientImageUpload.html:

read acmeWebAnimationClientImageUpload.html
-------------------------------------------

::

    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <script src="acmeWebAnimationClientImageUpload.js"></script>
        <style>
            body, table {
            text-align: center;
            margin-left: auto;
            margin-right: auto;
            }
        </style>
    </head>

    <body>
        <h1>ACME SDK<br>Api Demo Web Page<br>with Image Upload</h1>
        <br>
        This page will automatically create a new order for an animated QR code
        from the API at api.acme.codes.<br>
        <br>
        In addition, buttons tied to xmlhttp objects add support for a local custom image file to be specified and then uploaded.<br>
        <br>
        After the image has been uploaded, the animation will be started.<br>
        <br>
        After progress is complete, the image will be displayed below.<br>
        <br>
        Reload to restart with a fresh new order.<br>
        <br>
        <br>
        The order number is: <b id="orderNumber">--</b><br>
        <br>
        <input type="file" id="acmeUploadFile" />
        <button type="button" onclick="uploadImageWrapper()">Upload Image</button><br>
        <br>
        Animation Progress: <b id="orderProgress"></b><br>
        <br>
        Animation Stage: <b id="orderStage"></b><br><br>
        <table>
            <tr>
                <td>
                    <video id="mp4Animation" muted autoplay loop src=""></video>
                </td>
            </tr>
        </table>
    </body>
    </html>

|br|
|br|
|br|

.. _read acmeWebAnimationClientImageUpload.js:

read acmeWebAnimationClientImageUpload.js
-----------------------------------------

::

    let orderRequestJson = null;
    let mp4Animation = null;

    function getQrCode()
    {
    submitAnimationRequest();
    }

    function submitAnimationRequest()
    {
    // Send request for new animation
    // and retrieve order number response
    let orderRequest = getAbstractedXmlObj();
    orderRequest.tgtUrl = (
        'https://api.acme.codes/new?msg=AcmeSDKJsApiExample&' +
        '&anim=Spin' + // Spin is a fast demo
        '&xres=450' +  // higher than default resolution
        '&yres=450' +  // higher than default resolution
        '&gif=0' +     // gif creation is slow
        '&fbx=0' +     // fbx not needed for demo
        '&mp4=1' +     // mp4 is fastest / best
        '&startOnOrderCreation=0'  // Don't start on creation, let image upload start animation
        );

    orderRequest.onreadystatechange = function()
        {
        if (orderRequest.readyState === 4 && orderRequest.status === 200)
            {
            orderRequestJson = JSON.parse(orderRequest.responseText);
            document.getElementById('orderNumber').innerHTML =
                orderRequestJson.orderNumber;
            queryAndUpdateProgress();
            }
        };
    orderRequest.open('GET', orderRequest.tgtUrl);
    orderRequest.send();
    }

    function queryAndUpdateProgress()
    // Update progress until 100%
    {
    let progressRequest = getAbstractedXmlObj();
    progressRequest.tgtUrl = (
        'https://api.acme.codes/orders/' +
        document.getElementById('orderNumber').innerHTML +
        '/progress');
    progressRequest.onreadystatechange = function()
        {
        if (progressRequest.readyState === 4 && progressRequest.status === 200)
            {
            let orderProgressJson = JSON.parse(progressRequest.responseText);
            document.getElementById('orderProgress').innerHTML =
                orderProgressJson.progress + "%";
            document.getElementById('orderStage').innerHTML =
                orderProgressJson.stage;
            if (orderProgressJson.progress === 100)
                {
                retrieveMp4Animation(orderProgressJson.mp4);
                }
            else
                {
                // update every 3 seconds
                setTimeout(queryAndUpdateProgress, 3000);
                }
            }
        };
    progressRequest.open('GET', progressRequest.tgtUrl);
    progressRequest.send();
    }

    function retrieveMp4Animation(mp4Url)
    {
    mp4Animation = document.getElementById("mp4Animation");
    mp4Animation.setAttribute("src", mp4Url)
    }

    document.addEventListener('DOMContentLoaded',
                              function(event)
                                {
                                // Trigger auto-updating of animated qr code
                                getQrCode();
                                }
                              );

    function getAbstractedXmlObj()
        {
        let xmlhttp = null;
        if (window.XMLHttpRequest)
            {xmlhttp = new XMLHttpRequest();}
        else
            {xmlhttp = new ActiveXObject('Microsoft.XMLHTTP');}
        return xmlhttp;
        }

    function uploadImageWrapper()
        {
        let a = document.getElementById('acmeUploadFile');
        uploadImage(
            a.files[0],
            orderRequestJson.orderNumber
            )
        }

    function uploadImage(file, order)
        {
        let url = 'https://api.acme.codes/orders/' + order + '/image';
        let xhr = new XMLHttpRequest();
        let fd = new FormData();
        xhr.open('POST', url, true);
        xhr.onreadystatechange = function()
            {
            if (xhr.readyState === 4 && xhr.status === 200)
                {
                // Every thing ok, file uploaded, now
                // clear mp4 field and other output fields and then...
                if (mp4Animation != null)
                    {mp4Animation.src = '';}
                // ...update progress and reload when done
                queryAndUpdateProgress();
                }
            };
        fd.append('ufile', file);
        xhr.send(fd);
        }



|br|
|br|
|br|

