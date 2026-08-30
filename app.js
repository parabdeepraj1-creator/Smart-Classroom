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
FACULTY DATA
===================================== */

let faculty = [
{
name: "Prof. Rahul",
subject: "DBMS"
},
{
name: "Prof. Priya",
subject: "Python"
},
{
name: "Prof. Amit",
subject: "Web Technology"
}
];

/* =====================================
ROOM DATA
===================================== */

let rooms = [
{
name: "Room 101",
capacity: 60,
type: "Classroom"
},
{
name: "Room 102",
capacity: 50,
type: "Smart Classroom"
},
{
name: "Lab 201",
capacity: 40,
type: "Computer Lab"
}
];

/* =====================================
ADD FACULTY
===================================== */

const facultyForm =
document.getElementById("facultyForm");

facultyForm.addEventListener(
"submit",
function (event) {

    event.preventDefault();


    const name =
        document
            .getElementById("facultyName")
            .value;


    const subject =
        document
            .getElementById("facultySubject")
            .value;


    faculty.push({
        name: name,
        subject: subject
    });


    displayFaculty();


    facultyForm.reset();

}

);

function displayFaculty() {

const list =
    document.getElementById("facultyList");


list.innerHTML = "";


faculty.forEach(
    function (person, index) {

        const row =
            document.createElement("tr");


        row.innerHTML = `
            <td>${index + 1}</td>
            <td>${person.name}</td>
            <td>${person.subject}</td>
        `;


        list.appendChild(row);

    }
);


document
    .getElementById("facultyCount")
    .textContent =
    faculty.length;

}

/* =====================================
ADD CLASSROOM
===================================== */

const roomForm =
document.getElementById("roomForm");

roomForm.addEventListener(
"submit",
function (event) {

    event.preventDefault();


    const name =
        document
            .getElementById("roomName")
            .value;


    const capacity =
        document
            .getElementById("roomCapacity")
            .value;


    const type =
        document
            .getElementById("roomType")
            .value;


    rooms.push({
        name: name,
        capacity: capacity,
        type: type
    });


    displayRooms();


    roomForm.reset();

}

);

function displayRooms() {

const list =
    document.getElementById("roomList");


list.innerHTML = "";


rooms.forEach(
    function (room, index) {

        const row =
            document.createElement("tr");


        row.innerHTML = `
            <td>${index + 1}</td>
            <td>${room.name}</td>
            <td>${room.capacity}</td>
            <td>${room.type}</td>
        `;


        list.appendChild(row);

    }
);


document
    .getElementById("roomCount")
    .textContent =
    rooms.length;

}

/* =====================================
TIMETABLE DATA
===================================== */

let timetable = [];

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

function generateTimetable() {

const statusMessage =
    document.getElementById("statusMessage");


statusMessage.textContent =
    "Generating timetable...";


setTimeout(function () {

    timetable = [

        {
            day: "Monday",
            time: "09:00 - 10:00",
            subject: "DBMS",
            faculty: "Prof. Rahul",
            room: "Room 101",
            batch: "TY-A"
        },

        {
            day: "Monday",
            time: "10:00 - 11:00",
            subject: "Python",
            faculty: "Prof. Priya",
            room: "Room 102",
            batch: "TY-A"
        },

        {
            day: "Monday",
            time: "11:00 - 12:00",
            subject: "Web Technology",
            faculty: "Prof. Amit",
            room: "Lab 201",
            batch: "TY-A"
        },

        {
            day: "Tuesday",
            time: "09:00 - 10:00",
            subject: "Python",
            faculty: "Prof. Priya",
            room: "Room 101",
            batch: "TY-B"
        },

        {
            day: "Tuesday",
            time: "10:00 - 11:00",
            subject: "DBMS",
            faculty: "Prof. Rahul",
            room: "Room 102",
            batch: "TY-B"
        }

    ];


    displayTimetable();


    statusMessage.textContent =
        "Timetable generated successfully!";


    document
        .getElementById("classCount")
        .textContent =
        timetable.length;


    showTimetablePage();

}, 500);

}

/* =====================================
DISPLAY TIMETABLE
===================================== */

function displayTimetable() {

const body =
    document.getElementById("timetableBody");


body.innerHTML = "";


timetable.forEach(function (item) {

    const row =
        document.createElement("tr");


    row.innerHTML = `
        <td>${item.day}</td>
        <td>${item.time}</td>
        <td>${item.subject}</td>
        <td>${item.faculty}</td>
        <td>${item.room}</td>
        <td>${item.batch}</td>
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