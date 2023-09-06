// Get references to the date buttons and screening times container
const dateButtons = document.querySelectorAll('.date-button');
const screeningTimesContainer = document.querySelector('.screening-times');

// Add a click event listener to each date button
dateButtons.forEach((button) => {
    button.addEventListener('click', () => {
        const selectedDate = button.getAttribute('data-date'); // Get selected date
        const movieId = button.getAttribute('data-movie-id'); // Get movie ID

        // Make a GET request to your Flask API endpoint with the selected date and movie ID
        fetch(`/api/movies/${movieId}?day=${selectedDate}`)
            .then((response) => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then((screeningData) => {
                
                const screeningTimesList = screeningData.map((screening) => `
                    <li>
                        Screen ${screening.screen_number}: ${screening.time}
                        (Current Capacity: ${screening.current_capacity})
                    </li>
                `).join('');

                // Update the content of the screening times container
                screeningTimesContainer.innerHTML = `
                    <h3>All Showtimes ${selectedDate}</h3>
                    <ul>${screeningTimesList}</ul>
                `;
            })
            .catch((error) => {
                console.error('Error:', error);
                screeningTimesContainer.innerHTML = 'Failed to fetch screening data.';
            });
    });
});

