//  Random background
var dir = '../images/';
var size = 3;
var dict = {
  1: "rocks.jpg",
  2: "rainDrops.jpg",
  3: "redEggs.jpg"};
var random= Math.floor(Math.random() * size) + 1;
document.body.style.backgroundImage="url(" + dir + dict[1] + ")";
