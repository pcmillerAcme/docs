
.. |br| raw:: html

   <br />


CDN
###

`Content Delivery Network <https://en.wikipedia.org/wiki/Content_delivery_network>`_

ACME offers hosting of generated files (mp4, gif, fbx, png, zip) on our Microsoft Azure based Content Delivery Network (CDN) for paying subscribers. This allows for 24/7/365 global secure availability of created animation files. Note this is distinct from our standard file return hosting, which is only temporary. Our CDN subdomain endpoints are:
|br|
|br|
`https://cdn.api.acme.codes <https://cdn.api.acme.codes>`_
|br|
`https://acme.azureedge.net <https://acme.azureedge.net>`_
|br|
`https://acmeapicdn.z13.web.core.windows.net <https://acmeapicdn.z13.web.core.windows.net>`_
|br|
|br|
Each of the above endpoints references the same data source. 
|br|
|br|
ACME's CDN hosting is a separate additional offering from the standard ACME workflow of creating animation files in ``/orders``. To review subscriber options, an ACME subscriber can:

1. Utilize the ``/new`` resource to create animations (mp4, gif, etc.) which are available in temporary ``/orders`` resources. It is up to the subscriber to download the animation product files and host them where they like, since all content in the ``/orders`` resource is only temporarily available. 
|br|
|br|
2. Optionally, ACME subscribers can pay for additional services for automated publication of animations to our CDN. This support is essentially permanent global hosting of animations, so long as the subscription is active. 

See documentation on the `cdn flag in the /new resource <https://acme.readthedocs.io/en/latest/new.html#cdn>`_ on how to implement automated animation product publication on our CDN.

Please email sales@acme.codes for details on rates and sign up for CDN subscription.


