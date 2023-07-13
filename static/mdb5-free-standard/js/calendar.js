var currentDate = new Date();

var year = currentDate.getFullYear();
var month = currentDate.getMonth();


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


getFullMonthView(6, 2023);

