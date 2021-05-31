// https://en.wikipedia.org/wiki/MIT_License
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.

let orderRequestJson = null;

function getQrCode()
    {
    // Send request for new animation
    // and retrieve order number response

    let orderRequest = getAbstractedXmlObj();

    orderRequest.tgtUrl = (
        'https://api.acme.codes/new?' +  // Endpoint for new animation creation
        'msg=AcmeSDKJsApiCDNExample&' +  // Message to embed into code
        '&anim=Spin' + // Spin is a fast demo
        '&xres=450' +  // higher than default resolution
        '&yres=450' +  // higher than default resolution
        '&cdn=1' +     // Request CDN delivery for accounts that have it
        '&apiKey=6d3873dc-af01-4cc0-bbb2-0f3537b21f80'  // CDN requests requires an apiKey.
        // Note the above api key is ACME's locked test apiKey, but with CDN permissions
        );

    orderRequest.onreadystatechange = function()
        {
        if (orderRequest.readyState === 4 && orderRequest.status === 200)
            {
            orderRequestJson = JSON.parse(orderRequest.responseText);
            document.getElementById('orderNumber').innerHTML =
                orderRequestJson.orderNumber;
            document.getElementById('mp4File').innerHTML =
                orderRequestJson.mp4;
            document.getElementById('mp4Cdn').innerHTML =
                orderRequestJson.cdnMp4;
            queryAndUpdateProgress();
            }
        };
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
        '/progress');
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
        };
    progressRequest.open('GET', progressRequest.tgtUrl);
    progressRequest.send();
    }

function retrieveMp4Animation()
    {
    mp4Animation = document.getElementById("mp4Animation");
    mp4Animation.setAttribute(
        "src",
        document.getElementById("mp4Cdn").innerHTML
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

