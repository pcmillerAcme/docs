
.. |br| raw:: html

   <br />

Basic Animation
###############

Here is the minimal request sequence to receive an animated code from api.acme.codes:

1. Request an order number by http GET method /new, and receive `JSON <https://en.wikipedia.org/wiki/JSON>`_ response from the ACME service containing an **Order Number**.
2. Request the product (or any other information) by http GET method referencing the **Order Number**. 

For example, a requesting service could ask for an animation to be started by:
::

    GET: https://api.acme.codes/new?msg=ReadingAcmeDocumentationIsFun!

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

Reminder: all REST resources described in this documentation are http GET methods, and therefore executable by entering the shown http requests in any browser URL field; no command line request client (curl for example) is required. The reader is encouraged to experiment with these calls directly in a browser to interactively see the results.
