// popup.js
document.addEventListener('DOMContentLoaded', function() {
    console.log("Popup script loaded.");
  
    var button = document.getElementById('getDOMContent');
    if (button) {
      button.addEventListener('click', function() {
        chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
          var tabId = tabs[0].id;
  
          chrome.tabs.sendMessage(tabId, { message: "getDOMContent" }, function(response) {
            if (chrome.runtime.lastError) {
              console.error("Error sending message:");
            } else {
              console.log("Content received:", response.content);
            }
          });
        });
      });
    } else {
      console.error("Button with ID 'getDOMContent' not found.");
    }
  });
  