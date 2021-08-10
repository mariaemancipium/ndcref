# ndcref
A listing of all NDCs, as of June 8 2020

How this works - you'll need to go to the FDA's website and grab the latest source file if you want to build this thing from the most recent data. https://open.fda.gov/apis/drug/drugsfda/download/

Basically, these files work together to take the raw json you get from the FDA site and create a flat excel file. In order to limit this incredibly massive dataset, I went through and manually deleted things like hand sanitizer and sunscreen, since I developed this for a hospital setting.

Useful as a vlookup tool when your EHR only provides an NDC instead of a drug name. Also can classify drugs so that you can take a look at bulk data and understand treatment trends.
