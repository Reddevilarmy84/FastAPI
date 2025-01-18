
let nowTime = new Date()
function time() {
                var now = new Date()
                var seconds = now.getSeconds()
                var minutes = now.getMinutes()
                var hours = now.getHours()
                var AMPM = hours >= 12 ? 'PM' : 'AM'
                seconds = seconds < 10 ? '0' + seconds : seconds
                minutes = minutes < 10 ? '0' + minutes : minutes
                hours = hours === 12 ? hours : hours%12
                document.getElementById('time').innerHTML = `${AMPM}:${hours}:${minutes}:${seconds}`
                setTimeout(time, 1000)
            }
function Hello() {
                document.write("Hello! I am Java Script!")
            }
function showMessage() {
    alert("Привет от JavaScript!")
}
function changeText() {
    document.getElementById("myHeader").innerHTML = "Ты поменял текст в Header, но мы продолжаем кодить!"
}
function changeFontColor() {
    document.getElementById("myHeader").style.color = "red"
}
function cancelChanges() {
    document.getElementById("myHeader").style.color = ''
    document.getElementById("myHeader").textContent = 'Кодим...'
}
