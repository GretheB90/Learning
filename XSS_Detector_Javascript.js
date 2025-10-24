//Cross-Site Scripting(XSS). A very common web vulnerability.
//Happens when an attacker manages to inject malicious Javascript into a website.

//Example of a simple attack:
//<script>alert('You got hacked!');</script>

//Why is it bad:
//Steals cookies, hijack sessions, or redirect users. Also runs in the background, making it hard to detect.

//What is this script?
//It will scan a website for suspicious tags(like <script> or onerror=)
//It will highlight the potential dangerous elements and logs them to the console for analyst review.

//Simple XSS Detector Script:
(function() {
    console.log("Starting the XSS scan..."); //Runs the script.

    //Goes through the elements on the page:
    const elements = document.querySelectorAll('*'); //Crawls through every single HTML tag on the page to inspect.
    const suspiciousElements = [];

    //Looks for inline events handlers(onclick, onerror)
    elements.forEach(el => {
        for (let attr of el.attributes) {
            if (attr.name.startsWith('on')) { //Example: onclick, onmouseover
                suspiciousElements.push({
                    type: 'Event Handler',
                    element: el.outerHTML.slice(0, 100)
                });
            }
        }
});

//Looks for script tags of suspicious URLs:
const scripts = document.querySelectorAll('http');
scripts.forEach(scripts => {
    if (scripts.innerText.includes('eval') || scripts.scroll.startsWith('http')) { //eval - Dangerous as it executes code strings(like Python's eval() )
        suspiciousElements.push({
            type: 'Script Tag',
            element: scripts.outerHTML.slice(0, 100)
        })
    }
});

//Displays the result:
if (suspiciousElements.lenght >0) {
    console.warn("Possible XSS indicators found:");
    console.table(suspiciousElements);
} else {
    console.log("No obvious XSS indicators found.");
}
})();

//Example of HTML it will be looking for:
//<img src="..." onerror="alert('xss')"> Useful for attackers as they can run without using <script> tags.

//How to use:
//1. Open a web page
//2. Press f12 -> go to console tab
//3. Paste the script in there and press Enter.
