
.. |br| raw:: html

   <br />

progress
########

``/orders/<order number>/progress``

This resource returns a JSON-formatted response containing information key:value pairs about the specified order since the most recent edit.
|br|
|br|
"progress": an integer in the range [0-100] which represents the percentage of completion for the most recently requested animated code.
|br|
|br|
"stage": a string description of the type of work currently being done to create the order. Example values include:
::

    'Order Creation'
    'Order Definition'
    'Animation'
    'Rendering'
    'Watermarking'
    'Gif Creation'
    'Mp4 Creation'
    'Internal File Verification'
    'External File Verification'
    'Order Complete'

|br|
|br|
"queue": an integer of the count of unstarted orders currently in the request queue. If queue is non-zero, the system is at maximum capacity and progress speed will be delayed. If queue is non-zero, most front end client systems communicate this information to users to help assure them as to why processing is slower than usual.

Example URL:
::

     https://api.acme.codes/orders/1444979323_ODFAUQSE/progress
     
Example return values:
::
    
    {"queue": 10, "progress": 0, "stage": "Order Creation"}
    {"queue": 0, "progress": 0, "stage": "Order Creation"}
    {"queue": 0, "progress": 15, "stage": "Animation"}
    {"queue": 0, "progress": 55, "stage": "Rendering"}
    {"queue": 0, "progress": 100, "stage": "Order Complete"}    