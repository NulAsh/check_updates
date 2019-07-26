# check_updates
Script for automatic check for updates on webpages

This program is designed to automatically check for updates on web pages. The file check_updates.txt contains a list of objects to be scanned, in groups of 4 lines. The first line of the group is the URL of the page to check. The second is a flag denoting the method by which subsequent lines will be processed. At the moment, there are two methods implemented.

Flag 0:

The third line of the group is a retexp containing one subgroup (in parentheses). From the first match found, the subgroup will be highlighted and compared to the fourth line. If they do not match, an entry will be made to the check_updates_result.txt file. If no match is found on the page, or an error occurs on the page downloading, an entry will also be made about this.

Flag 1:

for complex cases and advanced users who know not only regexps, but also python as a whole. The third line will be passed first through eval(), then through exec().

Add this program to the Task Scheduler so that it runs automatically every day.
Python 3.x must be installed on the computer for the program to work.

Set permissions for the program and the task file check_updates.txt so that only the administrator can make changes there. An attacker who was able to edit them will be able to execute any command.
