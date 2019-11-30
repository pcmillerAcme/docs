// Copyright (c) 2020 Animated Codes Made Easy LLC

function getQrCode()
{
submitAnimationRequest();
}

function submitAnimationRequest()
{
// Send request for new animation
// and retrieve order number response
let orderRequest = getAbstractedXmlObj();
orderRequest.tgtUrl = (
    'https://api.acme.codes/new?msg=AcmeSDKJsApiExample&' +
    '&anim=Spin' + // Spin is a fast demo
    '&gif=0' +     // gif creation is slow
    '&fbx=0' +     // fbx not needed for demo
    '&mp4=1'       // mp4 is fastest / best
    )

orderRequest.onreadystatechange = function()
    {
    if (orderRequest.readyState === 4 && orderRequest.status === 200)
        {
        let orderRequestJson = JSON.parse(orderRequest.responseText);
        document.getElementById('orderNumber').innerHTML =
            orderRequestJson.orderNumber;
        queryAndUpdateProgress();
        }
    }
orderRequest.open('GET', orderRequest.tgtUrl);
orderRequest.send();
}

function queryAndUpdateProgress()
// Update progress until 100%
{
let progressRequest = getAbstractedXmlObj();
progressRequest.tgtUrl = (
    'https://api.acme.codes/orders/' +
    document.getElementById('orderNumber').innerHTML +
    '/progress')
progressRequest.onreadystatechange = function()
    {
    if (progressRequest.readyState === 4 && progressRequest.status === 200)
        {
        let orderProgressJson = JSON.parse(progressRequest.responseText);
        document.getElementById('orderProgress').innerHTML =
            orderProgressJson.progress + "%";
        document.getElementById('orderStage').innerHTML =
            orderProgressJson.stage;
        if (orderProgressJson.progress === 100)
            {
            retrieveMp4Animation();
            }
        else
            {
            // update every 3 seconds
            setTimeout(queryAndUpdateProgress, 3000);
            }
        }
    }
progressRequest.open('GET', progressRequest.tgtUrl);
progressRequest.send();
}

function retrieveMp4Animation()
{
mp4Animation = document.getElementById("mp4Animation")
mp4Animation.setAttribute(
    "src",
    ("https://api.acme.codes/orders/" +
    document.getElementById('orderNumber').innerHTML +
    "/mp4"
    )
    )
}

document.addEventListener('DOMContentLoaded',
                          function(event)
                            {
                            // Trigger auto-updating of animated qr code
                            getQrCode();
                            }
                          );

function getAbstractedXmlObj()
    {
    var xmlhttp;
    if (window.XMLHttpRequest)
        {xmlhttp = new XMLHttpRequest();}
    else
        {xmlhttp = new ActiveXObject('Microsoft.XMLHTTP');}
    return xmlhttp;
    }
// Copyright (c) 2020 Animated Codes Made Easy LLC
