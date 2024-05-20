from dataclasses import dataclass

@dataclass
class Movie:
    id: int
    title: str
    year: int
    rating: str
    director: str

    def get_movie_details(self):
        details = f"id: {self.id}, title: {self.title}, year: {self.year}, "
        details += f"rating: {self.rating}, director: {self.director}"
        return details