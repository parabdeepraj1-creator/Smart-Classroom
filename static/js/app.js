/* =====================================
BACKEND CONFIGURATION
===================================== */

const BASE_URL = "http://localhost:8000";


/* =====================================
PAGE NAVIGATION
===================================== */

function showPage(pageId, clickedButton) {

    const pages =
        document.querySelectorAll(".page");


    pages.forEach(function (page) {
        page.classList.remove("active-page");
    });


    document
        .getElementById(pageId)
        .classList.add("active-page");


    const navButtons =
        document.querySelectorAll(".nav-btn");


    navButtons.forEach(function (button) {
        button.classList.remove("active");
    });


    clickedButton.classList.add("active");

}


/* =====================================
GET AND DISPLAY FACULTY
===================================== */

async function displayFaculty() {

    try {

        const response =
            await fetch(`${BASE_URL}/api/faculty`);


        if (!response.ok) {
            throw new Error(
                "Failed to load faculty"
            );
        }


        const data =
            await response.json();


        const list =
            document.getElementById("facultyList");


        list.innerHTML = "";


        data.faculty.forEach(
            function (person, index) {

                const row =
                    document.createElement("tr");


                row.innerHTML = `
                    <td>${index + 1}</td>
                    <td>${person.name}</td>
                    <td>${person.subjects.join(", ")}</td>
                `;


                list.appendChild(row);

            }
        );


        document
            .getElementById("facultyCount")
            .textContent =
            data.faculty.length;


    } catch (error) {

        console.error(
            "Faculty loading error:",
            error
        );

    }

}


/* =====================================
ADD FACULTY
===================================== */

const facultyForm =
    document.getElementById("facultyForm");


facultyForm.addEventListener(
    "submit",
    async function (event) {

        event.preventDefault();


        const name =
            document
                .getElementById("facultyName")
                .value
                .trim();


        const department =
            document
                .getElementById("facultyDepartment")
                .value
                .trim();


        const email =
            document
                .getElementById("facultyEmail")
                .value
                .trim();


        const subjectsInput =
            document
                .getElementById("facultySubjects")
                .value;


        const subjects =
            subjectsInput
                .split(",")
                .map(function (subject) {
                    return subject.trim();
                })
                .filter(function (subject) {
                    return subject !== "";
                });


        try {

            const response =
                await fetch(
                    `${BASE_URL}/api/faculty`,
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({
                            name: name,
                            department: department,
                            email: email,
                            subjects: subjects
                        })

                    }
                );


            if (!response.ok) {
                throw new Error(
                    "Failed to add faculty"
                );
            }


            facultyForm.reset();


            await displayFaculty();


        } catch (error) {

            console.error(
                "Add faculty error:",
                error
            );


            alert(
                "Could not add faculty. Please make sure the backend is running."
            );

        }

    }
);


/* =====================================
GET AND DISPLAY ROOMS
===================================== */

async function displayRooms() {

    try {

        const response =
            await fetch(`${BASE_URL}/api/rooms`);


        if (!response.ok) {
            throw new Error(
                "Failed to load rooms"
            );
        }


        const data =
            await response.json();


        const list =
            document.getElementById("roomList");


        list.innerHTML = "";


        data.rooms.forEach(
            function (room, index) {

                const row =
                    document.createElement("tr");


                row.innerHTML = `
                    <td>${index + 1}</td>
                    <td>${room.room_number}</td>
                    <td>${room.capacity}</td>
                    <td>${room.room_type}</td>
                `;


                list.appendChild(row);

            }
        );


        document
            .getElementById("roomCount")
            .textContent =
            data.rooms.length;


    } catch (error) {

        console.error(
            "Room loading error:",
            error
        );

    }

}


/* =====================================
ADD CLASSROOM
===================================== */

const roomForm =
    document.getElementById("roomForm");


roomForm.addEventListener(
    "submit",
    async function (event) {

        event.preventDefault();


        const roomNumber =
            document
                .getElementById("roomNumber")
                .value
                .trim();


        const capacity =
            document
                .getElementById("roomCapacity")
                .value;


        const roomType =
            document
                .getElementById("roomType")
                .value;


        const facilitiesInput =
            document
                .getElementById("roomFacilities")
                .value;


        const facilities =
            facilitiesInput
                .split(",")
                .map(function (item) {
                    return item.trim();
                })
                .filter(function (item) {
                    return item !== "";
                });


        try {

            const response =
                await fetch(
                    `${BASE_URL}/api/rooms`,
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({
                            room_number: roomNumber,
                            capacity: Number(capacity),
                            room_type: roomType,
                            facilities: facilities
                        })

                    }
                );


            if (!response.ok) {
                throw new Error(
                    "Failed to add classroom"
                );
            }


            roomForm.reset();


            await displayRooms();


        } catch (error) {

            console.error(
                "Add classroom error:",
                error
            );


            alert(
                "Could not add classroom. Please make sure the backend is running."
            );

        }

    }
);


/* =====================================
GENERATE TIMETABLE
===================================== */

const generateBtn =
    document.getElementById("generateBtn");


const generateAgainBtn =
    document.getElementById("generateAgainBtn");


generateBtn.addEventListener(
    "click",
    generateTimetable
);


generateAgainBtn.addEventListener(
    "click",
    generateTimetable
);


async function generateTimetable() {

    const statusMessage =
        document.getElementById("statusMessage");


    const department =
        document
            .getElementById("department")
            .value
            .trim();


    const semester =
        document
            .getElementById("semester")
            .value;


    const section =
        document
            .getElementById("section")
            .value
            .trim();


    if (
        department === "" ||
        semester === "" ||
        section === ""
    ) {

        statusMessage.textContent =
            "Please enter department, semester and section.";

        return;

    }


    statusMessage.textContent =
        "Generating timetable...";


    try {

        const response =
            await fetch(
                `${BASE_URL}/api/timetable/generate`,
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        department: department,
                        semester: Number(semester),
                        section: section
                    })

                }
            );


        if (!response.ok) {
            throw new Error(
                "Failed to generate timetable"
            );
        }


        const data =
            await response.json();


        displayTimetable(
            data.timetable
        );


        statusMessage.textContent =
            "Timetable generated successfully!";


        document
            .getElementById("classCount")
            .textContent =
            data.timetable.length;


        showTimetablePage();


    } catch (error) {

        console.error(
            "Timetable generation error:",
            error
        );


        statusMessage.textContent =
            "Error generating timetable.";


        alert(
            "Could not generate timetable. Please make sure the backend is running."
        );

    }

}


/* =====================================
DISPLAY TIMETABLE
===================================== */

function displayTimetable(timetable) {

    const body =
        document.getElementById("timetableBody");


    body.innerHTML = "";


    if (timetable.length === 0) {

        const row =
            document.createElement("tr");


        row.innerHTML = `
            <td colspan="5"
                class="empty-message">
                No timetable was generated.
            </td>
        `;


        body.appendChild(row);

        return;

    }


    timetable.forEach(function (item) {

        const row =
            document.createElement("tr");


        row.innerHTML = `
            <td>${item.day}</td>
            <td>${item.period_id}</td>
            <td>${item.subject_id}</td>
            <td>${item.teacher_id}</td>
            <td>${item.classroom_id}</td>
        `;


        body.appendChild(row);

    });

}


/* =====================================
OPEN TIMETABLE PAGE
===================================== */

function showTimetablePage() {

    const pages =
        document.querySelectorAll(".page");


    pages.forEach(function (page) {
        page.classList.remove("active-page");
    });


    document
        .getElementById("timetable")
        .classList.add("active-page");


    const navButtons =
        document.querySelectorAll(".nav-btn");


    navButtons.forEach(function (button) {
        button.classList.remove("active");
    });


    navButtons[3].classList.add("active");

}


/* =====================================
LOAD BACKEND DATA
WHEN WEBSITE STARTS
===================================== */

document.addEventListener(
    "DOMContentLoaded",
    async function () {

        await displayFaculty();

        await displayRooms();

    }
);
