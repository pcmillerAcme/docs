
.. |br| raw:: html

   <br />


SDK
###

Software Development Kit

Here are working examples of client-side software running remotely and accessing api.acme.codes to attain animated or standard QR codes.

1. :ref:`Animated QR Code Retrieval - Python`
2. :ref:`Animated QR Code Retrieval - Web Page (Html & Javascript)`
3. :ref:`Standard QR Code Retrieval - Python`
4. :ref:`Standard QR Code Retrieval - Web Page Html`

|br|
|br|
|br|
|br|

.. _Animated QR Code Retrieval - Python:

Animated QR Code Retrieval - Python
-----------------------------------

acmeAnimationClient.py

This Python script which will make a new request for an animated QR code, check on the progress, and then download the mp4 animation when it is complete.
This script depends on the ``requests`` module, so make sure that is present or ``pip install`` the requests module on your system first.

Note the design pattern of 'request, check progress until complete, retrieve' is required since animation generation times exceed the
standard timeout periods of internet web service calls.

acmeAnimationClient.py: :download:`Download <./_static/acmeAnimationClient.py>` or :ref:`Read acmeAnimationClient.py`

|br|
|br|
|br|

.. _Animated QR Code Retrieval - Web Page (Html & Javascript):

Animated QR Code Retrieval - Web Page (Html & Javascript)
---------------------------------------------------------

acmeWebAnimationClient.html |br|
acmeWebAnimationClient.js

These files define a web page which dynamically queries api.acme.codes for an animation via chained xmlhttp calls.
Click `here <./_static/acmeWebAnimationClient.html>`_ to run the page directly.

Note the design pattern of 'request, check progress until complete, retrieve' is required since animation generation times exceed the
standard timeout periods of internet web service calls.

acmeWebAnimationClient.html: :download:`Download <./_static/acmeWebAnimationClient.html>` or :ref:`Read acmeWebAnimationClient.html`
acmeWebAnimationClient.js: :download:`Download <./_static/acmeWebAnimationClient.js>` or :ref:`Read acmeWebAnimationClient.js`

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

acmeStandardCodeClient.py: :download:`Download <./_static/acmeStandardCodeClient.py>` or :ref:`Read acmeStandardCodeClient.py`

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

acmeWebStandardCodeClient.html: :download:`Download <./_static/acmeWebStandardCodeClient.html>` or :ref:`Read acmeWebStandardCodeClient.html`

|br|
|br|
|br|
|br|
|br|
|br|
|br|

.. _Read acmeAnimationClient.py:

Read acmeAnimationClient.py
---------------------------

::

    import os
    import requests
    from os.path import join
    from time import sleep

    # Setup Request for animation
    request_object = requests.Session()
    new_anim_request_url = (
        'https://api.acme.codes/new?msg=DemonMessage'  # Baseline request
        '&gif=0'  # Suppress gif for speed
        '&fbx=0'  # Suppress fbx for speed
        '&mp4=1'   
        '&xres=400'  # since you're a developer...
        '&yres=400'  # ...let's make the resolution better than default 
    )

    # Send anim request, get order # in return
    order_request_response = request_object.get(new_anim_request_url)
    if order_request_response.status_code != 200:
        print('Problem with api call: ' + new_anim_request_url)
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
    mp4_url = ('https://api.acme.codes/orders/' +
               new_order_data['orderNumber'] + 
               '/mp4'
               )
    mp4_request = request_object.get(mp4_url)
    drop_image_file = join(join(os.getcwd(), 'DemoMp4FromAcme.mp4'))
    print('Saving file to: ' + drop_image_file)
    with open(drop_image_file, 'wb') as file_handle:
        for chunk in mp4_request.iter_content(4096):
            file_handle.write(chunk)
    print ('Done.')

.. _Read acmeWebAnimationClient.html:

Read acmeWebAnimationClient.html
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

.. _Read acmeWebAnimationClient.js:

Read acmeWebAnimationClient.js
------------------------------

::

    // Copyright (c) 2020 Animated Codes Made Easy LLC

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
        '&gif=0' +     // gif creation is slow
        '&fbx=0' +     // fbx not needed for demo
        '&mp4=1'       // mp4 is fastest / best
        )

    orderRequest.onreadystatechange = function()
        {
        if (orderRequest.readyState === 4 && orderRequest.status === 200)
            {
            let orderRequestJson = JSON.parse(orderRequest.responseText);
            document.getElementById('orderNumber').innerHTML =
                orderRequestJson.orderNumber;
            queryAndUpdateProgress();
            }
        }
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
        '/progress')
    progressRequest.onreadystatechange = function()
        {
        if (progressRequest.readyState === 4 && progressRequest.status === 200)
            {
            let orderProgressJson = JSON.parse(
                progressRequest.responseText);
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
        }
    progressRequest.open('GET', progressRequest.tgtUrl);
    progressRequest.send();
    }

    function retrieveMp4Animation()
    {
    mp4Animation = document.getElementById("mp4Animation")
    mp4Animation.setAttribute(
        "src",
        ("https://api.acme.codes/orders/" +
        document.getElementById('orderNumber').innerHTML +
        "/mp4"
        )
    )
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
    // Copyright (c) 2020 Animated Codes Made Easy LLC


.. _Read acmeStandardCodeClient.py:

Read acmeStandardCodeClient.py
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

.. _Read acmeWebStandardCodeClient.html:

Read acmeWebStandardCodeClient.html
-----------------------------------

::

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <script src="acmeWebStandardCodeClient.js"></script>
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
    <img src="https://api.acme.codes/new?msg=AcmeSDKJsApiExample&anim=staticCodeOnly&format=png">
    </td>
    </tr>
    </table>
    </body>
    </html>

