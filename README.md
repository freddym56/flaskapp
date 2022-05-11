# Simple flask api to query sqlite database
The database contains data on Google app downloads from the playstore.

# This is the endpoint to view data.
`http://127.0.0.1:8080/apps`

# can also paginate through the data using the page param
`http://127.0.0.1:8080/apps?page=1`

# Default item limit is 20. Can change using the limit param
`http://127.0.0.1:8080/apps?page=1&limit=100`
