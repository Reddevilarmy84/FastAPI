
let nowTime = new Date()
function TimeNow() {
                document.write(nowTime.toLocaleTimeString())
            }
function showTime() {
                var date = nowTime.toDateString()
                var time = nowTime.toTimeString()
                alert(date + " " + time)
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
