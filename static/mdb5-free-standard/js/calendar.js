var courses_data = JSON.parse(getCookie("courses_data"));

var currentDate = new Date();

var year = currentDate.getFullYear();
var month = currentDate.getMonth();


function getCourseById(course_id) {
    for (var course in courses_data) {
        course = courses_data[course];

        if (course["course_id"] === course_id) {
            return course;
        }
    }

    return null;
}


function getEventsOfGivenDay(day_in_unix_time) {
    var events = [];
    for (var course in courses_data) {
        course = courses_data[course];
        let course_day_unix_time = new Date(course["date"]).setHours(0,0,0,0);

        if (course_day_unix_time === day_in_unix_time) {
            events.push(course);
        }
    }

    return events;
}

function getAllDaysInMonth(month, year) {  // month starts with 0 (0 => january)
    var date = new Date(year, month, 1);
    var days = [];
    while (date.getMonth() === month) {
        days.push(new Date(date));
        date.setDate(date.getDate() + 1);
    }
    return days;
}

function getLastWeekOfPreviousMonth(month, year) {
    var days = [];
    let monday_reached = false;

    for (let i=1; i < 7; i++) {
        var day = new Date(year, month, 1);
        day.setDate(day.getDate() - 7 + i);
        if (day.getDay() === 1){
            monday_reached = true;
        }

        if (monday_reached) {
            days.push(day);
        }
    }

    return days
}

function getFirstWeekOfNextMonth(month, year) {

    var days = [];
    let monday_reached = false;

    for (let i=1; i < 8; i++) {
        var day = new Date(year, month + 1, 0);
        day.setDate(day.getDate() + i);
        if (day.getDay() === 1){
            break;
        }
        days.push(day);
    }

    return days
}

function getFullMonthView(month, year) {

    var days = [];
    let daysOfPreviousMonth = getLastWeekOfPreviousMonth(month, year);
    let daysOfCurrentMonth = getAllDaysInMonth(month, year);
    let daysOfNextMonth = getFirstWeekOfNextMonth(month, year);

    for (var day of daysOfPreviousMonth){
        days.push(day);
    }

    for (var day of daysOfCurrentMonth){
        days.push(day);
    }

    for (var day of daysOfNextMonth){
        days.push(day);
    }

    return days;
}

function getDayName(dayNumber) {
    switch(dayNumber) {
          case 0:
                return "Sonntag";
          case 1:
                return "Montag";
          case 2:
                return "Dienstag";
          case 3:
                return "Mittwoch";
          case 4:
                return "Donnerstag";
          case 5:
                return "Freitag";
          case 6:
                return "Samstag";
          default:
                return "DayNameError";
    }
}

function getMonthName(monthNumber) {
    switch(monthNumber) {
          case 0:
                return "Januar";
          case 1:
                return "Februar";
          case 2:
                return "März";
          case 3:
                return "April";
          case 4:
                return "Mai";
          case 5:
                return "Juni";
          case 6:
                return "Juli";
          case 7:
                return "August";
          case 8:
                return "September";
          case 9:
                return "Oktober";
          case 10:
                return "November";
          case 11:
                return "Dezember";
          default:
                return "MonthNameError";
    }
}

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "{}";
}


getFullMonthView(6, 2023);

