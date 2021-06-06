# URL's

[http:localhost://localhost:PORT/movies/](http://localhost:port/movies)
### METHODS

1. #### post - request:

   body json

       {
          "title":"movie Name"
          "genres":["genre1", "genre2"]
        }


    1. succes-Resposnse : `("Movie added", 200)` 
    2. Error response :  `Error, 401`



2. #### get - request:
    1. succes-Resposnse : `(movies.pdf, 200)`
    2. Error response :  `Error, 401`

3. #### put - request :

   body json

           { 
               "id":Int (important)
               "titel": String
               "genres":List
           }



       provie atleast one data to update `title or genres`
       1. success-resposnse :`("movie added", 200)`
       2. error-response : `Error, 401`


4. #### delete - request:
   body json

           {
            "id": int
            }

    1. success-response: ("movie removed", 200)
    2. error-response: (error, 401)


[http://localhost:PORT/movies/<title>/](http://localhost:port/movies/<title>)

### MTHODS

1. #### get - request:
   movies/movie_name/

    `1. success-response
       {
       "id":int
       "title":movie title
       "genres": [genre]
       }
      `


[http://localhost:PORT/search/<search>/](http://localhost:port/search<search>)

### METHODS

1. #### get - request
   `<search>` is the search patern
   `/search/the king`

       success-response: `(movies.pdf, 200)`
