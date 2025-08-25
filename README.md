# HireMe command line tool

Do you hate writing cover letters as much as I do?  Build a template and automate the process. F*** it, build a bunch of templates and automate the entire thing!  
  
This tool generates pdf fles by replacing as many labels within the text as your little heart desires (no seriously, add as many as you want)

## Standard Usage:
After installing HireMe, you must set your configuration:
```
HireMe --configure
```
For the configuration method, you will need to provide a folder for HireMe to work in.  
Next (still within configuration method), you give folder where your docx templates are located and it will copy them into the root folder. 

After configuring, you can generate cover letters with:
```
HireMe -G --company "COMPANY NAME" --role "COMPANY ROLE" --template keyword
```
If theres only 1 template in the directory, omit the final command, and use:
```
HireMe -G --company "COMPANY NAME" --role "COMPANY ROLE"
```






