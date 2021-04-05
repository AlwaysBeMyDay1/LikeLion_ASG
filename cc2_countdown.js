const dDay = '1 sep 2021'; 

function countdown() { 
    const dDayDate = new Date(dDay); 
    const currentDate = new Date(); 
    
    const totalSeconds = (dDayDate - currentDate) / 1000; 
    const days = Math.floor(totalSeconds / 3600 / 24); 
    const hours = Math.floor(totalSeconds / 3600) % 24; 
    const minutes = Math.floor(totalSeconds / 60) % 60; 
    const seconds = Math.floor(totalSeconds) % 60;
    
    document.getElementById('days').innerText = formatTime(days); 
    document.getElementById('hours').innerText = formatTime(hours); 
    document.getElementById('minutes').innerText = formatTime(minutes); 
    document.getElementById('seconds').innerText = formatTime(seconds); 
} 

function formatTime(time) { 
    return time < 10 ? '0' + time : time; 
} 

setInterval(countdown, 1000);

