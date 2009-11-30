This program uses my xgoogle library (see link (1) below) to find all the
plurks that have been indexed by Google.

I wrote it because I had plurked too much nonsense which I was not comfortable
with. I used this program in combination with delete-plurks GreaseMonkey
script that I also wrote (see link (2) below) to delete all the plurks that I
didn't like.

(1) http://www.catonmat.net/blog/python-library-for-google-search/
(2) http://github.com/pkrumins/plurk-delete-plurks

------------------------------------------------------------------------------

This program was written by Peteris Krumins (peter@catonmat.net).
His blog is at http://www.catonmat.net  --  good coders code, great reuse.

The code is licensed under the MIT license.

------------------------------------------------------------------------------

How to use this program?
------------------------

First you will need to get xgoogle. Get it from link (1) above. Unzip it, and
put this program in the same directory.

Next open the program in a text editor and edit the `queries` variable. It
contains all the queries that you want xgoogle to search for on Google. Notice
how they all contain 'site:plurk.com' so that the searched were performed only
over plurk pages.

Then edit `username` variable and set it to your nick.

(This all of course can be made more convenient, but this is just a quick and
dirty program to do the job.)

When run, program will output a list of URLs that you have plurked on. Use the
GreaseMonkey script from link (2) above to delete them (you may only delete
your own plurks).

If you don't want some plurks to be listed as output, include them in
`ignore_ids` set.


------------------------------------------------------------------------------


Sincerely,
Peteris Krumins
http://www.catonmat.net

