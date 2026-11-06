
from mcp.server import MCPServer

# Create our Movie Recommendation MCP Server
mcp = MCPServer("Movie Recommendation Server")

# MCP Tool 1: Search for movies
@mcp.tool()
def search_movies(
    genre: str,
    language: str,
    max_minutes: int
) -> list[dict]:
    """Search movies by genre, language, and duration.
    Use 'any' if genre or language is unspecified."""

    movies = [
        {"title": "Palm Springs", "genre": "comedy",
         "language": "English", "minutes": 90},

        {"title": "The Grand Budapest Hotel", "genre": "comedy",
         "language": "English", "minutes": 99},

        {"title": "Knives Out", "genre": "thriller",
         "language": "English", "minutes": 130},

        {"title": "Jathi Ratnalu", "genre": "comedy",
         "language": "Telugu", "minutes": 148},

        {"title": "Kshanam", "genre": "thriller",
         "language": "Telugu", "minutes": 110}
    ]

    matches = [
        movie for movie in movies
        if (genre.lower() == "any"
            or genre.lower() == movie["genre"].lower())
        and (language.lower() == "any"
             or language.lower() == movie["language"].lower())
        and movie["minutes"] <= max_minutes
    ]

    return matches



# MCP Tool 2: Get details of a specific movie
@mcp.tool()
def get_movie_details(title: str) -> dict:
    """Get the genre, language, and duration of a
    specific movie by its title."""

    movies = [
        {"title": "Palm Springs", "genre": "comedy",
         "language": "English", "minutes": 90},

        {"title": "The Grand Budapest Hotel", "genre": "comedy",
         "language": "English", "minutes": 99},

        {"title": "Knives Out", "genre": "thriller",
         "language": "English", "minutes": 130},

        {"title": "Jathi Ratnalu", "genre": "comedy",
         "language": "Telugu", "minutes": 148},

        {"title": "Kshanam", "genre": "thriller",
         "language": "Telugu", "minutes": 110}
    ]

    for movie in movies:
        if movie["title"].lower() == title.strip().lower():
            return movie

    return {"error": "Movie not found in our catalog"}


# Start the MCP server
if __name__ == "__main__":
    mcp.run()
