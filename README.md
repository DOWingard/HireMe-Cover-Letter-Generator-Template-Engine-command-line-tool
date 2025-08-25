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
## Best Practice:
* Do not use slashes in your template names because it can cause path issues, just avoid in general for any input in this tool.
* Quotes are not needed for string inputs, but if theres spaces in the input, use quotes.

## Command List

Configure the tool: 
``` 
HireMe --configure
```

Show current configuration:
```
HireMe --show
```

Generate a PDF [optional cmds]:  
```
HireMe HireMe -G --company "Big Company" --role "High Paying Job" [--date "00/00/00" --template "management1"]
```

Clear the configured storage folder:
```
HireMe --clean
```

Complete reset and reconfigure:
```
HireMe --reset
```

Add more templates to the tool and update template keys and {{LABELS}} [optional cmds]:
```
HireMe --update [--source /path/to/new/templates/folder]
```

Reset the {{LABELS}} used in the template, allows user to optionally add their own:
```
HireMe --resetlabels
```

Recreate the keywords assigned to each template:
```
HireMe --resetkwds
```

Read some crucial information:
```
HireMe --info
```











