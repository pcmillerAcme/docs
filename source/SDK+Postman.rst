
.. |br| raw:: html

   <br />


SDK+Postman
###########

SDK
---

`Software Development Kit <https://en.wikipedia.org/wiki/Software_development_kit>`_

Here are working programs of client-side software running remotely and accessing resource endpoints at api.acme.codes to attain animated or standard QR codes. Many of these examples can be run directly in your browser by clicking on the provided links. All published example code here has the MIT free use license embedded within it; Developers are encouraged to duplicate this code to get up and running with our API and then make modifications as needed.

Animated QR code creation examples:

    :ref:`Python`
    |br|
    :ref:`Python + Image Upload`
    |br|
    :ref:`Web Page`
    |br|
    :ref:`Web Page + Image Upload`
    |br|

Standard QR code - 'Std' - creation examples:

    :ref:`Python Std`
    |br|
    :ref:`Python Std + Image Upload`
    |br|
    :ref:`Web Page Std`
    |br|
    :ref:`Web Page Std + Image Reference`


|br|
|br|
|br|
|br|

.. _Python:

Python
~~~~~~

acmeAnimationClient.py

This Python script which will make a new request for an animated QR code, check on the progress, and then download the mp4 animation when it is complete.
This script depends on the ``requests`` module, so make sure that is present or ``pip install`` the requests module on your system first.

Note the design pattern of 'request, check progress until complete, retrieve' is required since animation generation times exceed the
standard timeout periods of internet web service calls.

`Download/Read acmeAnimationClient.py <./_static/acmeAnimationClient.py>`_


|br|
|br|
|br|


.. _Python + Image Upload:

Python + Image Upload
~~~~~~~~~~~~~~~~~~~~~

acmeAnimationClientImageUpload.py

This Python script is identical to acmeAnimationClient.py above except it has the additional
step of uploading a custom image to the order. It follows the general pattern of "POST new order, check progress #, download mp4"
|br|

`Download/Read acmeAnimationClientImageUpload.py <./_static/acmeAnimationClientImageUpload.py>`_
|br|
|br|
|br|
|br|

.. _Web Page:

Web Page
~~~~~~~~

acmeWebAnimationClient.html |br|
acmeWebAnimationClient.js

These files define a web page which dynamically queries api.acme.codes for an animation via chained xmlhttp calls.

Note the design pattern of 'request, check progress until complete, retrieve' is required since animation generation times exceed the
standard timeout periods of internet web service calls.

|br|
|br|
`Click here to load and run acmeWebAnimationClient.html <./_static/acmeWebAnimationClient.html>`_ in your browser now.
|br|
|br|
`Download/Read acmeWebAnimationClient.js <./_static/acmeWebAnimationClient.js>`_
|br|
|br|
|br|


.. _Web Page + Image Upload:

Web Page + Image Upload
~~~~~~~~~~~~~~~~~~~~~~~

acmeWebAnimationClientImageUpload.html
acmeWebAnimationClientImageUpload.js

This example set is the same as the above Web Animated QR code creation example, but with the additional feature of
a uploading a local image when making the request for the animation.

|br|
|br|
`Click here to load and run acmeWebAnimationClientImageUpload.html <./_static/acmeWebAnimationClientImageUpload.html>`_  in your browser now.
|br|
|br|
`Download/Read acmeWebAnimationClientImageUpload.js <./_static/acmeWebAnimationClientImageUpload.js>`_
|br|
|br|
|br|

.. _Python Std:

Python Std
~~~~~~~~~~

acmeStandardQrCodeClient.py

This Python script does a direct retrieval of a standard (non-animated) QR code from api.acme.codes.
Please note that usage of this resource does not require any Api key and is free of charge within certain volume limitations. ACME reserves
the right to suppress or deny service to users utilizing high usage volumes (~10-20 per hour) without payment.
Paid for subscriptions have much higher volume limits.

`Download/Read acmeStandardQrCodeClient.py <./_static/acmeStandardQrCodeClient.py>`_

|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|

.. _Web Page Std:

Web Page Std
~~~~~~~~~~~~

acmeWebStandardCodeClient.html

This simple Html file simply defines an image on the page that uses a remote resource on api.acme.codes that
triggers a QR code to made dynamically.

Note that because only a single image file in png format is requested, the turnaround time is quite sort, and can be handled within the scope of normal internet service calls. This is unlike requesting animations, which exceed the timeline of standard web service calls; api requests for animations must first query for progress completion before the final animated files are retrieved.

Obviously this is not the recommended approach to using the api.acme.codes, since the QR code image file is being made from scratch each time the page is viewed. Since ACME should never be considered as a Content Delivery Network (CDN), the proper approach would be to capture such images from api.acme.codes first and then store them on a CDN or web server. However, for educational purposes of this SDK kit, the illustration shows how certain calls api.acme.codes can be easily implemented.
|br|
|br|
`Click here to load and run acmeWebStandardCodeClient.html <./_static/acmeWebStandardCodeClient.html>`_ in your browser now.
|br|
|br|
|br|

.. _Python Std + Image Upload:

Python Std + Image Upload
~~~~~~~~~~~~~~~~~~~~~~~~~

acmeStandardCodeWithImageClient.py

This Python script does a direct retrieval of a standard (non-animated) QR code from api.acme.codes.
This script also demonstrates the option of uploading an image to be placed in the middle of the code.
|br|
|br|
When an image is uploaded for a standard QR code, the submitted image is placed in the middle of the code, and the QR code creation engine automatically increases the duplicated message content to help ensure the code is scannable.
|br|
|br|
An argument exists to alter the percentage size the uploaded image covers the QR code: imgScaleStill. It is not recommended to alter this value too much, but in some cases codes can remain scannable.
|br|
|br|
For those interested in the details, two placements occur. First an area of the background color is defined that is driven by imgScaleStill, but also has its borders 'snapped to' the borders of the QR code. This ensures that the image placement does not partially cover any code tiles, which could introduce errors in the scanned result of the code. Then, the image is scaled in its original proportions to fit inside the background color area. As a result, sometimes an area of the background color is visible at the edges of the image, but this is required as mentioned above to ensure scannability. To reduce this background color area, an image can be uploaded which is more square in shape than rectangular.
|br|
|br|

Please note that all image uploads require use of an Api key. Generate standard QR codes are free of charge within certain volume limitations. ACME reserves
the right to suppress or deny service to users utilizing high usage volumes (~10-20 per hour) without payment.
Paid for subscriptions have much higher volume limits.

`Download/Read acmeStandardCodeWithImageClient.py <./_static/acmeStandardCodeWithImageClient.py>`_

|br|
|br|
|br|
|br|

.. _Web Page Std + Image Reference:

Web Page Std + Image Reference
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

acmeWebStandardCodeWithImageClient.html

This simple Html file simply defines an image on the page that uses a remote resource on api.acme.codes that
triggers a QR code to made dynamically. The feature of putting in an image in the middle of the code is demonstrated.

Note that because only a single image file in png format is requested, the turnaround time is quite sort, and can be handled within the scope of normal internet service calls. This is unlike requesting animations, which exceed the timeline of standard web service calls; api requests for animations must first query for progress completion before the final animated files are retrieved.

Obviously this is not the recommended approach to using the api.acme.codes, since the QR code image file
is being made from scratch each time the page is viewed. Since ACME should never be as a Content Delivery Network (CDN) only if that service is subscribed to, the proper approach would be to capture such images from api.acme.codes first and then store them on a CDN or web server. However, for educational purposes of this SDK kit, the illustration shows how certain calls api.acme.codes can be easily implemented.

|br|
|br|
`Click here to load and run acmeWebStandardCodeWithImageClient.html <./_static/acmeWebStandardCodeWithImageClient.html>`_  in your browser now.
|br|
|br|
|br|

Postman
-------

Postman is a well known industry website for sharing, collaborating, and demonstrating API workflows and call sequences. For developers familiar with or interested in Postman, here is a link to our public `Postman workspace for api.acme.codes <https://www.postman.com/acme-codes/workspace/api-acme-codes>`_ On this page there are several Postman "collections" demonstrating the creation of both standard and animated QR codes. Note if you want to run the demonstration Postman collections on the above page, you will have to login or create a Postman account, but they have a baseline free level of service.

|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
