# CGI-Primer-Project
A simple CGI project

Log:
- Created a new repository called CGI-Primer-Project
- Setup environment for cgi
- Connected to the Perl interpreter
- Wrote code to connect via http to another server (http://www.twitter.com)
- Added a for loop to access the list of response variables within the header sent by twitter
- Added a loop to access the environment variables
- Response to GET added
- If the query string is "HTML", then the page will be rendered in html.
- Provided a stylesheet for the html page that is generated under /djh73969/styles/style.css

Summary:

This application is written in Perl and uses the cgi protocol. When it is called upon it checks to see if the 
query string has been set. If it has been set to "HTML", a page listing the path to the Perl interpreter, the
environment variables that were sent to the server, and the response variables sent by twitter.com is sent back as a
response to the browser. However, if the query string is not sent, the page will not be rendered with a style sheet or 
any formatting.
  
