
.. |br| raw:: html

   <br />

Standard QR Codes
#################

Sometimes folks want to use ACME's API to generate standard QR codes that are not animated. Why? Several features such as color control, tile shape, transparency, stenciling, anti-aliasing, rotation, and resolution are more controllable than other online standard (non-animated) QR code generation services.

Also, standard QR Codes are free.

(Within reasonable request volume limitations)

To clarify: Though encoded messages are wrapped in free use demo mode *for animations*, standard QR code embedded messages are not wrapped, and have the direct original message embedded in the code. In other words, animated QR codes are paywalled, while standard, non-animated, QR codes are completely free and without message wrapping.

Click `here <./new.html>`_ to see all the options for QR code generation, in particular people like to use the `pixelType <./new.html#pixeltype>`_ argument to customize the code tile shapes of standard QR Codes.

There are two methods to getting free standard QR codes form ACME's API:

1. The :ref:`Acme Sequence`, which is 2-3 API calls. This is the best API approach if you think you may want animated QR codes in the future, your code will already be able to handle the longer generation times required for animated code creation and avoid any timeout problems.
|br|
|br|
2. :ref:`Single Call` sequence. With certain arguments, ACME's API will return a PNG file directly as a response to the first creation API call. 

.. _Acme Sequence:

Acme Sequence
-------------
Here is the 'most ACME way' to do a multi-step request sequence to receive a standard (non-animated) code from api.acme.codes:

1. ``/new?anim=staticCodeOnly&msg=Hello!`` |br| Request an order number by http GET method /new and specify a non-animated product, and receive `JSON <https://en.wikipedia.org/wiki/JSON>`_ response from the ACME service containing an **Order Number** .
|br|
|br|
2. ``/orders/#/frames/1`` |br| Request the standard PNG file by http GET method referencing the **Order Number**. 

For example, a requesting service could ask for code by:
::

    GET: https://api.acme.codes/new?msg=Hello&anim=staticCodeOnly

ACME service would return JSON:
::

    {"orderNumber": "1444720642_NLGEDCVP"}
    
Now, almost immediately, the client can retrieve a standard PNG file:
::

    GET: https://api.acme.codes/orders/1444720642_NLGEDCVP/frames/1

ACME service would then return a png file:

.. image:: ./_static/AcmeFrame_1.png

Note: An immediate resource GET request to an accurate order *might* initially result in a '202 Accepted' response, and not a '200 OK' return code because the service has not yet completed creating the file. For non-animated requests like this, it is not usually required to query and order's progress because the creation time is so short. However, it is still good practice to check and retry if a 202 response is initially returned.
|br| |br|

.. _Single Call:

Single Call
-----------
By setting *both* ``anim=staticCodeOnly`` and ``format=png``, api.acme.codes will directly return a PNG file of a standard QR code. Note: Due to our high quality rendering pipeline, turnaround time varies and may require a few seconds before return. Contact ``sales@acme.codes`` if you require faster response times for standard QR code creation API calls, which are available. 
::

    GET: https://api.acme.codes/new?msg=Hi!&anim=staticCodeOnly&format=png

