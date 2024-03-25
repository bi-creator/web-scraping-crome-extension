// content.js
chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
      if (request.message === "getDOMContent") {
        sendResponse({ content: document.documentElement.outerHTML });
      }
    }
  );
  