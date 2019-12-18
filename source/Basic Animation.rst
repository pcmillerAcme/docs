
.. |br| raw:: html

   <br />

Basic Animation
###############

Here is the minimal 2 step request sequence to receive an animated code from api.acme.codes:

1. ``/new`` |br| Request an order number by http GET method /new, and receive `JSON <https://en.wikipedia.org/wiki/JSON>`_ response from the ACME service containing an **Order Number**.
|br|
|br|
2. ``/orders/#/mp4`` |br| Request the product (or any other information) by http GET method referencing the **Order Number**. 

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
Important reminder: Make sure to copy your animations down and place them in your app or `CDN <https://en.wikipedia.org/wiki/Content_delivery_network>`_ or data storage soon after you create them. Do not put links of the animations you create on api.acme.codes in your apps or CDNs; they will soon be deleted. The animations are only available off of api.acme.codes temporarily, though generally always available for 48 hours after creation. Older ``/orders`` are automatically deleted over time. Please remember your harvest period for all files you create on api.acme.codes is limited.
|br|
|br|
OR
|br|
|br|
If you become a monthly subscriber, ACME offers its own CDN as supported by Microsoft Azure. This ACME feature supports global, secure, 24/7/365 hosting of your animation files. See the `CDN section <https://acme.readthedocs.io/en/latest/CDN.html>`_ of this documentation and the ``cdn=`` argument of the ``/new`` resource for details. 
|br|
|br|

This completes the Basic Request workflow; The Standard Request workflow details how to avoid the '202 Accepted' response entirely.

Reminder: all REST resources described in this documentation are http GET methods, and therefore executable by entering the shown http requests in any browser URL field; no command line request client (curl for example) is required. The reader is encouraged to experiment with these calls directly in a browser to interactively see the results.
