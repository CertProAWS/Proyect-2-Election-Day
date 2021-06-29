# Project #2 Election Day

#### Participants: 4
There is a growing concern towards the transparency and integrity of elections in the country you live in. The government wants to implement a software solution that helps increase the trust in the electoral system.

The whole country votes through ballot papers which are stored in ballot boxes. Once all votes are cast, they are counted in a whiteboard. With the correct results they create the official document for the city/school/booth and send it to the central government for counting.

One of the mayor concerns of transparency is the step where the votes are copied over, there is a high chance this step is done incorrectly, either by mistake or purposefully.

</br>
 </br>
 <p align="center">
    <img src="https://github.com/AleS900/prueba/blob/master/assets/Electionay-Revised.jpg" width="600" height="450"/>
 </p>


# Election officials API

The system you have to develop is a verification mechanism on site. The election officials will fill the booth results in the system and upload a picture of the official document along the whiteboard. The idea is to have a way to verify the step from whiteboard to document. Then, we should make sure that these numbers match the votes cast.


# Participants API

Whenever a person enters the booth to vote, it should be registered in the database with the time of arrival. We should register how many absentees there are per school, city and nationwide.


# Elections results

The output should be the results of the election nationwide, by city and by school. These results should be available for people to see in a public website. This website will allow people to see where they voted and what the result was along with the picture that proves it.


# Invalidations API

There needs to be an API for the government that

- Allows to invalidate a booth. Booths will be invalidated if there is a mismatch between the picture and the final result, or if the absentees don’t match the votes cast
- Shows all invalidated booths
- Shows a count of all invalidated booths by city, sorted by the highest count
- Shows a count of all invalidated booths by school in a city, sorted by the highest count

