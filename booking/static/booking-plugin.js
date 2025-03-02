(function () {
    async function fetchAvailableSlots(date) {
        const response = await fetch(`http://127.0.0.1:8000/available-slots/?date=${date}`);
        return response.json();
    }

    async function bookAppointment(data) {
        const response = await fetch("http://127.0.0.1:8000/book-appointment/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data),
        });
        return response.json();
    }

    function createBookingUI() {
        const container = document.createElement("div");
        container.innerHTML = `
            <label>Select Date:</label>
            <input type="date" id="booking-date">
            <button id="fetch-slots">Check Slots</button>
            <div id="slots-container"></div>
            <form id="booking-form" style="display:none;">
                <input type="text" id="name" placeholder="Your Name" required>
                <input type="text" id="phone" placeholder="Phone Number" required>
                <select id="time-slot"></select>
                <button type="submit">Book</button>
            </form>
            <p id="booking-status"></p>
        `;
        document.body.appendChild(container);

        document.getElementById("fetch-slots").addEventListener("click", async () => {
            const date = document.getElementById("booking-date").value;
            if (!date) return alert("Please select a date");
            
            const { available_slots } = await fetchAvailableSlots(date);
            const slotSelect = document.getElementById("time-slot");
            slotSelect.innerHTML = available_slots.map(slot => `<option>${slot}</option>`).join("");
            
            document.getElementById("booking-form").style.display = "block";
        });

        document.getElementById("booking-form").addEventListener("submit", async (e) => {
            e.preventDefault();
            const data = {
                name: document.getElementById("name").value,
                phone_number: document.getElementById("phone").value,
                date: document.getElementById("booking-date").value,
                time_slot: document.getElementById("time-slot").value
            };

            const response = await bookAppointment(data);
            document.getElementById("booking-status").textContent = response.message || "Error booking";
        });
    }

    createBookingUI();
})();
