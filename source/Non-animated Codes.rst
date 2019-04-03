
.. |br| raw:: html

   <br />

Non-animated Codes
##################

Sometimes folks want to use our API to generate standard QR codes that are not animated. Why? Several features such as color control, transparency, anti-aliasing, rotation, and resolution are more controllable than other online standard (non-animated) code generation services.

Also, standard QR Codes are free!

To clarify: Though encoded messages are wrapped in free use demo mode *for animations*, static (non-animated) code embedded messages are not wrapped, and have the direct original message embedded in the code. In other words, animated QR codes are paywalled, while standard, non-animated, QR codes are completely free and without message wrapping.

Here is the best request sequence to receive a standard non-animated code from api.acme.codes:

1. Request an order number by http GET method /new and specify a non-animated product, and receive `JSON <https://en.wikipedia.org/wiki/JSON>`_ response from the ACME service containing an **Order Number** .
2. Request the static png file by http GET method referencing the **Order Number**. 

For example, a requesting service could ask for code by:
::

    GET: https://api.acme.codes/new?msg=Hello&anim=staticCodeOnly

ACME service would return JSON:
::

    {"orderNumber": "1444720642_NLGEDCVP"}
    
Now, almost immediately, the client can retrieve a static non animated png file:
::

    GET: https://api.acme.codes/orders/1444720642_NLGEDCVP/frames/1

ACME service would then return a png file

Note: An immediate resource GET request to an accurate order *might* initially result in a '202 Accepted' response, and not a '200 OK' return code because the service has not yet completed creating the file. For non-animated requests like this, it is not usually required to query and order's progress because the creation time is so short. However, it is still good practice to check and retry if a 202 response is initially returned.
