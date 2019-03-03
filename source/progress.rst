
.. |br| raw:: html

   <br />

progress
########

This resource returns a JSON-formatted response containing information key:value pairs about the specified order since the most recent edit. Pairs include "progress", which returns an integer in the range [0-100], and represents the percentage of completion for the most recently requested animated code. This progress information is useful to communicate to end users how much longer they will have to wait until their order update is completed. Also, "queue" returns the current size of the backup request queue. If queue is non-zero, the system is at maximum capacity and progress speed will be delayed. If queue is non-zero, most front end client systems communicate this information to users to help assure them as to why processing is slower than usual. Example URL:
::

     https://api.acme.codes/orders/1444979323_ODFAUQSE/progress
     
Example return values:
::
    
    {"queue": 10, "progress": 0}
    {"queue": 0, "progress": 0}
    {"queue": 0, "progress": 15}
    {"queue": 0, "progress": 100}    