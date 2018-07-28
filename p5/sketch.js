var x = 900;
var y = 0;
function setup() {
  var canvasWidth = 1000;
  var canvasHeight = 680;
  createCanvas(canvasWidth, canvasHeight);
  frameRate(60);
}

function draw() {
  background(200);
  fill(255,0,0);
  x = x-2;
  y = y+2;
  rect(x, y, 100, 100);

}
