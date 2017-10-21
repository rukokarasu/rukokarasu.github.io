function setup() {
    createCanvas(720, 480);
    background(255);
}

let ticks = 0;
var lastMouseX = null;
var lastMouseY = null;

function draw() {
    const r = random(0);
    const m = millis();
    const t = (millis() / 10);
    const color = tinycolor({h: mouseX / 2, s: 100, v: 100});
    const hjhjh = color.getFormat();
    const rgbColor = color.toRgb();
    stroke(rgbColor.r, rgbColor.g, rgbColor.b, 250);
    if (mouseIsPressed) {
        if (lastMouseX == null || lastMouseY == null) {
            lastMouseX = mouseX;
            lastMouseY = mouseY;
        } 
        line(lastMouseX, lastMouseY, mouseX, mouseY);
        lastMouseX = mouseX;
        lastMouseY = mouseY;
    } else {
        lastMouseX = null;
        lastMouseY = null;
    }
    ticks += 1;
}
