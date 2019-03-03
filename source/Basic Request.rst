
.. |br| raw:: html

   <br />

Basic Request
#############

The minimal request sequence:

1. GET a new order number, receive JSON response containing an **Order Number**.
2. GET the product (or any other information) by referencing the **Order Number**. 

For example, a requesting service could:
::

    GET: https://api.acme.codes/new?msg=Reading%20ACME%20documentation%20is%20fun!

ACME service would return JSON:
::

    {"orderNumber": "1444720642_NLGEDCVP"}
    
Now, after some time has passed, the client can retrieve up to 5 different animated products: gif, mp4, fbx, png (single frames), and zip (raw aggregated frames). For example, an mp4 movie file can be attained by:
::

    GET: https://api.acme.codes/orders/1444720642_NLGEDCVP/mp4

ACME service would then return an animated requested file type. Depending on creation arguments described in this documentation, a file similar to this mp4 would be returned:

.. raw:: html 

   <video loop autoplay muted src="./_static/BasicDemo.mp4"></video> 


Note: An immediate resource GET request to an accurate order will initially result in a '202 Accepted' response, and not a '200 OK' return code because the service has not yet completed creating the file. This response page will contain a message clarifying the reason for the temporary inability to return the requested file.
|br| |br|
This completes the Basic Request workflow; The Standard Request workflow details how to avoid the '202 Accepted' response entirely.
