
.. |br| raw:: html

   <br />

Standard Animation
##################

Since ACME animation generation times can vary significantly based on animation complexity (sub-second to > 2 minutes), the more standard transaction sequence described below provides more options to a client application. 

1. ``/new`` |br|
(Required) |br|
Initiate a new animation creation by GETing a new order by calling https://api.acme.codes/new, and receive JSON response containing an **Order Number**. See the documentation on ``/new`` for details on the many arguments that define your requested animation. 
|br|
|br|
2. ``/orders/<order number>/image`` |br|
(Optional, rarely used) |br|
After the initial order creation request is made, a follow up POST call may be made to upload an image to the specific order just created. The animation is automatically remade with the newly uploaded image. Note this optional call is one of two different ways to supply an image to a requested animation. This resource supports private direct upload of an image after the order is created but requires two API calls. Alternatively, if the desired image is published on the internet, the initial call to ``/new`` can be giving the published image location, bypassing the need for this resource entirely. See more details in the description of the ``image`` resource, and also the alternate ``img1=`` argument of the ``/new`` resource.
|br|
|br|
3. ``/orders/<order number>/progress`` |br|
(Required) |br|
Iteratively GET the **server-side runtime information and order progress** of the animation generation by referencing the **Order Number**. This can be used to display a real time progress bar feedback window for the client. When progress is 100%, the final mp4 URL is also returned.
|br|
|br|
4. ``/orders/<order number>/frames/1`` |br|
(Optional, rarely used) |br|
GET the **first frame** (or any frame, with reasonable correlation to the known server-side progress) by referencing the **Order Number**. This can be used to provide accurate visual feedback to the client user of the product as it is being made. Then, when the server-side progress is = 100%:
|br|
|br|
5. ``/orders/<order number>/mp4-file-info`` |br| 
(Optional, rarely used) |br|
GET the final product file size. This information can be used below.
|br|
|br|
6. Retrieve the final mp4 animation. |br|
(Required) |br|
This can be done in two ways: |br|
``/orders/<order number>/mp4`` |br| GET the final product (animation, 3d file, frames, etc.) with the genericly named ``/mp4`` resource, or |br|
``<Final url provided in above progress resource>`` |br| GET the final mp4 with a specific file URL returned in the above ``progress`` resource when progress is 100%. |br|
|br|

7. Measure |br|
(Optional, rarely used) |br|
Measure the local file size as it is streamed in from the above call and compare it to the known full file size. This comparison can be used to accurately provide visual progress bar(s) to the client regarding file transmission. 

8. Retrieve by CDN |br|
(Optional) |br| If paying for ACME Content Delivery Network (CDN) subscription, use the URL supplied in the JSON response from step 1 which contains an absolute path to the hosted animation files. See the `CDN section <https://acme.readthedocs.io/en/latest/CDN.html>`_ of this documentation for details.

Below are specific detailed examples of the above process.


New Order
"""""""""

For example, a client application could:
::

    GET: https://api.acme.codes/new?msg=ReadingAcmeDocumentationIsFun!

ACME service would return JSON:
::

    {"orderNumber": "1444720642_NLGEDCVP"}
    
Progress
""""""""

Optionally, now the client application can iteratively retrieve the server-side order progress:
::

    GET: https://api.acme.codes/orders/1444720642_NLGEDCVP/progress

ACME service would return JSON:
::

    {"progress": 12, "queue": 0}
    
The client can repeatedly request the progress resource (every few seconds or so) until the "progress" key is 100, indicating that the order is complete. Also, if the "queue" value is non zero, this indicates the service resources are at their maximum capacity since a queue has formed, indicating a slowdown in the usual turnaround time. This can be communicated to the user to help explain slow or temporarily static progress values.|br|
Most importantly, when progress is 100 and mp4 file was requested, a URL is provided targeting a specific mp4 file available on the server for download or display:
::

    {"progress": 100, "queue": 0, "mp4": "https://api.acme.codes/orders/1595107770_1EGWU128/AcmeCode_441535.mp4"}
    


Frames
""""""

Optionally (and rarely used), the remote client application can retrieve arbitrary frames as they become available. Here are 3 examples of specific frames being requested: 
::
    
    GET: https://api.acme.codes/orders/1444720642_NLGEDCVP/frames/1

ACME service would return a non-animated single png file of frame 1:

.. image:: ./_static/AcmeFrame_1.png

::
    
    GET: https://api.acme.codes/orders/1444720642_NLGEDCVP/frames/90

ACME service would return a non-animated single png file of frame 90:

.. image:: ./_static/AcmeFrame_90.png

::
    
    GET: https://api.acme.codes/orders/1444720642_NLGEDCVP/frames/120

ACME service would return a non-animated single png file of frame 120:

.. image:: ./_static/AcmeFrame_120.png


Size
""""
    
Optionally, and rarely used, when reported server-side order "progress" is 100%, the client application can request the final product file size:
::

    GET https://api.acme.codes/orders/1444720642_NLGEDCVP/mp4-file-info

ACME service would return JSON:
::

    {"fileSize": 439441}


Animation
"""""""""

Finally, the client application can retrieve the completed animated products. ACME's API generates the following products: mp4, gif, png frames, fbx and zip. The most common retrieval is the mp4 file of an animation, which is best retrieved from the "mp4" data returned from the "progress" resource when progress has completed at 100. The "mp4" value contains a specific URL and filename for retrieval:
::

    GET: https://api.acme.codes/orders/1595107770_1EGWU128/AcmeCode_441535.mp4
    
Alternatively, the mp4 can retrieved from a non-specific, or generic resource:
::

    GET: https://api.acme.codes/orders/1444720642_NLGEDCVP/mp4

In either case, ACME service would then return an animated mp4 file. Depending on creation arguments described below, a file similar to this would be returned:

.. raw:: html 

   <video loop autoplay muted src="./_static/BasicDemo.mp4"></video> 

Optionally, and rarely used, the client application can display the transmission progress of the final product as it is streamed from server to client by querying the size of the local streamed file as it arrives and comparing it to the known full file size from the above optional mp4-file-info resource.
|br|
|br|
Important reminder: Make sure to copy your animations down and place them in your app or `CDN <https://en.wikipedia.org/wiki/Content_delivery_network>`_ or data storage soon after you create them. Do not put links of the animations you create on api.acme.codes in your apps or CDNs; they will soon be deleted. The animations are only available off of api.acme.codes temporarily; they are automatically deleted over time. Please remember your harvest period for all files you create on api.acme.codes is limited.
|br|
|br|
OR
|br|
|br|
Optionally, if paying for ACME Content Delivery Network subscription, use the URL supplied in the JSON response from step 1 which contains an absolute path to the hosted animation files:

::

    {"orderNumber": "1576574190_8Z0U08JD", "cdnMp4": "https://cdn.api.acme.codes/2019/12/17/e4983b0f-3688-48c1-a49a-f92bda5fb703/AcmeCode_283150.mp4"}

This location can then be embedded in any web page html with global high reliability and availability:

::

   <video loop autoplay muted src="https://cdn.api.acme.codes/2019/12/17/e4983b0f-3688-48c1-a49a-f92bda5fb703/AcmeCode_283150.mp4"></video> 


See the `CDN section <https://acme.readthedocs.io/en/latest/CDN.html>`_ of this documentation for details.
