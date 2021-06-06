#URL's
['http:localhost://localhost:PORT/movies/']
###METHODS
post - request:
  sample data  
` {
        "title":"movie Name"
        "genres":["genre1", "genre2"]
    }`

succes-Resposnse : ("Movie added", 200) 
Error response :  Error, 401



get - request:
    succes-Resposnse : (movies.pdf, 200)
    Error response :  Error, 401

put - request :
        `{ 
                "id":Int (important)
                "titel": String
                "genres":List
        }`
        provie atleast one data to update `title or genres`
        success-resposnse :("movie added", 200)
        error-response : Error, 401

delete - request:
           `{
                "id": int
           }`
            success-response: ("movie removed", 200)
            error-response: (error, 401)

            
[http://localhost:PORT/movies/<title>/]
get - request:
        movies/movie_name/
        success-response: `{
                                "id":int
                                 "title":movie title
                                  "genres": [genre]
                          }` 


[http://localhost:PORT/search/<search>/]

get - request
      <search> is the search pathhern
       /search/the king
        
       success-response: (movies.pdf, 200)
