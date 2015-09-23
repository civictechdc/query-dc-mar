Query the DC MAR API
====================

The DC government's Master Address Repository (MAR) is a comprehensive service for geocoding District addresses and getting information about District addresses including ward, ANC, etc.

DC's official address lookup page: http://dcatlas.dcgis.dc.gov/mar/

MAR API overview: http://citizenatlas.dc.gov/newwebservices/locationverifier.asmx (There is a lot more here than address geocoding.)

Address lookup API documentation: http://citizenatlas.dc.gov/newwebservices/locationverifier.asmx?op=findLocation2

This repository contains a simple wrapper script to query the MAR.

For any address in the District you'll get a JSON dict with:

* The segmented address (street, quadrant, etc.)
* Latitude/longitude.
* Ward, ANC, SMD, police district, voting precinct.
* Census tract number.
* Google Street View URL.

To get set up:

	pip install -r requirements.txt

To run from the command line:

	python mar.py "3460 14th St NW #125"

Example output:

	{
	  "UNIT": "#125", 
	  "UNITNUMBER": "125", 
	  "details": "<STRONG>Normalized:</STRONG> 3460 14TH ST NW #125</br><STRONG>Parsed:</STRONG></br><EM>Address Number: </EM>3460</br><EM>Address Number Suffix: </EM></br><EM>Street Name: </EM>14TH</br><EM>Street Type: </EM>STREET</br><EM>Quad: </EM>NW</br>", 
	  "processTime": "0 seconds and 31 milliseconds", 
	  "returnBlkAddrDataset": null, 
	  "returnCDDataSet": {
	    "Address Return Codes": [
	      {
	        "Assessment": "Valid", 
	        "Component": "Street Type", 
	        "Parsed & Normalized": "STREET"
	      }, 
	      {
	        "Assessment": "Valid", 
	        "Component": "Quad", 
	        "Parsed & Normalized": "NW"
	      }, 
	      {
	        "Assessment": "Verified", 
	        "Component": "Full Address", 
	        "Parsed & Normalized": "3460 14TH STREET NW"
	      }
	    ]
	  }, 
	  "returnCodes": null, 
	  "returnDataset": {
	    "Table1": [
	      {
	        "ADDRESS_ID": 234578.0, 
	        "ADDRNUM": 3460.0, 
	        "ADDRNUMSUFFIX": null, 
	        "ANC": "ANC 1A", 
	        "ANC_2002": "ANC 1A", 
	        "ANC_2012": "ANC 1A", 
	        "CENSUS_TRACT": "002801", 
	        "CITY": "WASHINGTON", 
	        "CLUSTER_": "Cluster 2", 
	        "ConfidenceLevel": 100.0, 
	        "FOCUS_IMPROVEMENT_AREA": "NA", 
	        "FULLADDRESS": "3460 14TH STREET NW", 
	        "HAS_ALIAS": "Y", 
	        "HAS_CONDO_UNIT": "N", 
	        "HAS_RES_UNIT": "Y", 
	        "HAS_SSL": "Y", 
	        "IMAGEDIR": "20040816", 
	        "IMAGENAME": "DG064851.jpg", 
	        "IMAGEURL": "http://citizenatlas.dc.gov/mobilevideo", 
	        "LATITUDE": 38.93290697, 
	        "LONGITUDE": -77.03301422, 
	        "NATIONALGRID": "18S UJ 23784 11296", 
	        "NBHD_ACTION": " ", 
	        "POLDIST": "Police District - Fourth District", 
	        "PSA": "Police Service Area 409", 
	        "QUADRANT": "NW", 
	        "RES_TYPE": "RESIDENTIAL", 
	        "ROADWAYSEGID": 2236.0, 
	        "ROC": "NA", 
	        "SMD": "SMD 1A02", 
	        "SMD_2002": "SMD 1A02", 
	        "SMD_2012": "SMD 1A02", 
	        "SSL": "2678    0709", 
	        "STATE": "DC", 
	        "STATUS": "ACTIVE", 
	        "STNAME": "14TH", 
	        "STREETVIEWURL": "http://maps.google.com/maps?z=16&layer=c&cbll=38.93290697,-77.03301422&cbp=11,264.786887158805,,0,2.09", 
	        "STREET_TYPE": "STREET", 
	        "VOTE_PRCNCT": "Precinct 41", 
	        "WARD": "Ward 1", 
	        "WARD_2002": "Ward 1", 
	        "WARD_2012": "Ward 1", 
	        "XCOORD": 397137.54, 
	        "YCOORD": 140558.73, 
	        "ZIPCODE": 20010.0
	      }
	    ]
	  }, 
	  "sourceOperation": "DC Address"
	}
