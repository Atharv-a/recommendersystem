# RECOMMENDER SYSTEMS
- Built a recommender system based on content based filtering.
- Preprocessed Dataset of Tmdb with 5000 movies and created Tags for all movies.
- With help of scikit-learn Converted all tags to vector and calculated cosine distance of all vectors with respect to each other to find most familiar movies.
- Created a database on Mongodb to store all cosine distance and to fetch data for a movie whenever a recommendation has to be made. 
- Used Render to create a web application for deploying Movie recommender system.
- Application fetches five most similar movies with respect to one entered and prints their names with respective posters.Posters are fetched with the help of Tmdb API.

click https://movie-recommender-0yro.onrender.com to get site.

Type movie name in the search box.

![img1](https://user-images.githubusercontent.com/95877070/233489186-34f2132c-0614-4105-adc6-0885110cb1f6.png)

Then Click on recommend button.

![img2](https://user-images.githubusercontent.com/95877070/233489354-217145fa-a613-4058-afe6-a9711ac077ca.png)

Five most similiar movies will be shown to you.

![img3](https://user-images.githubusercontent.com/95877070/233489516-0c4ff7dc-e281-4269-916e-d682e26b75c0.png)

