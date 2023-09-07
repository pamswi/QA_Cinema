// Get references to the date buttons and screening times container
const dateButtons = document.querySelectorAll('.date-button');
const screeningTimesContainer = document.querySelector('.screening-times');
const bookingFormContainer = document.querySelector('.booking-form-container'); // Assuming you have a container for the booking form

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
                // Create a list of screening times with buttons to display
                const screeningTimesList = screeningData.map((screening) => `
                    <li>
                        <button class="screening-button" data-screening-id="${screening.id}">
                            Screen ${screening.screen_number}: ${screening.time}
                            Book Now
                        </button>
                    </li>
                `).join('');

                // Update the content of the screening times container
                screeningTimesContainer.innerHTML = `
                    <h3>All Showtimes ${selectedDate}</h3>
                    <ul>${screeningTimesList}</ul>
                `;

                // Add a click event listener to each screening button
                const screeningButtons = document.querySelectorAll('.screening-button');
                screeningButtons.forEach((screeningButton) => {
                    screeningButton.addEventListener('click', () => {
                        // Handle button click actions here
                        const screeningId = screeningButton.getAttribute('data-screening-id');
                        generateBookingForm(screeningId); // Call a function to generate the booking form
                    });
                });
            })
            .catch((error) => {
                console.error('Error:', error);
                screeningTimesContainer.innerHTML = 'Failed to fetch screening data.';
            });
    });
});

// Function to generate the booking form
function generateBookingForm(screeningId) {
    // You can create and append the booking form HTML here
    const bookingFormHTML = `
        <h3>Booking Form</h3>
        <h3>Booking Form</h3>
        <form method="POST">
            <input type="hidden" name="screening_id" value="{{ form.screening_id.data }}">
            <label for="user_id">{{ form.user_id.label }}</label>
            <input type="text" id="user_id" name="user_id" value="{{ form.user_id.data }}"><br>

            <label for="discounted_ticket_number">{{ form.discounted_ticket_number.label }}</label>
            <input type="number" id="discounted_ticket_number" name="discounted_ticket_number" value="{{ form.discounted_ticket_number.data }}"><br>

            <label for="full_price_ticket_number">{{ form.full_price_ticket_number.label }}</label>
            <input type="number" id="full_price_ticket_number" name="full_price_ticket_number" value="{{ form.full_price_ticket_number.data }}"><br>

            <label for="ticket_type">{{ form.ticket_type.label }}</label>
            <select id="ticket_type" name="ticket_type">
                <option value="standard" {% if form.ticket_type.data == 'standard' %}selected{% endif %}>Standard</option>
                <option value="vip" {% if form.ticket_type.data == 'vip' %}selected{% endif %}>VIP</option>
            </select><br>

            <label for="quantity">{{ form.quantity.label }}</label>
            <input type="number" id="quantity" name="quantity" value="{{ form.quantity.data }}"><br>

            <label for="price">{{ form.price.label }}</label>
            <input type="text" id="price" name="price" value="{{ form.price.data }}"><br>

            <input type="submit" value="{{ form.submit.label }}">
        </form>
    `;

    // Update the content of the booking form container
    bookingFormContainer.innerHTML = bookingFormHTML;
}