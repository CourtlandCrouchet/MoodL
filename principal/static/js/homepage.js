
function randombg(){
  //image directory
  var dir = '../images/';
  var dict = {
    0: "redSky.jpg",
    1: "cat.jpg",
    2: "yellowLeaves.jpg"};
  var random= Math.floor(Math.random() * 3) + 1;
  document.body.style.backgroundImage="url(" + dir + dict[random] + ")";
}
